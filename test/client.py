from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

url = "http://127.0.0.1:5000/ocr"  # The URL of the server
client = MLClient(url)  # Create an instance of the MLClient object

inputs = [
    {"file_path": "./test/example/english.png"},
    {"file_path": "./test/example/english.png"},
]  # The inputs to be sent to the server
data_type = DataTypes.IMAGE  # The type of the input data
response = client.request(inputs=inputs, data_type=data_type)

print(response)  # Print the response