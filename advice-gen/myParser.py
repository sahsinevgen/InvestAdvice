import re

def parse(msg):
    currency = None
    operation_type = None
    entry = None

    stop_losses = []
    take_profits = []

    msg = msg.upper()
    
    for i, line in enumerate(msg.split('\n')):
        words = line.split()

        double_values = re.findall(r"[+]?(?:\d*\.\d+|\d+)", line)

        if len(words) == 0:
                continue

        if i == 0:
            if words[0] == 'BUY' or words[0] == 'SELL':
                operation_type = words[0]
                if len(words) > 1:
                    currency = words[1]
            else:
                currency = words[0]

            if len(double_values) > 0 and len(words) > 1:
                entry = float(double_values[-1])
            
            continue
        
        if len(double_values) == 0:
            continue

        if re.search('ENTRY', line) :
            entry = float(double_values[-1])
            continue

        if re.search('TP|PROFIT', line):
            take_profits += [float(double_values[-1])]
            continue

        if re.search('SL|LOSS', line):
            stop_losses += [float(double_values[-1])]
            continue


    if currency == None \
        or entry == None \
        or len(stop_losses) == 0 \
        or len(take_profits) == 0:

        return None
    
    take_profits.sort()
    stop_losses.sort()

    if operation_type == None:
        if entry < take_profits[0]:
            operation_type = 'BUY'
            stop_losses.reverse()
        else:
            operation_type = 'SELL'
            take_profits.reverse()
    else:
        if operation_type == 'BUY':
            stop_losses.reverse()
        else:
            take_profits.reverse()

    
    x = 1
    if operation_type == 'SELL':
        x = -1
    
    if entry * x > take_profits[0] * x \
        or entry * x < stop_losses[0] * x:

        return None

    res = {
        'currency': currency,
        'operation_type': operation_type,
        'entry': entry,
        'stop_losses': stop_losses,
        'take_profits': take_profits
    }

    return res
