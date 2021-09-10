import os
from pathlib import Path
from random import choice

import config
from modules import utils, weather, embedder

PATH = Path(os.path.dirname(os.path.realpath(__file__)))
WALLPAPERS_PATH = PATH / config.FOLDER_NAME

# Folders
if not WALLPAPERS_PATH.exists():
    print(f'No {WALLPAPERS_PATH} folder was found, create it first using generate_folders.py')
    exit()
ranges = utils.get_ranges(WALLPAPERS_PATH)

# Weather
temperature = weather.get_temperature(config.CITY_NAME)

# Wallpaper
range_idx = utils.find_range(temperature, ranges)
wallpapers = utils.get_all_files(WALLPAPERS_PATH / ranges[range_idx][2])

if len(wallpapers) == 0:
    print('No suitable wallpapers found.')
    exit()

wallpaper = choice(wallpapers)

if config.EMBED_TEMPERATURE:
    embedder.embed_text(wallpaper, f"{int(temperature)}°", 'wallpaper.png')

# Change wallpaper
utils.change_wallpaper(PATH / 'wallpaper.png')
print("Wallpaper changed.")
