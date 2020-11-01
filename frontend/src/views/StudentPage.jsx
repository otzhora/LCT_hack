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
import {getNameFromPath} from '../helpers'

const solution = {text:""}
const solutionFile = {text:""}
function StudentPage(props){
  const editorRef = useRef(null)
  const [result, setResult] = useState(null)
  const loadResult = async (name) =>
      fetch(`http://localhost:8000/task/${name}/`,{
        method: 'POST',
        headers: {
          'Content-Type': 'raw'
        },
        body: JSON.stringify({
            username: 'lol',
            text: solution.text,
            lang: 'Python'
          })
      })
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json()).then(res=>{setResult(res)})
  function submitCode(){
      solution.text = editorRef.current.editor.getValue()
      console.log(solution.text)
      loadResult(url) 
  }
  function submitCodeFromFile(){
    if (solutionFile.text){
      solution.text = solutionFile.text
      console.log(solutionFile.text, 'solution')
      loadResult(url)
    }
    else console.log('empty file')
  }
  function onFileLoaded(text){
    console.log(text, 'filereaded')
    solutionFile.text = text
  }
  function handlePep(tests){
      if(tests[0].style_result) return <div>{tests[0].style_result}</div>
      else return null
    
  }
  function handleResult(result){
    if(result){
      const successfulTests = result.filter((res)=>res.check) 
      const failTests = result.filter((res)=>!res.check)
      console.log(failTests)
      const percentage = successfulTests.length / result.length;
      return percentage===1 
      ? <div>SUCCESS 100%{handlePep(successfulTests)}</div> 
    : <div>FAIL {percentage}{handlePep(failTests)}</div>
    }
    else return null
  }
  const url = window.location.href.replace('http://localhost:3000/student-page/','');
  
  useEffect(()=>{editorRef.current.editor.resize()},[])
  
  return (
    <React.Fragment>
      <TaskListStudent></TaskListStudent>
      <Container >
        
        <div display="flex">
          
          <TaskStatement name={url}></TaskStatement>
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
        <Button onClick={submitCode}> Submit Code From Editor</Button>
        <ReadFromFile onFileLoaded={onFileLoaded}></ReadFromFile>
        <Button onClick={submitCodeFromFile}> Submit Code From File</Button>
        
        <div>Your Score is
        {handleResult(result)}
        </div>
      </Container>
    </React.Fragment>
  );
}

export default StudentPage;
