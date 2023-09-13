import os
import time
import random

from src.services.uber_az import Uber_az
from src.services.emulator import Emulator
from src.utils.common import Utils
from src.scenario.common_flow_uberAZ import CommonFlowUberAZ



def main():
    xyz = CommonFlowUberAZ()

    routes_hash_map = Utils.get_json_to_dict(os.getcwd() + '/src/config/top_routes.json')

    # xyz.reinstall_with_new_id()

    if not xyz.uber.package_name:
        xyz.reinstall_with_new_id()

        time.sleep(5)

        xyz.uber.start_uber_app()

    xyz.uber.kill_uber_app()

    xyz.uber.start_uber_app()

    # time.sleep(5)
    if not xyz.uber.is_any_active_order():
        try:
            xyz.uber.click_gps_location_circle()

        except:
            xyz.uber.kill_uber_app()

            time.sleep(10)

            xyz.uber.start_uber_app()

            time.sleep(50)

            xyz.uber.click_gps_location_circle()

    else:
        time.sleep(10)
        print(xyz.handle_active_order())

        xyz.cancel_active_order()

    while True:
        random_key = random.choice(list(routes_hash_map))
        x, y = random_key, routes_hash_map[random_key]

        xyz.send_new_state_route(x, y)

        time.sleep(5)

        is_confirmed = xyz.confirm_ride()

        if not is_confirmed:
            # uninstall app
            # clone app with new ID

            xyz.reinstall_with_new_id()

            time.sleep(3)

            xyz.uber.start_uber_app()

            time.sleep(8)

            xyz.uber.kill_uber_app()

            time.sleep(3)

            xyz.uber.start_uber_app()

            time.sleep(8)

            # handle access issues

            xyz.send_new_state_route(x, y)

            xyz.confirm_ride()

        print(xyz.handle_active_order())

        xyz.cancel_active_order()



if __name__ == "__main__":

    main()



