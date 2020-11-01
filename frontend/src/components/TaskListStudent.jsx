import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

import { useState } from 'react';
import { useEffect } from 'react';

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
    position: 'fixed',
    margin: '16px'
  },
}));

function ListItemLink(props) {
  return <ListItem button component="a" {...props} />;
}

export default function SimpleList() {
  const classes = useStyles();
  const [tasks, setTasks] = useState([]);
  async function loadTasks(){
    fetch(`http://localhost:8000/tasks/`,{
        method: 'GET',
      })
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json()).then(res=>{ setTasks(res.tasks); console.log(tasks,'sas')})
  }
  useEffect(()=>{loadTasks()},[])
  return (
    <div className={classes.root}>
      <List component="nav" aria-label="main mailbox folders">
        {tasks.map(task=>{
          const url = task.title.toLowerCase().replace(' ','')
          return (
          <ListItemLink href={`/student-page/${url}`}>
            <ListItemText primary={task.title}  />
          </ListItemLink>)
        }
          )}
        
      </List>
      
      
    </div>
  );
}