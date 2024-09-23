import argparse
from pathlib import Path
from src.ml.model import OcrModel

import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")


def main():
    parser = argparse.ArgumentParser(description='Read text from image files')
    parser.add_argument('--image_file', type=str, help='The path to the image file to read text from', default=None)
    parser.add_argument('--output_directory', type=str, help='The path to the directory to save the text outputs',
                        required=True)
    args = parser.parse_args()

    if not args.image_file:
        raise ValueError("The --image_file argument must be provided.")

    image_file_path = args.image_file

    output_directory = Path(args.output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    model = OcrModel()

    # Process the image and save the text output
    result_text = model.read_text(image_file_path)
    image_file_path_obj = Path(image_file_path)
    output_file = output_directory / f"{image_file_path_obj.stem}.txt"
    with open(output_file, 'w') as file:
        file.write(result_text)
    print(f"Text for {image_file_path} saved to {output_file}")


if __name__ == '__main__':
    main()
