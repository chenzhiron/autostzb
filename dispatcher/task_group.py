from modules.pageSwitch.page_switch import *
# 征兵
conscription = [handle_in_map_conscription]
# 扫荡
mopping_up = [handle_in_lists_action, handle_in_battle_result, handle_in_map_conscription]
# 出征


task_all = {}


def set_task_all(key, value):
    task_all[key] = value


def get_task_all(key):
    return task_all[key]