from datetime import datetime

def get_log_file(log_file):
    """
    Récupérer le nom du fichier log
    :param log_file: le nom du fichier où stocker les log de l'application (file.log)
    :return: le nom du fichier log (file.log)
    """
    if log_file.lower().endswith(".log"):
        return log_file
    else:
        print(f"{log_file} n'est pas de type (.log), il a été créé dans 'imagefilter.log' par défaut")
        return "imagefilter.log"

def log(msg, log_file):
    """
    Sauvegarder dans un fichier log toutes les actions effectuées par l'utilisateur
    :param msg: Le message que vous voulez ajouter dans le fichier log
    :param log_file: le nom du fichier où stocker les log de l'application (file.log)
    """
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y - %H:%M:%S >>>")
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} {msg} \n")

def dump_log(log_file):
    """
    Afficher dans la console tout le contenu du fichier log qui contient les actions effectuées
    :param log_file: log_file: le nom du fichier où stocker les log de l'application (file.log)
    """
    try:
        with open(log_file, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)