import React from 'react';
import './App.css';
import Navigation from './components/Navbar';
import Routes from './Routes';
function App() {
  return (
    <div className="App" style={{color:'chartreuse'}}>
    pca app - channel 3
    <p>from flask = {window.token}</p>
    <Navigation />
    <Routes />
    </div>
  );
}

export default App;
