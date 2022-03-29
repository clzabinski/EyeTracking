from platform import platform
import subprocess
import sys
import ctypes


class ScreenResolution:
    if sys.platform.startswith("win32"):

        def __init__(self):
            self.user32 = ctypes.windll.user32
            self.screensize0 = self.user32.GetSystemMetrics(0)
            self.screensize1 = self.user32.GetSystemMetrics(1)

    elif sys.platform.startswith("linux"):
        output = subprocess.Popen(
            'xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE
        ).communicate()[0]
        print(output)

    def screen_resolution(self):
        return ScreenResolution()
