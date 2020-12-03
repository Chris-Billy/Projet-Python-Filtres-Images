import sys
import functions as f
from logger import log


args = sys.argv
filters_list = []
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

# if run:
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
            # On récupère tous nos filtres dans un tableau
            all_filters = args[i+1].split("|") # ['grayscale', 'blur:10', 'dilate:15']
            for filter in all_filters:
                # filter.split(":") = ['grayscale'] - ['blur', '10'] - ['dilate', '15']
                if "grayscale" in filter:
                    grayscale = filter.split(":")
                    filters_list.append({"name": grayscale[0]})
                if "blur" in filter:
                    blur_split = filter.split(":")
                    intensity = int(blur_split[1])
                    # On vérifie que le flou soit positif ET impaire
                    if intensity < 0 or intensity % 2 == 0:
                        print("La valeur du flou doit etre positive ET impaire")
                        log("Gossian Blur => Tentative echouee, la valeur du flou est incorrect")
                        quit()
                    else:
                        filters_list.append({"name": blur_split[0], "intensity": intensity})
                if "dilate" in filter:
                    dilate_split = filter.split(":")
                    intensity = int(dilate_split[1])
                    filters_list.append({"name": dilate_split[0], "intensity": intensity})
            if len(filters_list) == 0:
                print("Enter an existing filter")
            else:
                f.application_filter(entry_folder, output_folder, filters_list)

    i += 1