import './App.css';
import * as React from 'react'
import { Link, BrowserRouter as Router, Route } from 'react-router-dom';
import IndexPage from './views/IndexPage'
import StudentPage from './views/StudentPage'
import TeacherPage from './views/TeacherPage'
import LoginForm from './views/LoginForm'
// import NavigationPanel from './components/NavigationPanel'
import AppBar from '@material-ui/core/AppBar';
import {Toolbar, Button} from '@material-ui/core/';
import {createMuiTheme} from '@material-ui/core/styles'
import {ThemeProvider} from '@material-ui/core'
const theme = createMuiTheme({
  overrides: {
    // Style sheet name ⚛️
    MuiButton: {
      root: {
        background: "linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%) !important",
        border: 0,
        borderRadius: 3,
        boxShadow: "0 3px 5px 2px rgba(255, 105, 135, .3)",
        color: "white",
        height: 48,
        padding: "0 30px",
        margin: "0 0 0 10px",
      },
    },
  },
});
function App() {
  return (
    <section className="App">
      <Router>        
        <AppBar position="static">
          <Toolbar>
            <ThemeProvider theme={theme}>
            <Button href='/about'>
              Home       
            </Button>
            <Button href='/teacher-page'>
              Teacher page
            </Button>
            <Button href='/student-page'>
              Student Page
            </Button>
            <Button href='/login'>
              Login
            </Button>
            </ThemeProvider> 
          </Toolbar>
        </AppBar>
          
       
       <Route path="/about">
         <IndexPage></IndexPage>
       </Route>
       <Route path="/teacher-page"><TeacherPage></TeacherPage></Route>
       <Route path="/student-page"><StudentPage></StudentPage></Route>        
       <Route path="/login"><LoginForm></LoginForm></Route>      
      </Router>  
    </section>
  );
}

export default App;
