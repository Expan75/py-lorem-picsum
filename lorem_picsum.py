import engine

def run_as_tool():
    from cli import args
    engine.verify_valid_directory(args.folder)
    engine.download_images(master_seed=args.seed, n_images=args.number, image_directory=args.folder)

if __name__ == '__main__':
    run_as_tool()