from configparser import ConfigParser
from functions import config_filter

def get_config_file(conf_file):
    f"""
    Récupère les configurations du fichier ini sous forme de dictionnaire enregistré dans un tableau
    :param conf_file: le nom du fichier où se trouve les configurations (file.ini)
    :return: un tableau de dictionnaire (array = ['{"key": "value"}'])
    """
    config = []

    parser = ConfigParser()
    parser.read(conf_file)

    entry_folder = parser.get("general", "input_dir")
    config.append({"input_dir": entry_folder})

    output_folder = parser.get("general", "output_dir")
    config.append({"output_dir": output_folder})

    log_file = parser.get("general", "log_file")
    config.append({"log_file": log_file})

    filters_list = config_filter(parser.get("filters", "content"), log_file)
    config.append({"content": filters_list})

    return config