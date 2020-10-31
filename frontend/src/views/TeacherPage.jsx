import { Container } from '@material-ui/core';
import React from 'react'

const TeacherPage = () => {
  return (
    <Container>
      Teachers Page
      Post New Task
      Title
      <input type="text" id="TitleInput">
      </input>
      Text of task
      <input type="text" id="SolutionTextInput">
      </input>
    </Container>
  );
}

export default TeacherPage;
