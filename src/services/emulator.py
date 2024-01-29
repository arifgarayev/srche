from src.services.appium_service import Appium
from src.utils.common import Utils


import os, subprocess
import time


class Emulator(Appium):
    """
    Inherits abstract class Appium
    Appium server should be on top
    """

    def __init__(self, config: dict):
        # self.start_emulator() # FIXME
        # time.sleep(10)
        self.device_name = config["desired_caps"]["deviceName"]

        self.kill_appium_server()
        time.sleep(5)
        self.start_appium_server()  # from base abstract class
        time.sleep(5)

        # from base abstract class

        self.delete_all_appium_packages()

        # config

        # print(config)
        self.connect_selenium_appium_server(config)

        # time.sleep(15)

    def stop_appium_server(self):
        # with default port 4723
        return Appium.kill_appium_server()

    def reboot_emulator(self):
        os.system(f"adb -s {self.device_name} reboot")
        time.sleep(25)

    def list_active_adb_emulators(self):
        return subprocess.check_output(
            f"adb -s {self.device_name} devices", shell=True
        ).decode()

    def stop_adb_server(self):
        os.system(f"adb -s {self.device_name} kill-server")

    def start_emulator(self):
        os.environ["ANDROID_EMULATOR_HOME"] = (
            os.environ["ANDROID_SDK_ROOT"] + "/emulator/emulator"
        )

        # -grpc-use-jwt

        # -netdelay none -netspeed full -engine auto -no-snapshot-save
        subprocess.Popen(
            "$ANDROID_EMULATOR_HOME -avd $($ANDROID_EMULATOR_HOME -list-avds | awk '{print $1}') -grpc-use-jwt -grpc -noaudio -nocache -no-snapshot-load -gpu host -memory 4000 -engine qemu2 -nojni",
            stdout=subprocess.PIPE,
            env=os.environ.copy(),
            shell=True,
        )
        is_device_online = self.list_active_adb_emulators()

        while "emulator" not in is_device_online:
            is_device_online = self.list_active_adb_emulators()

        time.sleep(20)

        return True

    def kill_emulator(self):
        subprocess.Popen(
            f"adb -s {self.device_name} devices | grep emulator | cut -f1 | while read line; do adb -s $line emu kill; done",
            shell=True,
        )


if __name__ == "__main__":
    xxx = Emulator(
        Utils.get_json_to_dict(
            os.path.dirname(os.getcwd()) + "/config/emulator_config.json"
        )
    )

    xxx.driver.back()
