import os
import random
from util import progressbar
from typing import List
from urllib.request import urlretrieve

def get_endpoint(seed: int, size=300, url="https://picsum.photos") -> str:
    """ Helper for designing the endpoint given image specifications """
    if seed:
        url += f"/seed/{seed}"
    url += f"/{size}"
    return url

def generate_seeds(master_seed: str, number_of_seeds: int) -> List[str]:
    """ Generates a list of integer seeds deterministictly based on a master seed """
    print(f"generating {number_of_seeds} seeds based on master seed {master_seed}")
    random.seed(master_seed)
    seeds = []
    while len(seeds) < number_of_seeds:
        seed = random.randint(1, 999999)
        if seed not in seeds:
            seeds.append(seed)
    return sorted(seeds)

def download_images(master_seed: int, n_images: int, image_directory="./img") -> None:
    """ Initates and manages the flow of downloads """
    seeds = generate_seeds(master_seed, n_images)
    for i in progressbar(range(n_images), f"Downloading images to '{image_directory}':", 35):
        seed = seeds[i]
        url = get_endpoint(seed)
        filepath = os.path.join(image_directory, f"{seed}.jpg")
        urlretrieve(url, filepath)
    return