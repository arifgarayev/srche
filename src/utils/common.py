import os
import json
from datetime import datetime as dt

class Utils:
    """
    Common utils for
    - Converting json to dict
    - Get current date and time
    - Read or Write data from any desired file
    """


    @staticmethod
    def get_json_to_dict(path):
        file = open(path)
        return json.load(file)

    @staticmethod
    def get_date_today():
        return dt.now().strftime("%d-%m-%Y")

    @staticmethod
    def get_time_now():
        return dt.now().strftime("%H:%M")

    @staticmethod
    def last_checked(file, mode='r', data=None):

        if mode == 'r':
            file = open(os.getcwd() + file, 'r')
            return file.readline()

        if mode == 'w' and data:
            file = open(os.getcwd() + file, 'w')
            file.write(data)


if __name__ == "__main__":
    print(Utils.get_json_to_dict(os.path.dirname(os.getcwd()) + '/config/top_routes.json'))