import React from 'react';
import AdviceItem from './AdviceItem';

import './style/advice-list.css'

function AdviceList({advices}) {
    return (
        <div className='container' id='note-list'>
            <div className='list'>
                {advices.map(advice=><AdviceItem key={advice.id} advice={advice} />)}
                {/* {<NewItem />} */}
            </div>
        </div>
    )
}

export default AdviceList;