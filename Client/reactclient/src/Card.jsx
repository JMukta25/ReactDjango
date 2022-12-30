
import React from "react";

function Card(props) {
  return (
    <div className="note">
      <h1>{props.title}</h1>
      <img  width="50px" height="50px"src={props.image} alt="api logo" ></img>
      <p>{props.desc}</p>
      <button>Add</button>
     
    </div>
  );
}

export default Card;
