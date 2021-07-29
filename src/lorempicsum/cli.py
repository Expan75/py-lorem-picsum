import argparse

parser = argparse.ArgumentParser(description='CLI tool for complimenting image classification')
parser.add_argument('-f', '--folder', default='images', help='Specify the path of a directory in which to store photos')
parser.add_argument('-n', '--number', help='Specify how many images you want to download', type=int)
parser.add_argument('-s', '--seed', type=int,
    help='Used to ensure the same images are downloaded. Useful for reproduction of experiements and datasets')
parser.add_argument('-z', '--size', type=int,
help='The size of the downloaded image. Right now only square images are supported.')
args = parser.parse_args()

def main():
    from .engine import verify_valid_directory, download_images
    if not args.number or not args.seed: 
        raise RuntimeError('Please provide both an integer for the number of images to download, as well as an integer seed to ensure replication! See --help for more information on arguments.')
    verify_valid_directory(args.folder)
    download_images(master_seed=args.seed, n_images=args.number, image_directory=args.folder, size=args.size)

if __name__ == '__main__':
    main()