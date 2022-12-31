
import './App.css';
import Create from './Create';
import Login from './Login';
import Home from './Home'
import FiAid from './FiAid';
import {BrowserRouter as Router,Route,Routes} from 'react-router-dom'


function App() {
  return (  
    <Router>
      <div className="App">
    <Routes>
    <Route  exact path="/" element={<Login />} />
    <Route path="/Create" element={<Create/>} />
    <Route path="/Home" element={<Home/>} />
    <Route path="/FiAid" element={<FiAid/>} />

  </Routes>
  </div>
  </Router>
   
  );
}

export default App;
