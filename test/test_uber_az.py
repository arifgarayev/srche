import os

from src.services.uber_az import Uber_az
from src.services.emulator import Emulator
from src.utils.common import Utils

# print(os.getcwd())

emu = Emulator(Utils.get_json_to_dict(os.getcwd() + "/src/config/emulator_config.json"))

uber = Uber_az(emu)

uber.start_uber_app()
