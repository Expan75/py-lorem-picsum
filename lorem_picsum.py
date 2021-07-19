import os
from engine import download_images

if __name__ == "__main__":
    image_dir = "img"
    os.makedirs(image_dir, exist_ok=True)
    download_images(master_seed=1337, n_images=5, image_directory=image_dir)