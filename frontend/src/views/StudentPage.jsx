import React from 'react'
import { useEffect } from 'react'
import AceEditor from 'react-ace'
import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-monokai";
import {makeStyles} from '@material-ui/core/styles'
import './StudentPage.css';
import {useRef} from 'react';
import TaskListStudent from '../components/TaskListStudent'
import TaskStatement from '../components/TaskStatement'
import {Button, Container} from '@material-ui/core'
import ReadFromFile from '../components/ReadFromFile';
import { useState } from 'react';
import Async from 'react-async';
// const classes = makeStyles((theme) => ({
//   root: {
//     flexGrow: 1,
//   },
//   paper: {
//     padding: theme.spacing(2),
//     textAlign: 'center',
//     color: theme.palette.text.secondary,
//   },
// }));

function StudentPage(){
  const editorRef = useRef(null)
  const [solutionText, setSolutionText] = useState('')
  const [result, setResult] = useState(null)
  const loadResult = async (name) =>
      fetch(`http://localhost:8000/task/${name}/`,{
        method: 'POST',
        headers: {
          'Content-Type': 'raw'
        },
        body: JSON.stringify({
            username: 'otzhora',
            text: solutionText,
            lang: 'Python'
          })
      })
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json()).then(res=>{setResult(res)})
  function submitCode(){
    if (solutionText){
      loadResult('sum')
    }
    else {
      setSolutionText(editorRef.current.text)
      loadResult('sum')
    }
  }
  function onFileLoaded(text){
    setSolutionText(text)
  }
  function handleResult(result){
    if(result){
      const successfulTest = result.map((res)=>{
        if (res.check) return res;
      }) 
      const percentage = successfulTest.length / result.length;
      return percentage===1 
      ? <div>SUCCESS 100%</div> 
      : <div>FAIL {percentage}</div>
    }
    else return null
  }
  
  
  useEffect(()=>{editorRef.current.editor.resize()},[])
  return (
    <React.Fragment>
      <TaskListStudent></TaskListStudent>
      <Container >
        
        <div display="flex">
          
          <TaskStatement name='sum'></TaskStatement>
        </div>
        
        <div id="editor">
            <AceEditor
              mode='python'
              theme='monokai'  
              fontSize={24}
              ref={editorRef}
              width={'100%'}
              height={'700px'}
            />
        </div>
        <ReadFromFile onFileLoaded={onFileLoaded}></ReadFromFile>
        <Button onClick={submitCode}> Submit Code</Button>
        <div>Your Score is
        {handleResult(result)}
        </div>
      </Container>
    </React.Fragment>
  );
}

export default StudentPage;
