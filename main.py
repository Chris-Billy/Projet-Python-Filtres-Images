import os
import cv2
from logger import log
from filters import grayscale as g, blur as b, dilate as d
import functions as f
import sys

args = sys.argv

# TODO:

i = 0

for arg in args:

    if arg == "--h":
        print("usage: imagefilter")
        print("--h,----help")
        print("-i,--input-dir <directory>")
        print("-o,--output-dir <directory>")

    if arg == "-i":
         entry_folder = f"{args[i+1]}"

    elif arg == "-o":
        output_folder = f"{args[i+1]}/"

    elif arg == "--filters":
        split_arg = args[i+1].split("|")
        for split_arg_filter in split_arg:
            split_arg_filter_list = split_arg_filter.split(":")
            if len(split_arg_filter_list) == 2:
                print(split_arg_filter_list[1])



    i += 1

#print(split_arg)

if "moi" in split_arg:
    print("coucou")

# Séparer l'argument avec les filtres avec "|"
# Séparer l'argument du filtre avec ":"
# Savoir si un des mots correspondant à un filtre est dans la liste et donc appliquer le filtre

#f.application_filter(entry_folder, output_folder)

