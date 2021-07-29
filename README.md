# py-lorem-picsum
[picsum.photos](https://picsum.photos) is a brilliant API written by David Marby & Nijiko Yonskai. This library/tool is a little helper for downloading images in a easy and experimentally reproducable way from their API.

I would use this in image labeling ML tasks to ensure that my model can adequately detects non-relevant data.

## Installation
Assuming you have Python3 installed, simply use the package manager [pip](https://pip.pypa.io/en/stable/) to install py-lorem-picsum.

    pip install lorempicsum

## Usage

    python -m lorempicsum \
        --folder myimages \
        --number 100 \ 
        --seed 42 \
        --size 300

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Tests

Run via unittest module:

    python -m unittest

## License
[MIT](https://choosealicense.com/licenses/mit/)