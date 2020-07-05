import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App" style={{color:'chartreuse'}}>
    pca app - channel 3
    <p>from flask = {window.token}</p>
    <form method="POST" action="">

    <h1 style={{letterSpacing:'4px'}}>data:</h1> <br/>

    <div className="field">
        <div>first name</div>
        <input type = "text" name= "fname" /> <br/>
    </div>

    <div className="field">
        <div>last name</div>
        <input type = "text" name = "lname" /> <br/>
    </div>

    <div className="field">
        <div>age</div>
        <input type = "int" name = "age" /> <br/>
    </div>

    <div className="field">
        <div>book</div>
        <input type = "int" name = "book" /> <br/>
    </div>

    <input type = "submit"/>

    </form>
    </div>
  );
}

export default App;
