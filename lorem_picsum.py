from engine import download_images, verify_valid_directory

def run_as_tool():
    from cli import args
    verify_valid_directory(args.folder)
    download_images(master_seed=args.seed, n_images=args.number, image_directory=args.folder)

if __name__ == '__main__':
    run_as_tool()
