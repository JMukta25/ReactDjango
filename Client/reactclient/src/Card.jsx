
import React from "react";
import { useNavigate } from "react-router-dom";

function Card(props) {
 
  const navigate=useNavigate();
  const handleClick=(id)=>{ 
    localStorage.setItem("id",id);
   navigate("/FiAid");
  }
  return (
    <div className="note">
      <h1>{props.title}</h1>
      <img  width="50px" height="50px"src={props.image} alt="api logo" ></img>
      <p>{props.desc}</p>
      <button onClick={()=>{
        handleClick(props.id)
      }}>Add</button>
     
    </div>
  );
}

export default Card;
