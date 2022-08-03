import csv

from flask import jsonify


class IndexModel:
    def __init__(self):
        self.description = "API Starting Page"
        self.message = "This is a sample flutter flask API template"

    def to_json(self):
        return jsonify(description=self.description,
                       message=self.message,
                       )


class InfoModel:

    def __init__(self):
        self.info = self.__get_info()

        # all info fields - activate in schemas.py
        self.id = [d['id'] for d in self.info if 'id' in d]
        self.object_hash = [d['object_hash'] for d in self.info if 'object_hash' in d]
        self.message = [d['message'] for d in self.info if 'message' in d]

    @staticmethod
    def __get_info():
        with open('data/sample_data.csv') as f:
            list_of_dicts = [{k: str(v) for k, v in row.items()}
                             for row in csv.DictReader(f, skipinitialspace=True)]

        return list_of_dicts


class ImageModel:

    def __init__(self, name, filetype, size, shape, message):
        self.message = message
        self.name = name
        self.filetype = filetype
        self.size = size
        self.shape = shape
