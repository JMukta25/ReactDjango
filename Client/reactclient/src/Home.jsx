import React from 'react'
import Navbar from './Navbar';
import Card from './Card'
import useData from './useData'
import ApisList from './ApisList'
;
export default function Home() {
    console.log("In Home");
   
    const {data:apis,ispending,error}=useData("http://localhost:8000/api/getTicketData");
    
  return (
    
    <div>
      <Navbar />
      {apis && <ApisList apis={apis} />}
     
     
    </div>
  )
}
