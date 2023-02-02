import {useEffect,useState} from 'react';

const useData =(url)=>{
 console.log("url "+url);
  // const [name,setName]=useState("Abhir");
   const [data,setData]=useState(null);
   const [ispending,setisPending]=useState(true);
   const [error,setError]=useState(null);
  
      console.log("Inside ");
      useEffect(()=>{
         setTimeout(()=>{
            fetch(url)
            .then((res)=>{
              console.log("Inside Then"); 
             if(!res.ok){
                console.log(error);
                  throw Error("could not load message");
             }else{
               console.log("res"+res);
               return res.json();
             }
                 
            })
            .then(data =>{
             console.log("data");
             console.log(data);
             setData(data);
             setisPending(false);
             setError(null);
            })
            .catch((err)=>{
             setisPending(false);
             setError("Could not load")
             
               //console.log(err.message);
            })},1000)

      },[url])
       
   
   return {data,ispending,error}

}
export default useData;