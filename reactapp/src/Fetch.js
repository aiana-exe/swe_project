import React from "react";


function FetchApi(){
const[docs,setDocs]=React.useState([])
React.useEffect(()=> {
    getData()
  },[])

  const getData=async () =>{
    const doctorResponse=await fetch('http://127.0.0.1:8000/patient/0108113223225/appointment')
    const docs=await doctorResponse.json()
    setDocs(docs)
    console.log(docs)
  }
  return (
    <div>
        {docs && docs.map(d=>
        <h1>{d.full_name}</h1>
            )}
    </div>
)
}



export default fetch