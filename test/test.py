import subprocess
import os


os.system(
    f"adb shell monkey -p {subprocess.check_output('adb shell pm list packages | grep dkapp', shell=True).decode().split(':')[-1].strip()} -c android.intent.category.LAUNCHER 1"
)

print(
    f"adb shell monkey -p {subprocess.check_output('adb shell pm list packages | grep dkapp', shell=True).decode().split(':')[-1].strip()} -c android.intent.category.LAUNCHER 1"
)
