import React from 'react';
import './Login.css';

function Login() {
  return (
    <div className="App" style={{color:'chartreuse'}}>
    <form method="POST" action="">

    <div style={{fontSize:"19px",letterSpacing:'4px'}}>input data:</div> <br/>

<div className="superfield" style={{transform:'translateY(-9px)'}}>
    <div className="field">
        <div>first name</div>
        <input type = "text" name= "fname" style={{
          fontSize:"19px", borderStyle:"solid",
          borderRadius:"9px", borderWidth:"5px",
          borderColor:"#FF00FF09", opacity:"60%",
        outline:"none"}} /> <br/>
    </div>

    <div className="field">
        <div>last name</div>
        <input type = "text" name = "lname" style={{
          fontSize:"19px", borderStyle:"solid",
          borderRadius:"9px", borderWidth:"5px",
          borderColor:"#FF00FF09", opacity:"60%",
        outline:"none"}} /> <br/>
    </div>

    <input type = "submit"/>
    </div>

    </form>
    </div>
  );
}

export default Login;
