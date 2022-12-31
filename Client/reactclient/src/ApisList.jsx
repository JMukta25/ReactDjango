import React from 'react'
import Card from './Card'

export default function apisList({apis}) {
  return (
    <div className="ApisList">
        {apis.map((item)=>(
        <div className="blog-preview" key={item.id}>
             <Card  id={item.id}  title={item.ticket_name} image={item.ticket_image} desc={item.ticket_func}/>
    
        </div>
       ) )}
      
    </div>
  )
}
