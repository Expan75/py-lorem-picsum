import os
import sys
import random
from typing import List, Iterable
from urllib.request import urlretrieve

def get_image_url(seed: int, size=300, url="https://picsum.photos") -> str:
    """ Helper for designing the endpoint given image specifications """
    if seed:
        url += f"/seed/{seed}"
    url += f"/{size}"
    return url

def generate_seeds(master_seed: int, n_seeds: int) -> List[int]:
    """ Generates a list of integer seeds deterministictly based on a master seed """
    print(f"generating {n_seeds} seeds based on master seed {master_seed}")
    random.seed(master_seed)
    seeds = []
    while len(seeds) < n_seeds:
        seed = random.randint(1, 999999)
        if seed not in seeds:
            seeds.append(seed)
    return sorted(seeds)

def progressbar(iterable: Iterable, prefix="", size=60, file=sys.stdout):
    """ Simple progressbar shamelessy ripped from: 
        https://stackoverflow.com/questions/3160699/python-progress-bar/34482761#34482761

        Can be used on any iterable but brakes on generators without list casting (?)
    """
    count = len(iterable)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def download_images(master_seed: int, n_images: int, image_directory="./img") -> None:
    """ Initates and manages the flow of downloads """
    seeds = generate_seeds(master_seed, n_images)
    for i in progressbar(range(n_images), f"Downloading images to '{image_directory}':", 35):
        seed = seeds[i]
        url = get_image_url(seed)
        filepath = os.path.join(image_directory, f"{seed}.jpg")
        urlretrieve(url, filepath)
    return

class DirectoryAlreadyContainsPhotosExecption(Exception):
    pass

def verify_valid_directory(dir_path: str) -> bool:
    """Checks if a filled image directory already exists; safely throws if it does contain images"""
    if os.path.exists(dir_path) and len(os.listdir(dir_path)) > 0:
        raise DirectoryAlreadyContainsPhotosExecption('non-empty directory already detected; exiting...')
    else:
        os.makedirs(dir_path, exist_ok=True)