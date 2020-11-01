import { Container, Button, Paper } from '@material-ui/core';
import React from 'react'
import { useEffect ,useState} from 'react';
import Async from 'react-async';
import {getNameFromPath} from '../helpers'
let tasks = []
const students = [
  'otzhora',
  'lol'
]

const TeacherPage = (props) => {
  const [studentResults, setStudentResults] = useState([])
  async function getResult(stud, task){
    fetch(`http://localhost:8000/results/${stud}/${task}/`,{
        method: 'GET',
      })
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json()).then(res=>{setStudentResults([...studentResults, {  
          student: stud,
          task: task,
          results: res
        
        }])}).then(()=>{console.log('works')})
    
  }
  function getAllResults(studArr, taskArr){
    studArr.forEach(stud => {
      tasks.forEach(task=>{
        getResult(stud, getNameFromPath(task.path));
      });
    });
  }
  const renderList = () => {
    if(studentResults.length){
      return <ul>{studentResults.map(res=>(
        <li>{res.student}|{res.task}|{res.results.pop()}</li>
    ))}</ul>
    }
    else return null
  }
  useEffect(()=>{
    fetch(`http://localhost:8000/tasks/`,{
      method: 'GET',
    })
    .then(res => (res.ok ? res : Promise.reject(res)))
    .then(res => res.json()).then(res=>{tasks = res.tasks; console.log(tasks, 'tasks')})
    .then(()=>{getAllResults(students,tasks)})
    .then(console.log(studentResults, 'sas'))
  },[])
  return (
    <div>
      {renderList()}
    </div>
  );
}
//content type form data multi-part from data

export default TeacherPage;
