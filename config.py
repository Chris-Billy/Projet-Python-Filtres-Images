from configparser import ConfigParser
from functions import config_filter

def get_config_file(log_file):

    config = []

    parser = ConfigParser()
    parser.read(log_file)

    entry_folder = parser.get("general", "input_dir")
    config.append({"input_dir": entry_folder})

    output_folder = parser.get("general", "output_dir")
    config.append({"output_dir": output_folder})

    log_file = parser.get("general", "log_file")
    config.append({"log_file": log_file})

    filters_list = config_filter(parser.get("filters", "content"), log_file)
    config.append({"content": filters_list})

    return config