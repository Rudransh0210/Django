import React, { useState } from 'react';
import tryLogin from '../../services/django/login';
import { useNavigate } from 'react-router-dom';
import { getBlogs } from '../../services/django/getblogs';
var sha256 = require('js-sha256');

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    return (
        <div className='login-page'>
            <div className='email'>
                UserName:
                <input type="text" onChange={(event)=>{setUsername(event.target.value)}} id="login-username">
                </input>
            </div>
            <div className='password'>
                Password:
                <input type="password" onChange={(event)=>{setPassword(event.target.value)}} id="login-password">
                </input>
            </div>
            <button onClick={async()=>{
                const hashedPassword = sha256.create();
                hashedPassword.update(password);
                const status = await tryLogin(username, hashedPassword.hex());
                if (status) {
                    alert("Welcome darling");
                    await getBlogs();
                    document.cookie=`username=${username};secure`;
                    document.cookie=`password=${hashedPassword.hex()};secure`;
                    navigate('/main');
                }
                else {
                    {alert("Invalid Credentials")}
                }
            }}>Login</button>
        </div>
    )
}

export default LoginPage;