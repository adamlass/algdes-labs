import glob, sys, os, time

directory = sys.argv[1]

file_dirs = list(glob.glob(directory))
file_dirs.sort(key=lambda x: x)

OUT_FILE_NAME = "outputs/test.txt"

os.system(f"> {OUT_FILE_NAME}")

# for file_dir in file_dirs:
for file_dir in file_dirs:
    print(f"Running for {file_dir}")
    os.system(f'python3 src/cp.py {file_dir} >> {OUT_FILE_NAME}')
    print("done")