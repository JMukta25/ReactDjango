import {useEffect,useState} from 'react';

const useData =(url)=>{
 
  // const [name,setName]=useState("Abhir");
   const [data,setData]=useState(null);
   const [ispending,setisPending]=useState(true);
   const [error,setError]=useState(null);
   useEffect(()=>{
    
       setTimeout(()=>{
      fetch(url)
      .then((res)=>{
       if(!res.ok){
            throw Error("could not load message");
       }
           return res.json();
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
   },[url]);
   return {data,ispending,error}

}
export default useData;