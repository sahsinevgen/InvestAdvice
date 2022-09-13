import React, { useContext } from 'react';
import { useState } from 'react';
import { useReducer } from 'react';
import LogoutImg from './images/Logout.jpg'
import UserSettings from './UserSettings'
import { reducer } from './SignIn';
import { Context, ContextDispatch } from './Context';
import { getUserSettings, saveUserSettings, getAdvicesView } from './services/BackApi';
import { dataLoaded } from './SignIn';
import AdviceList from './AdviceList';

var currentId = { id: 0 };

function Login() {
    // if (localStorage.getItem('username') == null) {
    //     document.location.href = 'http://localhost:3000/';
    // }

    const [state, dispatch] = useReducer(reducer, {
        LoadedData: false,
    });

    const [advices, setAdvices] = useState([])
    const [userSettings, setUserSettings] = useState(new Map())

    if (state['LoadedData'] == false) {
        getAdvicesView({setAdvices, dispatch})
        getUserSettings({setUserSettings, dispatch})
        dispatch(dataLoaded())
    }

    function get_greeting() {
        if (localStorage.getItem('username') == null) {
            return 'You are not authorized';
        } else {
            return 'Hello, ' + localStorage.getItem('username');
        }
    }

    async function applyUserSettings(source, currency) {
        await saveUserSettings(source, currency, {setUserSettings, dispatch});
        await getAdvicesView({setAdvices, dispatch})
    }

    return (
        <div className='preview'>
            <nav className='navigate-bar'>       
                <a  href='/' > <div class="logo">
                    Investment advice
                </div></a>
                <div className='greetings'>
                    Welcome
                </div>
                <a  href='/' > <img src={LogoutImg} class="logout"/></a>
                <Context.Provider value={{applyUserSettings}}>
                    <AdviceList class='advice-list' advices={advices} />
                    <UserSettings class='user-settings' userSettings={userSettings}/>
                </Context.Provider>
            </nav>
        </div>)
}

export default Login;


