import sys
import functions as f
from logger import *
from configparser import ConfigParser


args = sys.argv
filters_list = []
entry_folder = "imgs"
output_folder = "output"
conf_file = "imagefilter.ini"
log_file = "imagefilter.log"
i = 0

for arg in args:

    if arg == "--h":
        print("usage: imagefilter")
        print("--h,----help")
        print("-i,--input-dir <directory>")
        print("-o,--output-dir <directory>")
        print("--conf-file <file.ini>")
        print("--log-file <file.log>")
        print("--filters <grayscale|blur:5|dilate:10")

    if len(args) == 1:
        print("Add arguments please")

    if arg == "--conf-file":
        if f.next_arg_exist(i, args):
            if args[i+1].lower().endswith(".ini"):
                conf_file = args[i+1]
            else:
                print(f"{args[i+1]} n'est pas de type (.ini), 'imagefilter.ini' par défaut")
                conf_file = "imagefilter.ini"
            parser = ConfigParser()
            parser.read(conf_file)
            entry_folder = parser.get("general", "input_dir")
            output_folder = parser.get("general", "output_dir")
            log_file = parser.get("general", "log_file")
            filters_list = f.config_filter(parser.get("filters", "content"), log_file)
            if len(filters_list) == 0:
                print("Enter an existing filter")
            else:
                f.application_filter(entry_folder, output_folder, filters_list, log_file)
                dump_log(log_file)

    if arg == "-i":
        if f.next_arg_exist(i, args):
            entry_folder = args[i+1]

    elif arg == "-o":
        if f.next_arg_exist(i, args):
            output_folder = args[i+1]

    elif arg == "--log-file":
        if f.next_arg_exist(i, args):
            log_file = get_log_file(args[i+1])

    elif arg == "--filters":
        if f.next_arg_exist(i, args):
            filters_list = f.config_filter(args[i+1], log_file)
            if len(filters_list) == 0:
                print("Enter an existing filter")
            else:
                f.application_filter(entry_folder, output_folder, filters_list, log_file)
                dump_log(log_file)

    i += 1