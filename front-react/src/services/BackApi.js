import { useContext } from "react";
import { loginSucceed, loginFailed, refreshFailed, dataLoaded, nonAuthorized } from "../SignIn"

const baseUrl = 'http://127.0.0.1:8000/api/'

export async function saveUserSettings(source, currency, {setUserSettings, dispatch}) {
    await refreshTokensView({dispatch})
    await fetch(baseUrl + 'user/settings/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json', 
            'Authorization': 'JWT ' + localStorage.getItem('access')
        },
        body: JSON.stringify({
            source: source,
            currency: currency
        })
    })
    .then(await getUserSettings({setUserSettings, dispatch}))
}

export async function getUserSettings({setUserSettings, dispatch}) {
    await refreshTokensView({dispatch})
    await fetch(baseUrl + 'user/settings/', {
        method: 'GET',
        headers: {
            'Content-type': 'application/json;charset=utf-8', 
            'Authorization': 'JWT ' + localStorage.getItem('access')
        }
    })
    .then(data=>data.json())
    .then(data=>setUserSettings(data))
}

export async function getAdvicesView({setAdvices, dispatch}) {
    await refreshTokensView({dispatch})
    await fetch(baseUrl + 'advices/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json', 
            'Authorization': 'JWT ' + localStorage.getItem('access')
        },
        body: JSON.stringify({
            count: 8
        })
    })
    .then(data=>data.json())
    .then(data=>setAdvices(data))
}

export async function getTokensView(username, password, {dispatch}) {
    await fetch(baseUrl + 'token/obtain/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
        })
    }).then((response)=>{ 
        console.log(response);
        if (!response.ok) {
            throw 'bad response';
        }
        return response.json()
    })
    .then((data)=> {
        console.log(data)
        localStorage.setItem('refresh', data['refresh'])
        localStorage.setItem('access', data['access'])
        // localStorage.setItem('username', data['user']['username'])
        console.log(localStorage.getItem('refresh'))
        console.log(localStorage.getItem('access'))
        dispatch(loginSucceed())
        console.log("getTokensView fault")
    }).catch(e=>{
        dispatch(loginFailed());
        console.log(e)
    })
}


export async function refreshTokensView({dispatch}) {
    await fetch(baseUrl + 'token/refresh/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            refresh: localStorage.getItem('refresh'),
        })
    }).then((response)=>{ 
        console.log(response);
        if (!response.ok) {
            throw 'bad response';
        }
        return response.json()
    })
    .then((data)=> {
        console.log(data)
        localStorage.setItem('refresh', data['refresh'])
        localStorage.setItem('access', data['access'])
        console.log(localStorage.getItem('refresh'))
        console.log(localStorage.getItem('access'))
    }
    ).catch(e=> {
        dispatch(nonAuthorized());
        console.log(e)
    })
}

export async function createUserView(username, password, {dispatch}) {
    await fetch(baseUrl + 'user/create/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then((response)=>{ 
        console.log(response);
        if (!response.ok) {
            throw 'bad response';
        }
        return response.json()['data']
    })
}