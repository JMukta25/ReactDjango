import {Link} from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheckSquare, faUser } from '@fortawesome/fontawesome-free-solid'
const Navbar=()=>{
 return (
    <div className="navbar">
        <h1 className="logo">API</h1>
        <div className="links">
            <span className="nav-item"> <Link to="/Home">Home</Link></span>
           <span className="nav-item"><Link to="/About">About</Link></span>
           <span className="nav-item-profile"><FontAwesomeIcon icon={faUser} /> <p>{localStorage.getItem("Username")}</p></span>
           
            
       </div>

    </div>

  );
}
export default Navbar;