from platform import platform
import subprocess
import sys
import ctypes


def get_screen_resolution():
    if sys.platform.startswith("win32"):
        user32 = ctypes.windll.user32
        screensize0 = user32.GetSystemMetrics(0)
        screensize1 = user32.GetSystemMetrics(1)
        return (screensize0, screensize1)

    elif sys.platform.startswith("linux"):
        output = subprocess.Popen(
            'xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE
        ).communicate()[0]
        output = output.decode("utf-8")
        screensize0 = output[0:4]
        screensize1 = output[5:9]
        return (screensize0, screensize1)


if __name__ == "__main__":
    print(get_screen_resolution())
