import os

from src.services.uber_az import Uber_az
from src.services.emulator import Emulator
from src.utils.common import Utils
from src.services.sms_activate import SMSActivator
from src.entity.common_queries import Query


class CommonObjectGenerator:
    def __init__(self):
        self.emu = Emulator(
            Utils.get_json_to_dict(os.getcwd() + "/src/config/emulator_config.json")
        )
        self.db = Query(
            Utils.get_json_to_dict(os.getcwd() + "/src/config/database_config.json")[
                "DB_conn_str"
            ]
        )
        self.sms = SMSActivator()
