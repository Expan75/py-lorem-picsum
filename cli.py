import argparse

parser = argparse.ArgumentParser(description='CLI tool for complimenting image classification')
parser.add_argument('-f', '--folder', default='images/', help='Specify the path of a directory in which to store photos')
parser.add_argument('-n', '--number', help='Specify how many images you want to download', type=int)
parser.add_argument('-s', '--seed', type=int,
    help='Used to ensure the same images are downloaded. Useful for reproduction of experiements and datasets')
args = parser.parse_args()
assert args.number and args.seed, 'Please provide how many images you want to download and a seed to ensure replication!'

 