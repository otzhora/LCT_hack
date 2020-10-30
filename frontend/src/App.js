import './App.css';
import { Link, BrowserRouter as Router, Route , Switch} from 'react-router-dom';
import IndexPage from './views/IndexPage'
import StudentPage from './views/StudentPage'
import TeacherPage from './views/TeacherPage'
import LoginForm from './views/LoginForm'
function App() {
  return (
    <section className="App">
      <Router>        
       <Link to="/about">Home</Link>        
       <Link to="/teacher-page">Teacher page</Link>
       <Link to="/student-page">Student Page</Link>
       <Link to="/login">Login</Link>    
       
       <Route path="/about">
         <IndexPage></IndexPage>
       </Route>
       <Route path="/teacher-page"><TeacherPage></TeacherPage></Route>
       <Route path="/student-page" render={StudentPage} />        
       <Route path="/login" render={LoginForm} />      
      </Router>  
    </section>
  );
}

export default App;
