import sys, os, inspect
import functions as f
from logger import *
from config import get_config_file


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
        print("--config-file <file.ini>")
        print("--log-file <file.log>")
        print("--filters <grayscale|blur:5|dilate:10")

    if arg == "--list-filters":
        for module in os.listdir("filters"):
            if module.startswith("__"):
                continue
            else:
                module_name = inspect.getmodulename(module)
                print(module_name)

    if len(args) == 1:
        print("Add arguments please")

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
        if not "--conf-file" in args:
            if f.next_arg_exist(i, args):
                filters_list = f.config_filter(args[i+1], log_file)
                if len(filters_list) == 0:
                    print("Enter an existing filter")
                else:
                    f.application_filter(entry_folder, output_folder, filters_list, log_file)
                    dump_log(log_file)
        else:
            entry_folder = get_config_file(conf_file)[0]["input_dir"]
            output_folder = get_config_file(conf_file)[1]["output_dir"]
            log_file = get_config_file(conf_file)[2]["log_file"]
            filters_list = get_config_file(conf_file)[3]["content"]
            if f.next_arg_exist(i, args):
                filters_list = f.config_filter(args[i+1], log_file)
                if len(filters_list) == 0:
                    print("Enter an existing filter")
                else:
                    f.application_filter(entry_folder, output_folder, filters_list, log_file)
                    dump_log(log_file)

    if arg == "--config-file":
        if not "--filters" in args:
            if f.next_arg_exist(i, args):
                if args[i+1].lower().endswith(".ini"):
                    conf_file = args[i+1]
                else:
                    print(f"{args[i+1]} n'est pas de type (.ini), 'imagefilter.ini' par défaut")
                    conf_file = "imagefilter.ini"
                entry_folder = get_config_file(conf_file)[0]["input_dir"]
                output_folder = get_config_file(conf_file)[1]["output_dir"]
                log_file = get_config_file(conf_file)[2]["log_file"]
                filters_list = get_config_file(conf_file)[3]["content"]
                if len(filters_list) == 0:
                    print("Enter an existing filter")
                else:
                    f.application_filter(entry_folder, output_folder, filters_list, log_file)
                    dump_log(log_file)
    i += 1