import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App" style={{color:'magenta'}}>
    pca app - channel 2
    <p>from flask = {window.token}</p>
    <form method="POST" action="">
    <center>
    <h1>enter deets </h1> <br/>
    First Name <input type = "text" name= "fname" /> <br/>
    Last Name <input type = "text" name = "lname" /> <br/>
    <input type = "submit"/>
    </center>
    </form>
    </div>
  );
}

export default App;
