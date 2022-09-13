import React from 'react';
import ExitImg from './images/Exit.png'
import LoginImg from './images/Login.jpg'
import EyeImg from './images/Eye.png'
import EyeCrossImg from './images/EyeCross.png'
import { createUserView, getTokensView } from './services/BackApi';
import { reducer } from  './SignIn'
import { useReducer } from 'react'



import $ from 'jquery'
import './style/login.css'
import './style/preview.css'


function Preview() {
    localStorage.clear();

    const [state, dispatch] = useReducer(reducer, {
        Authorized: false,
    });
      
    function open_login_icon(id_popap) {
        $("#login_icon").addClass('active');
    }

    function close_login_icon(id_popap) {
        $("#login_icon").removeClass('active');
    }

    async function getTokens(username, password) {
        await getTokensView(username, password, {dispatch})
    }

    async function signIn() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        await getTokens(username, password);
        if (state['Authorized'] == true) {
            document.location.href += 'login';
        }
    }
      
    async function register() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        await createUserView(username, password, {dispatch});
        await getTokens(username, password);
        if (state['Authorized'] == true) {
            document.location.href += 'login';
        }
    } 

    function showPassword() {
        const element = document.getElementById('password');
        if (element.type == 'password') {
            element.type = 'text'
        }
        else {
            element.type = 'password';
        }
    }

    return (
        <div className='preview'>
            <nav className='navigate-bar'>       
                <a  href='/'><div className='logo'>
                    Investment advice
                </div></a>
                <button  onClick={open_login_icon} className='exit-btn'> <img src={LoginImg} class="login"/></button>
            </nav>
            <div class='text-item-up'>
                <div className='text-up'>
                    We also try to give advice ourselves by predict the stock market.
                </div>
            </div>
            <div className='text-frame-down'>
                <div className='text-down'>
                    Don't want to look for investment advice on telegram channels?<br/>
                    We will collect them for you.
                </div>
            </div>
            <div className='blur' id="login_icon"> 
                <div className='form-out'> 
                    <button class="exit-btn" onClick={close_login_icon}><img src={ExitImg} class="exit"/></button>
                    <div className='form-welcome'>
                        <div className='welcome-text'>
                        Welcome!</div> 
                    </div>
                    <div className='form-in'> 
                        <div className='intro-text'>Introduce yourself</div>
                        <input className='username' placeholder='Username' id='username'></input> 
                        <input className='password' placeholder='Password' type="password" id="password"/>
                        <button onClick={showPassword} class='eye'><img src={EyeImg} class='eye-img' id='eye'/></button>
                        <button className='sign-in' onClick={signIn}>
                            <div className='sign-in-text'>Sign in</div>
                        </button>
                        <button className='register' onClick={register}> 
                            <div className='register-text'>Register</div>
                        </button>
                    </div>
                </div> 
            </div> 
        </div>
    )
}

export default Preview;