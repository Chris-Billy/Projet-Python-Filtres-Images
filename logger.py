from datetime import datetime

def get_log_file(log_file):

    if log_file.lower().endswith(".log"):
        return log_file
    else:
        print(f"{log_file} n'est pas de type (.log), il a été créé dans 'imagefilter.log' par défaut")
        return "imagefilter.log"

def log(msg, log_file):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y - %H:%M:%S >>>")
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} {msg} \n")

def dump_log(log_file):
    """
    Afficher dans la console tout le contenu du fichier log qui contient les actions effectuées
    """
    try:
        with open(log_file, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)