
import React from "react";


function HistoryBlock(props) {
 console.log("HistoryBlock"+props);
  console.log(props.id);
  return (
    <div className="note">
      <h1>{props.text}</h1>
      <h2>{props.status}</h2>
      <p>{props.id}</p>
     
     
    </div>
  );
}

export default HistoryBlock;