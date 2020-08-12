import React from 'react';
import './Navbar.css';
import { Navbar } from 'react-bootstrap';
import { withRouter } from 'react-router-dom';

const Navigation = (props) => {
    console.log(props);
    return (
      <div>

        <Navbar className='root' style={{backgroundColor:'rgba(145, 255, 0,0.79)', opacity:'49%',
                      fontFamily:'Djakarta', letterSpacing:'4px', fontSize:'19px', width:'145px',
                      margin:'9px', borderRadius:'14px', padding:'9px',fontWeight:'bold',
                      color:'white',textDecoration: 'none'}}>
          <Navbar.Brand style={{fontSize:'25px', color:'rgb(143, 0, 145)',textDecoration: 'none'}}
          href="/login">
          PCA Intake </Navbar.Brand>
        </Navbar>

      </div>
    )
}

export default withRouter(Navigation);
