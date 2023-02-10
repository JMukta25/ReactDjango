from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import UserSerializer, TicketSerializer, userHistorySerializer, storeUserHistorySerializer
from djangoRestApp.models import User, ticket, userHistory
import pandas as pd
import numpy as np 
import spacy 
import sqlite3 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  
import math

sa = SentimentIntensityAnalyzer() 
finance_words = [
    "payment",
    "income",
    "amount",
    "salary",
    "job",
    "class",
    "middle",
    "family",
    "economics",
    "money",
    "banking",
    "investment",
    "budget",
    "accountancy",
    "remuneration",
    "compensation",
    "reimbursement",
    "gratuity",
    "wages",
    "reward",
    "revenue",
    "earnings",
    "salary",
    "wages",
    "profit",
    "yield",
    "stipend",
    "allowance",
    "grant",
    "scholarship",
    "bursary",
    "salary",
    "compensation",
    "salary",
    "wages",
    "pay",
    "income",
    "earnings",
    "remuneration",
    "compensation",
    "internship",
    "placement",
    "traineeship",
    "apprenticeship",
    "work-experience",
    "co-op",
    "on-the-job-training",
    "job",
    "career",
    "employment",
    "occupation",
    "position",
    "vocation",
    "livelihood",
    "wealth", 
    "amount"
]
var = list(set(finance_words))

def equal(pat, text):
    # Ignore non-space and non-word characters
    ans = "" 
    for i in pat:
        ans+='[\s]*'
        s = "[" + i.lower() + "|" + i.upper() + "]"  
        ans+=s
    ans+='[\s]*' 
    # print(ans)
    return 1 if len(re.findall(ans,text)) > 0 else 0

def negativity(s):
    neg = 0 
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(s)
    for i in doc.sents:
        for j in var: 
            if (equal(j,str(i)) or equal(nlp(j)[0].lemma_,str())):
                neg+=sa.polarity_scores(str(i))['neg'] 
                # print(i," ",sa.polarity_scores(str(i))['neg'])
    return neg

def euclidean_distance(x,y):
    l = []
    for i in range(len(x)):
        l.append((x[i]-y[i])*(x[i]-y[i])) 
    return math.sqrt(sum(l))
def KNNClassifier(k,row,df):
    d = dict() 
    row['x1'] = len(row['text']) / 300 
    row['x2'] = equal(row['userName'], row['text']) and equal(row['ticket_name'],row['text'])
    corpus = [row['text'],row['ticket_func']] 
    cv = CountVectorizer() 
    vector = cv.fit_transform(corpus) 
    similarity_score = cosine_similarity(vector)[0][1] 
    row['x3'] = similarity_score
    # row['x4'] = sa.polarity_scores(row['text'])['neg'] 
    row['x5'] = negativity(row['text'])
    l = [] 
    for i in range(len(df)):
        l.append(euclidean_distance([row['x1'],row['x2'],row['x3'],row['x5']],[df.iloc[i]['x1'],df.iloc[i]['x2'],df.iloc[i]['x3'],df.iloc[i]['x5']])) 
    df['distance'] = l 
    f = df.sort_values(by = "distance") 
    d['Accepted'] = 0 
    d['Rejected'] = 0 
    for i in range(k):
        d[f.iloc[i]['status']]+=1 
    # df = df.drop('distance')
    return max(d,key = d.get) 

@api_view(['POST'])
def registerUser(request):
    user = request.data 
    serializer = UserSerializer(data = user) 
    if serializer.is_valid():
        serializer.save() 
    return Response("User created!!")


@api_view(['POST'])
def loginUser(request):
    user = request.data 
    if User.objects.filter(userName = user.get("userName")):
        valid_user = User.objects.get(userName = user.get("userName"))
        if valid_user and valid_user.passWord == user.get("passWord"):
            return Response({"userName" : user.get("userName"), "message":"Valid user"})
        else:
            return Response({"message":"Invalid user"})
    else:
        return Response({"message":"Invalid user"})

@api_view(['GET']) 
def getTicketData(request): 
    tickets = ticket.objects.all() 
    serializer = TicketSerializer(tickets,many = True) 
    return Response(serializer.data) 

@api_view(['POST']) 
def postRequest(request):
    userAction = request.data 
    conn = sqlite3.connect("D://USERS//Dell//Desktop//Web//React//Project//Server//DjangoServer//db.sqlite3")


    df_ticket = pd.read_sql_query("SELECT * FROM djangoRestApp_ticket", conn) 
    df_userHistory=pd.read_sql_query("SELECT * FROM djangoRestApp_userhistory", conn) 
    df_ticket.rename(columns = {"id":"ticket_id"}, inplace = True) 
    df = pd.merge(df_userHistory,df_ticket, on = "ticket_id", how = "left") 
    df = df[["text","userName_id","ticket_name","ticket_func","status","ticket_id"]]
    df.rename(columns = {"userName_id" : "userName"}, inplace = True) 
    nlp = spacy.load("en_core_web_lg") 
    cv = CountVectorizer() 
    l= []
    for i in range(len(df)):
        corpus = [df.iloc[i]['text'],df.iloc[i]['ticket_func']] 
        vector = cv.fit_transform(corpus)
        similarity_score = cosine_similarity(vector)[0][1]
        # print(similarity_score)
        l.append(similarity_score)
    df['x3'] = l 
    l = []
    for i in range(len(df)):
        l.append(len(df.iloc[i]['text']) / 300)
    df['x1'] = l

    m = [] 
    for i in range(len(df)):
        # print(df.iloc[i]['text'])
        m.append(equal(df.iloc[i]['userName'],df.iloc[i]['text']) and equal(df.iloc[i]['ticket_name'],df.iloc[i]['text']))
    df['x2'] = m 

    l = []
    for i in range(len(df)):
        t = sa.polarity_scores(df.iloc[i]['text']) 
        l.append(t['neg'])
    df['x4'] = l 

    l = []
    for i in range(len(df)):
        l.append(negativity(df.iloc[i]['text']))
    df['x5'] = l
    d = {"userName" : userAction.get("userName"), "ticket_name" : ticket.objects.get(id = userAction.get("ticket_id")).ticket_name, "text":userAction.get("text"), "ticket_func" : ticket.objects.get(id = userAction.get("ticket_id")).ticket_func}
    userAction['status'] = KNNClassifier(3,d,df) 
    serializer = storeUserHistorySerializer(data = userAction) 
    if serializer.is_valid(): 
        serializer.save()
        print("checking") 
        return Response({"message":"Data inserted"})
        
    else:
        print(userAction)
        return Response({"message":"Invalid data"})


@api_view(['GET']) 
def getUserInfo(request,username):
    userInfo = userHistory.objects.filter(userName = username)
    serializer = userHistorySerializer(userInfo,many = True) 
    return Response(serializer.data)

@api_view(['GET'])
def getTicketInfo(request,id):
    ticketInfo = ticket.objects.filter(id = id)
    serilizer = TicketSerializer(ticketInfo,many = True)
    return Response(serilizer.data)

