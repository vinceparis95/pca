import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App" style={{color:'magenta'}}>
    pca app - channel 2
    <p>from flask = {window.token}</p>
    <h1>enter details </h1> <br>
    first name <input type = "text" name= "fname" /> <br>
    last name <input type = "text" name = "lname" /> <br>
    <input type = "submit">

    </div>

  );
}

export default App;
