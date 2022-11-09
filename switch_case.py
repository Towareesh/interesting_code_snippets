# checkin

def switch_case(n):
    ''' Implementation switch_case
    '''
    switches = {
        0: 'штиль',
        1: 'тихий ветер',
        2: 'легкий ветер',
        3: 'слабый ветер',
        4: 'умеренный ветер',
        5: 'свежий ветер',
        6: 'сильный ветер'
    }.get(n, 'шторм')

    return switches