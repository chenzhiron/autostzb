import time

from device.main_device import connect_device

from tools.reg_screenshot import general_screenshot_tools
from maps.map_area import base_area, address_area,const_w,const_h
from path.img import path
from ocr.main import ocr_map
from tools.computed_distance import base_point
from modules.module_shili.module_shili import module_click_shili
from maps.map_fn import reg_address



def map_start():
    d = connect_device()
    module_click_shili(path, '势力')
    time.sleep(1)
    general_screenshot_tools(address_area)
    result = ocr_map(path)
    list = []
    for v in result:
        list.append(v['text'])
    list = reg_address(list)
    print(result)

def screen_shot_maps():
    d = connect_device()
    general_screenshot_tools(address_area)
    # result = ocr_map(path)
    # list = []
    # for v in result:
    #     list.append(v['text'])
    # list = reg_address(list)
    # print(list)








if __name__ == '__main__':
    map_start()
    # d = connect_device()
    # # general_screenshot_tools(base_area)
    # # result = ocr_default(path)
    # # print(result)
