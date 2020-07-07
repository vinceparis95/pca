import React from 'react';
import './Login.css';

function Login() {
  return (
    <div className="App" style={{color:'chartreuse'}}>
    <form method="POST" action="">

    <h1 style={{letterSpacing:'4px'}}>input data:</h1> <br/>

<div className="superfield" style={{transform:'translateY(-36px)'}}>
    <div className="field">
        <div>first name</div>
        <input type = "text" name= "fname" style={{
          fontSize:"19px", borderStyle:"solid",
          borderRadius:"9px", borderWidth:"5px",
          borderColor:"#FF00FF45", opacity:"60%",
        outline:"none"}} /> <br/>
    </div>

    <div className="field">
        <div>last name</div>
        <input type = "text" name = "lname" style={{
          fontSize:"19px", borderStyle:"solid",
          borderRadius:"9px", borderWidth:"5px",
          borderColor:"#FF00FF45", opacity:"60%",
        outline:"none"}} /> <br/>
    </div>

    <input type = "submit"/>
    </div>

    </form>
    </div>
  );
}

export default Login;
