import React ,{useState}from 'react'
import Navbar from './Navbar'
import {useNavigate} from 'react-router-dom'

export default function FiAid() {
    const navigate=useNavigate();
    const [text,setText]=useState();
    const handleSubmit=(e)=>{
        e.preventDefault();
        const userName=localStorage.getItem("Username");
        const ticket=localStorage.getItem("id");
        const status="Rejected";
        
        const requestTicket={userName,ticket,text,status};
     
        fetch("http://localhost:8000/api/postRequest/",{
            method:'POST',
            headers : {"Content-Type":"application/json"},
            body:JSON.stringify(requestTicket)
        })
        .then(()=>{
            console.log("You Request submitted Successfully");
            localStorage.removeItem("id");
           navigate("/Home");
            
           
        })
         
    }
  return (
    <div>
      <Navbar />
<div className="create">
<h2>Request for financal aid</h2>   
<form onSubmit={handleSubmit} >
  
<div className="body">
<label >Why do you want this financial aid</label><br></br>
<textarea required value={text}

onChange={(e)=>{
    setText(e.target.value);

}}
 ></textarea></div>

{/* <p>{title}</p>
<p>{body}</p>
<p>{author}</p> */}
{  <button className="addbtn">Submit</button>}

</form>
</div>  
    </div>
  )
}
