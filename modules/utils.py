import ctypes
from pathlib import Path

def find_range(value, ranges):
    for i, rng in enumerate(ranges):
        if i == 0:
            if value <= rng[0]:
                return i
        elif i == len(ranges) - 1:
            if value >= rng[1]:
                return i
        if rng[0] < value <= rng[1]:
            return i 

def get_ranges(folder_path):
    ranges = [tuple(map(int, p.stem.split('_'))) + (p.stem,) for p in folder_path.iterdir() if p.is_dir()]
    return sorted(ranges, key=lambda x: x[0])

def get_all_files(path):
    return [f for f in path.iterdir() if f.is_file()]

def change_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 0)