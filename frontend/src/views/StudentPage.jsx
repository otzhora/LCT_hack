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
  function submitCode(){

  }
  useEffect(()=>{editorRef.current.editor.resize()},[])
  return (
    <React.Fragment>
      <TaskListStudent></TaskListStudent>
      <Container >
        
        <div display="flex">
          
          <TaskStatement></TaskStatement>
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
        <Button onClick={submitCode}> Submit Code</Button>
      </Container>
    </React.Fragment>
  );
}

export default StudentPage;
