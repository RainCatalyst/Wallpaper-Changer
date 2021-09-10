import os
import argparse
import config
from pathlib import Path

WALLPAPERS_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / config.FOLDER_NAME

# https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
def split_range(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

parser = argparse.ArgumentParser(description='Generate temperature folders.')
parser.add_argument('min', metavar='m', type=int,
                    help='min temperature')
parser.add_argument('max', metavar='M', type=int,
                    help='max temperature')
parser.add_argument('count', metavar='C', type=int,
                    help='folder count')
args = parser.parse_args()

if WALLPAPERS_PATH.exists():
    print(f'{WALLPAPERS_PATH} folder already exists, please remove it to create a new one')
    exit()

WALLPAPERS_PATH.mkdir(parents=False, exist_ok=True)

for rng in split_range(range(args.min, args.max), args.count):
    (WALLPAPERS_PATH / f'{rng[0]}_{rng[-1] + 1}').mkdir(parents=False, exist_ok=True)

print(f'Created {args.count} folders.')