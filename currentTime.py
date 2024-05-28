import time

"""
Este programa utiliza o módulo time para retornar o tempo em segundos e realiza
as devidas conversões para horas, minutos, segundos e dias.
No fim, ele exibe os dados formatados para melhor vizualização.
"""

last_epoch = time.time()

def current_time(since_epoch):
    hours_since = since_epoch // 60 // 60
    current_hour = (hours_since - (hours_since // 24) * 24) - 3
    minutes_since = since_epoch // 60
    current_minute = minutes_since - (minutes_since // 60) * 60
    second_since = since_epoch // 1
    current_second = second_since - (second_since // 60) * 60

    return current_hour, current_minute, current_second

def days_since_epoch(epoch):
    days = epoch // 60 // 60 // 24

    return days

hours, minutes, seconds = current_time(last_epoch)
days = days_since_epoch(last_epoch)

print(f'Current time: {int(hours)}:{int(minutes)}:{int(seconds)}')
print(f'Days since last epoch: {int(days)}')