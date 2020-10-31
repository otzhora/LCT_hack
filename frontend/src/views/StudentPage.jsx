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

const solution = {text:""}
function StudentPage(){
  const editorRef = useRef(null)
  const [solutionFile, setSolutionFile] = useState('')
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
      loadResult('sum') 
  }
  function submitCodeFromFile(){
    if (solutionFile){
      solution.text = solutionFile
      console.log(solution.text)
      loadResult('sum')
    }
  }
  function onFileLoaded(text){
    setSolutionFile(text)
  }
  function handleResult(result){
    if(result){
      const successfulTests = result.filter((res)=>res.check) 
      const failTests = result.filter((res)=>!res.check)
      console.log(failTests)
      const percentage = successfulTests.length / result.length;
      return percentage===1 
      ? <div>SUCCESS 100%</div> 
    : <div>FAIL {percentage}{failTests[0].styleResult}</div>
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
