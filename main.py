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

    i += 1

f.application_filter(entry_folder, output_folder)