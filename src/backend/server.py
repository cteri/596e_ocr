from ..ml.model import OcrModel
from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import ImageResult, ResponseModel

model = OcrModel()
server = MLServer(__name__)


@server.route('/ocr', input_type=DataTypes.IMAGE)
def ocr(inputs: list[dict], parameters: dict):
    results = model.predict(inputs)
    results = [
        ImageResult(file_path=res["file_path"], result=res["result"]) for res in results
    ]
    response = ResponseModel(results=results)
    return response.get_response()


server.run()
