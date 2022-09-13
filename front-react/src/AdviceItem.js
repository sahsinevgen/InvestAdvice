import React from 'react';

var counter = 0;

function AdviceItem({advice}) {

    function adviceToText(advice) {
        let text = advice['currency'] + ' ' + advice['operation_type'].toString().toUpperCase() + '\n\n'
                 + 'entry: ' + parseFloat(advice['entry']).toFixed(2) + '\n\n';

        advice['take_profits'].map(tp => {text += 'TP: ' + parseFloat(tp['entry']).toFixed(2) + '\n'});
        advice['stop_losses'].map(sl => {text += 'SL: ' + parseFloat(sl['entry']).toFixed(2) + '\n'});

        text += '\nsource: \n'+ advice['source'] + '\n';
        text += 'time: ' + advice['datetime'] + '\n'
        return text;
    }

    return (
        <div class='border'>
            {/* <div class='title'>{advice['currency'] + " " + advice['operation_type'].toString().toUpperCase()}</div>
            <div class='line'> </div> */}
            <div class='text' style={{'font-size': '20px', 'user-select': 'text'}}>
                {adviceToText(advice)}
            </div>
        </div>

    );
}
export default AdviceItem;