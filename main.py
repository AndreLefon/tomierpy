import time

#difícil para um caralho acertar esses indentedBlock

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Acabou o tempo!')

t = input('Digite o tempo em segundos: ')

countdown(int(t))
