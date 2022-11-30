//import { getDefaultNormalizer } from '@testing-library/react'
//import React, {  useEffect } from 'react'
//import doctors from './doctors'
//import specializations from './specializations'
//import Fetch from './Fetch'
import React from 'react'

function App() {
  
  /*const [modal, setModal] = React.useState(false)
  const [slotDoc, setSlot] = React.useState(null)
  const [active, setActive] = React.useState(null)
  const [searchValue, SetValue] = React.useState('')
  //const[spec,setSpec]=React.useState([])*/
  const [docs, setDocs] = React.useState([]);
  const [spec,setSpec]=React.useState([])
    React.useEffect(()=> {
        getData()
      },[]);
    
    const getData=async () =>{
        const params = new URLSearchParams(window.location.pathname);
        const iin=params.get("iin_num")
        const doctorResponse=await fetch(`patient/${iin}/appointment`)
        //const x=`patient/${id}/appointment`
        const docs=await doctorResponse.json()
        console.log(docs['doctors'])
        console.log(docs['specialization'])
        setDocs(docs['doctors'])
        setSpec(docs['specialization'])
        //setSpec(data.get('specialization'))
        console.log(docs)
        //console.log(spec)
      }
    return(
      <div>
      {docs && docs.map(d=>
        <h1 key={d.iin_num}>{d.full_name}</h1>
            )}
            </div>
    )

  /*useEffect(()=> {
    getData()
  },[])

  const getData=async () =>{
    const doctorResponse=await fetch('http://127.0.0.1:8000/jai')
    const doctors=await doctorResponse.json()
    setDocs(doctors)
    console.log(doctors)
  }*/


  /*function filterSpec(specialization, index) {
    setActive(index)
    setDocs(docs.filter(doc => doc.department_id === specialization.department_id))
    //it finds the department id,not the name of a department itself
  }
  function filterSearch(event) {
    setDocs(docs.filter(doc => doc.full_name.includes(event.target.value)  || doc.department_id.includes(event.target.value) || doc.specialization_details_id.some(procedure => procedure.includes(event.target.value))))
  //think about procedures
  }
  function showAll() {
    setActive(null)
    setDocs(doctors)
  }
  function submitSlot(idxdoc, idxslot) {
    setModal(true)
    setSlot([idxdoc, idxslot])
  }
  function closeModal() {
    setModal(false)
    setSlot(null)
  }
  function acceptSlot() {
    setModal(false)
    setSlot(null)
  }
  return (
    <div className="wrapper">
      {
        modal == true 
        ?
        <div className='modal'>
          <div class='modal-inner'>
            <p>{docs[slotDoc[0]].full_name}</p>
            <p>{docs[slotDoc[0]].available_time_slots[slotDoc[1]]}</p>
            <div className="buttons">
              <div onClick={acceptSlot}>Accept</div>
              <div onClick={closeModal}>Reject</div>
            </div>
          </div>
        </div>
        :
        <div></div>
      }
      <input type='text' placeholder='Search' class='search' onChange={filterSearch}></input>
      <div className='specializations'>
        {spec.map((specialization, index) => {
          return (
          <div className='specialization' style={{background: active === index ? 'MediumVioletRed' : 'HotPink'}} onClick={() => filterSpec(specialization, index)}>{specialization}</div>
          )
        })}
      </div>
      <div className='showall' onClick={showAll}>Показать всех</div>
      <div className='doctors'>
        {docs.map((doctor, idxdoc) => {
          return (
            <div className='doctor'>
              <p className='name'>{doctor.name} {doctor.surname}</p>
              <div className='spec'>
                <p className='title'>Specialization:</p>
                <p>{doctor.specialization}</p></div>
              <div className='procedures'>
                <p class='title'>Procedures:</p>
                {doctor.procedures.map(procedure => {
                  return (
                    <div className='procedure'>{procedure}</div>
                  )
                })}
              </div>
              <p><strong>Availaibe Time Slots:</strong></p>
              <div className='slots'>
                {doctor.available_time_slots.map((slot, idxslot) => {
                  return (
                    <p onClick={() => submitSlot(idxdoc, idxslot)}>{slot}</p>
                  )
                })}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  );
  /*return (
    <><div>
      kk
    </div><Fetch /></>
  )*/
  
 //const[spec,setSpec]=React.useState([]);
 
    /*return (
        <div>
          <h1>hi</h1>
          <h1>hello</h1> 
          {docs && docs.map(d=>
            <h1>{d.full_name}</h1>
                )}
        </div>
    );*/

}



export default App;
