import time

from config.const import TIMESLEEP
from config.paths import path

from device.main_device import return_device
from modules.modules_start.module_start_area import start_area
from ocr.main import ocr_txt_verify
from tools.reg_click_direction import reg_direction
from modules.general.module_options_name import start_name


def module_click_start(auto_text=start_name):
    if ocr_txt_verify(path, auto_text, start_area):
        device = return_device()
        x, y = reg_direction(start_area)
        device.click(x, y)
        time.sleep(TIMESLEEP)
        return True
