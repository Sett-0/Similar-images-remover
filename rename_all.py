import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--shift', type=int, default=0, help='Starting naming index. Can be used to add pics later.')
parser.add_argument('--stop_after', type=int, default=None, help='Rename only first X files.')
args = parser.parse_args()

shift = args.shift
stop_after = args.stop_after

files = os.listdir('.')
files.pop(-1)
files.sort(key=lambda filename: int(filename.split('.')[0]))
count = 1

for filename in files:
    os.rename(filename, str(count + shift) + filename[-4:])
    if (count == stop_after): break
    count += 1