def loading_bar(length, current_length, bar_length=10, dot=False, line=True, corpus=True, arrow=True, delete_line=1, percent=True):
    part = int(current_length / length * bar_length)
    i = 0
    while delete_line > 0:
        print('', end='\r')
        delete_line -= 1
    if corpus:
        print('[', end='')
    while i < part:
        if dot:
            print('.', end='')
        elif line:
            print('-', end='')
        i += 1
    part = bar_length - part - 1
    if part < bar_length and arrow:
        print('>', end='')
    while part > 0:
        print(' ', end='')
        part -= 1
    if corpus:
        print(']', end='')
    if percent:
        print(' ' + str(current_length/length*100)[:4] + '%', end='')
