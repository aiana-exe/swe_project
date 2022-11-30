/*import React,{useState,useEffect} from 'react'


const Doctors=() =>{
    let[doctors,setDoctors]=useState([])
    useEffect(()=>{
        getDoctors()
    },[])

    let getDoctors=async()=>{
        let response=await fetch('http://127.0.0.1:8000/patient/010811322325/appointment')
        let data=await response.json()
        setDoctors(data)
        console.log(doctors)
    }
    return doctors
}*/


//export default doctors

/*React.useEffect(() => {
    apiReq();
  }, []); 
  async function apiReq() {
    const url = 'http://127.0.0.1:8000/patient/010811322325/appointment';
    const res = await fetch(url);
    const doctors = await res.json();
    console.log(doctors)
  }*/

  export default [
    {
        id: 1,
        name: "Alibek",
        surname: "Zhantayev",
        specialization: "Dentistry",
        procedures: ["consultation", "tooth extraction", "cavity treatment", "braces"],
        available_time_slots: [ '2022-11-21 9:00:00','2022-11-21 10:00:00', '2022-11-21 11:00:00', '2022-11-21 12:00:00',
        '2020-11-23 9:00:00','2020-11-23 10:00:00', '2020-11-23 11:00:00', '2022-11-23 12:00:00',
        '2020-11-25 9:00:00','2020-11-25 10:00:00', '2020-11-25 11:00:00', '2022-11-25 12:00:00']
    },
    {
        id: 2,
        name: "Zhanna",
        surname: "Mukanova",
        specialization: "Dentistry",
        procedures: ["consultation", "cavity treatment"],
        available_time_slots: [ '2020-11-22 9:00:00','2020-11-22 10:00:00', '2020-11-22 11:00:00', '2020-11-22 12:00:00',
        '2020-11-24 9:00:00','2020-11-24 10:00:00', '2020-11-24 11:00:00', '2020-11-24 12:00:00']
    },
    {
        id: 3,
        name: "Qurmash",
        surname: "Kabenov",
        specialization: "Otorhinolaryngology",
        procedures: ["consultation", "earwax blockage removal", "nasal irrigation"],
        available_time_slots: [ '2020-11-21 14:00:00','2020-11-21 15:00:00', '2020-11-21 16:00:00', '2020-11-21 17:00:00',
        '2020-11-23 14:00:00','2020-11-23 15:00:00', '2020-11-23 16:00:00', '2020-11-23 17:00:00',
        '2020-11-25 14:00:00','2020-11-25 15:00:00', '2020-11-25 16:00:00', '2020-11-25 17:00:00']
    },
    {
        id: 4,
        name: "Kenzhibek",
        surname: "Zharassov",
        specialization: "Otorhinolaryngology",
        procedures: ["consultation"],
        available_time_slots: [ '2020-11-22 14:00:00','2020-11-22 15:00:00', '2020-11-22 16:00:00', '2020-11-22 17:00:00',
        '2020-11-24 14:00:00','2020-11-24 15:00:00', '2020-11-24 16:00:00', '2020-11-24 17:00:00']
    },
    {
        id: 5,
        name: "Dariya",
        surname: "Dalelqyzy",
        specialization: "Gynaecology",
        procedures: ["consultation", "mammography"],
        available_time_slots: [ '2020-11-22 9:00:00','2020-11-22 10:00:00', '2020-11-22 11:00:00', '2020-11-22 12:00:00',
        '2020-11-24 9:00:00','2020-11-24 10:00:00', '2020-11-24 11:00:00', '2020-11-24 12:00:00']
    },
    {
        id: 6,
        name: "Anastassiya",
        surname: "Berezhnaya",
        specialization: "Ophthalmology",
        procedures: ["consultation", "ophthalmoscopy", "perimetry test"],
        available_time_slots: [ '2020-11-21 9:00:00','2020-11-21 10:00:00', '2020-11-21 11:00:00', '2020-11-21 12:00:00',
        '2020-11-23 9:00:00','2020-11-23 10:00:00', '2020-11-23 11:00:00', '2020-11-23 12:00:00',
        '2020-11-25 9:00:00','2020-11-25 10:00:00', '2020-11-25 11:00:00', '2020-11-25 12:00:00']
    },
    {
        id: 7,
        name: "Pavel",
        surname: "Victor",
        specialization: "Dermatology",
        procedures: ["consultation", "cryotherapy"],
        available_time_slots: [ '2020-11-21 14:00:00','2020-11-21 15:00:00', '2020-11-21 16:00:00', '2020-11-21 17:00:00',
        '2020-11-23 14:00:00','2020-11-23 15:00:00', '2020-11-23 16:00:00', '2020-11-23 17:00:00',
        '2020-11-25 14:00:00','2020-11-25 15:00:00', '2020-11-25 16:00:00', '2020-11-25 17:00:00']
    },
    {
        id: 8,
        name: "Kenes",
        surname: "Kenessov",
        specialization: "Cardiology",
        procedures: ["consultation", "electrocardiography", "ultrasonography of the heart"],
        available_time_slots: [ '2020-11-22 12:00:00','2020-11-22 13:00:00', '2020-11-22 14:00:00', '2020-11-22 15:00:00',
        '2020-11-24 12:00:00','2020-11-24 13:00:00', '2020-11-24 14:00:00', '2020-11-24 15:00:00']
    },
    {
        id: 9,
        name: "Zhibek",
        surname: "Abulgazina",
        specialization: "Endocrinology",
        procedures: ["consultation", "ultrasonography of the thyroid"],
        available_time_slots: [ '2020-11-21 9:00:00','2020-11-21 10:00:00', '2020-11-21 11:00:00', '2020-11-21 12:00:00',
        '2020-11-23 9:00:00','2020-11-23 10:00:00', '2020-11-23 11:00:00', '2020-11-23 12:00:00']
    },
    {
        id: 10,
        name: "Daulet",
        surname: "Tarazov",
        specialization: "Gastroenterology",
        procedures: ["consultation", "ultrasonography of the abdomen"],
        available_time_slots: [ '2020-11-21 9:00:00','2020-11-21 10:00:00', '2020-11-21 11:00:00', '2020-11-21 12:00:00',
        '2020-11-23 9:00:00','2020-11-23 10:00:00', '2020-11-23 11:00:00', '2020-11-23 12:00:00']
    },
    {
        id: 11,
        name: "Maral",
        surname: "Janbolatqyzy",
        specialization: "Surgery",
        procedures: ["consultation", "x-ray", "suturing"],
        available_time_slots: [ '2020-11-21 9:00:00','2020-11-21 10:00:00', '2020-11-21 11:00:00', '2020-11-21 12:00:00',
        '2020-11-23 9:00:00','2020-11-23 10:00:00', '2020-11-23 11:00:00', '2020-11-23 12:00:00',
        '2020-11-25 9:00:00','2020-11-25 10:00:00', '2020-11-25 11:00:00', '2020-11-25 12:00:00']
    },
    {
        id: 11,
        name: "Akmaral",
        surname: "Janbolatqyzy",
        specialization: "Neuropathology",
        procedures: ["consultation", "MRI of the brain", "doppler ultrasonography of neck veins"],
        available_time_slots: [ '2020-11-22 14:00:00','2020-11-22 15:00:00', '2020-11-22 16:00:00', '2020-11-22 17:00:00',
        '2020-11-24 14:00:00','2020-11-24 15:00:00', '2020-11-24 16:00:00', '2020-11-24 17:00:00']
    }
]