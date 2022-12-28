import { useState } from "react";

const Create=()=>{
const [userName,setUserName]=useState("");   
const [passWord,setPassWord]=useState("");   



 const handleSubmit=(e)=>{
   e.preventDefault();
   const user={userName,passWord};

   fetch("http://localhost:8000/api/registerUser/",{
       method:'POST',
       headers : {"Content-Type":"application/json"},
       body:JSON.stringify(user)
   })
   .then(()=>{
       console.log("new user added");
       
      
   })
    
}
   return(
<div className="create">
<h2>User Registration </h2>   
<form onSubmit={handleSubmit}>
   <div className="title">
<label>Username</label><br></br>
<input  type="text"
required value={userName}
 onChange={(e)=>{
   setUserName(e.target.value)}}></input>
   </div>
   <div className="title">
<label>Password</label><br></br>
<input  type="password"
required value={passWord}
 onChange={(e)=>{
   setPassWord(e.target.value)}}></input>
   </div>


{/* <p>{title}</p>
<p>{body}</p>
<p>{author}</p> */}
{  <button className="addbtn">Submit</button>}

</form>
</div>  

)

}
export default Create;