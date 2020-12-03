import sys
import functions as f

args = sys.argv

# TODO:

entry_folder = ""
output_folder = ""
filters = ""
run = True
args_required = ["-i", "-o"]
i = 0

for arg in args_required:
    if arg in args:
        continue
    else:
        if arg == "-i":
            print(f"L'argument {arg} est nécessaire pour connaitre le chemin des images initale")
            run = False
        if arg == "-o":
            print(f"L'argument {arg} est nécessaire pour connaitre le chemin des images en sortie")
            run = False

if run:
    for arg in args:

        if arg == "--h":
            print("usage: imagefilter")
            print("--h,----help")
            print("-i,--input-dir <directory>")
            print("-o,--output-dir <directory>")

        if len(args) == 1:
            print("Add arguments please")

        if arg == "-i":
            if f.next_arg_exist(i, args):
                entry_folder = args[i+1]

        elif arg == "-o":
            if f.next_arg_exist(i, args):
                output_folder = args[i+1]

        elif arg == "--filters":
            if f.next_arg_exist(i, args):
                if "grayscale" in args[i+1]:
                    filters += "grayscale, "
                elif "blur" in args[i+1]:
                    filters += "blur, "
                elif "dilate" in args[i+1]:
                    filters += "dilate, "
                else:
                    filters = "filter do no exist"
                    run = False
            if run:
                f.application_filter(entry_folder, output_folder, filters)

        i += 1

    f.application_filter(entry_folder, output_folder, filters)