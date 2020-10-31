import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import InboxIcon from '@material-ui/icons/Inbox';
import DraftsIcon from '@material-ui/icons/Drafts';
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
const tasks1 = [
  {id: 1, name: 'First Task'},
  {id: 2, name: 'Second Task'}  
]

export default function SimpleList() {
  const classes = useStyles();
  const [tasks, setTasks] = useState({tasks:[]});
  async function loadTasks(){
    fetch(`http://localhost:8000/tasks/`,{
        method: 'GET',
      })
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json()).then(res=>{ setTasks(res); console.log(tasks,'sas')})
  }
  useEffect(()=>{loadTasks()},[])
  return (
    <div className={classes.root}>
      <List component="nav" aria-label="main mailbox folders">
        {tasks.tasks.map(task=>(<ListItem button>
          <ListItemText primary={task.title}  />
        </ListItem>))}
        
      </List>
      
      
    </div>
  );
}