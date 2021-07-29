from engine import download_images
from util import verify_valid_directory

def run_as_tool():
    from cli import args

    seed, n_images, image_dir = args.seed, args.number, args.folder 

    verify_valid_directory(image_dir)
    download_images(master_seed=seed, n_images=n_images, image_directory=image_dir)

if __name__ == '__main__':
    run_as_tool()