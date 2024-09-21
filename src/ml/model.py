import easyocr


class OcrModel:
    def __init__(self, lang_list=['en']):
        self.reader = easyocr.Reader(lang_list)  # Initialize the EasyOCR reader with specified languages

    def _validate_image_path(self, image_path: str) -> None:
        if image_path is None:
            raise ValueError("image_path cannot be None")

    def read_text(self, image_path: str, out_dir: str = None) -> str:
        self._validate_image_path(image_path)

        result = self.reader.readtext(image_path, detail=0)
        result_text = ' '.join(result)

        return result_text

    def predict(self, image_paths: list[str]) -> list[dict]:
        return [{'file_path': str(image_path.file_path), 'result': self.read_text(image_path.file_path)} for image_path
                in image_paths]
