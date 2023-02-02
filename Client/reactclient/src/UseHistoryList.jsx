import React ,{useState}from 'react'
import HistoryBlock from './HistoryBlock'

async function getData(id) {
  try {
    const response = await GetName(id);
    console.log(response);
  } catch (err) {
    console.log(err);
  }
}
function GetName(id){
  

  fetch("http://localhost:8000/api/getTicketInfo/"+id+"/")

  .then( (res) => {
    console.log("Inside Then"); 
    if (!res.ok) {
        console.log("This is error in getName");
        throw Error("could not load message");
    } else {
        console.log("res"+res);
        return  res.json(); 
    }
})
  .then(data =>{
   console.log("data");
   console.log(data[0].ticket_name);
   return data[0].ticket_name;
   
  
  })
  .catch((err)=>{

    
   console.log("Could not load")}
  )
  
 }
   
export default function UseHistoryList({history}) {

  
   console.log("hist"+{history});
   console.log("getData"+getData(1)[0]);
   
    

  return (
    <div className="useHistory">
      
        {history.map((item)=>{
      
       
       return(
        <HistoryBlock key={item.id} text={item.text}  status={item.status} id={item.ticket_name} />
        
       
      );   
       
         }  )}
      
    </div>
  )
}
