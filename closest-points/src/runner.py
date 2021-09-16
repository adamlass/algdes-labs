# TO RUN THE FILE EXAMPLE:
# python3 src/runner.py "data/*-tsp.txt" 

import glob, sys, os, time

directory = sys.argv[1]

file_dirs = list(glob.glob(directory))
file_dirs.sort(key=lambda x: x)

# for file_dir in file_dirs:
print("starting")
os.system(f'python3 src/cp.py {" ".join(file_dirs)} > outputs/test.txt')
print("done")
    
