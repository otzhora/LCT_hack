import { Container, Button, Paper } from '@material-ui/core';
import React from 'react'
import { useState } from 'react';
import AttachZip from '../components/AttachZip';
import ResultTable from '../components/ResultTable';

const zipArchive = {value: {}}
const teacher = 'Petrovich'
const TeacherPage = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  function onZipLoaded(file){
    zipArchive.value = file
  }
  async function postTask(){
    let formData = new FormData();
    console.log(title)
    formData.append('data', zipArchive.value, 'Sample.zip')
    formData.append('url', title.target.value)
    formData.append('title', title.target.value)
    formData.append('description', description.target.value)
    formData.append('teacher', teacher)
    fetch('http://localhost:8000/new_task/',{
      method: 'POST',
      body: formData
    })
    .then((res)=>((res.ok ? res : Promise.reject(res))))
    .then((res)=>{console.log(res); return res.json()})
  }
  return (
    <Container>
      Teachers Page
      <Paper className={'createNewTask'}>
        Post New Task
        <div>
        Title
        <input type="text" id="TitleInput" 
          value={title.value} 
          onChange={setTitle}>
        </input>
        </div>
        <div>
        Text of task
        <input type="text" id="DescriptionInput" 
          value={description.value} 
          onChange={setDescription}>
        </input>
        </div>
        <input type='file' id='file' accept='.zip' 
        onChange={e=>{zipArchive.value = e.target.files[0]}}/>
        <Button onClick={postTask}>Post Task</Button>
      </Paper>
      <Paper className={'createNewTask'}>
        <ResultTable></ResultTable>
      </Paper>
      
    </Container>
  );
}
//content type form data multi-part from data

export default TeacherPage;
  