import { useState} from "react";
import {Link,useNavigate } from 'react-router-dom'


const Login=()=>{
const [userName,setUserName]=useState("");   
const [passWord,setPassWord]=useState("");   
const navigate = useNavigate();


 const handleSubmit=(e)=>{
   e.preventDefault();
   const user={userName,passWord};

   fetch("http://localhost:8000/api/loginUser/",{
       method:'POST',
       headers : {"Content-Type":"application/json"},
       body:JSON.stringify(user)
   })
   .then((response) => response.json())
   .then((data) => {
      console.log(data.userName);
      if(data.message==="Valid user"){
         localStorage.setItem("Username",data.userName);
         navigate("/Home");
      }else{
         localStorage.setItem("Username","");
         navigate("/Login");
      }
      
      

   });
    
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
<Link to="/Create"><h3>Create Account</h3></Link>
        



</form>
</div>  

)

}
export default Login;