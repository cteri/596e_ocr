# OCR tool

## 0. Installing requirements
```
python3 -m pip install -r requirements.txt
```

## 1. Flask-ML
### Starting the server
```
python3 -m src.backend.server
```

### Client example
```
python3 client.py
```

## 2. CLI
### Command line tool
* OCR a single file
```
python3 cmd_client.py --output_directory ./out --image_file ./input_dir/english.png
```
