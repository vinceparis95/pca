import React from 'react';
import './App.css';
import Navigation from './components/Navbar';
import Routes from './Routes';
function App() {
  return (
    <div className="Bod" style={{color:'chartreuse'}}>
    <Navigation />
    <Routes />
    </div>
  );
}

export default App;
