import React, { useContext } from 'react';

import './style/user-settings.css'
import { Context } from './Context';


function UserSettings({userSettings}) {
    const {applyUserSettings} = useContext(Context)

    async function _applyUserSettings() {
        const source = document.getElementById('source-input').value.toString();
        const currency = document.getElementById('currency-input').value.toString().toUpperCase();
        await applyUserSettings(source, currency);
        document.getElementById('source-input').value = source
        document.getElementById('currency-input').value = currency
    }

    return (
        <div className='settings' id="login_icon">
            <div className='form-out'> 
                <div className='welcome-text'>
                    Settings
                </div>
                <div className='form-in'> 
                    <div className='currency-text'>
                        Enter a currency or leave the field blank 
                        to receive advice for all currencies.
                    </div>
                    <input className='currency-input' placeholder='All currencies' id='currency-input' defaultValue={userSettings['currency']} /> 
                    <div className='source-text'>
                        Choose source of our advices.
                    </div>
                    <select className='source-input' id='source-input' defaultValue={userSettings['source'] + ""}>
                        <option value="both">From all sources</option>
                        <option value="tg_channels">From telegram channels</option>
                        <option value="prediction">From our predictions</option>
                    </select>                    
                    <button className='apply-button' onClick={() => _applyUserSettings()}>
                        <div className='apply-button-text'>Apply</div>
                    </button>
                </div>
            </div> 
        </div>
    )
}

export default UserSettings;