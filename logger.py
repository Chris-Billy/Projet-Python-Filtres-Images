from datetime import datetime

def log(msg):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y - %H:%M:%S >>>")
    with open('imagefilter.log', 'a') as f:
        f.write(f"{timestamp} = {msg} \n")