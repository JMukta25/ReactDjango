import React from 'react'
import { useEffect } from 'react';
import useData from './useData' 
import UseHistoryList from './UseHistoryList'



 

  
 


export default function Profile() {
      const name= localStorage.getItem("Username")
  
      const {data:history,ispending,error}=useData("http://localhost:8000/api/userInfo/"+name);


    
  return (
    <div>
            {history && <UseHistoryList history={history} />}
     
    </div>
  )
  }
