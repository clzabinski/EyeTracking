import ctypes


class ScreenMeasurement:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.screensize0 = self.user32.GetSystemMetrics(0)
        self.screensize1 = self.user32.GetSystemMetrics(1)


def screen_measurement():
    return ScreenMeasurement()
