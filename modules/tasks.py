from dispatcher.Dispatcher import task_dispatcher
from modules.taskGroup import handle_in_map_conscription, handle_in_lists_action, handle_in_battle_result, \
    handle_in_unmark, handle_in_draw_battle
from config.task_or_web_common import saodangType, chuzhengType, zhengbingType, wotuType, chengpiType


class Task:
    dispatcher = task_dispatcher

    @classmethod
    def set_task_group(cls, t):
        if t == zhengbingType:
            return [handle_in_map_conscription]
        elif t == saodangType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription]
        elif t == chuzhengType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription, handle_in_unmark]
        elif t == wotuType or t == chengpiType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription]
        else:
            return []

    def __init__(self, t, circulation=1):
        self.task_group = self.set_task_group(t)
        self.type = t
        self.circulation = circulation
        self.setup = 0
        self.delay_time = 0
        self.offset = 0
        self.next_times = 0
        self.status = False
        self.lists = 1
        self.txt = None
        self.battle_result = None

    def add_attribute(self, key, value):
        setattr(self, key, value)

    def change_config_storage_by_key(self, key, value):
        setattr(self, key, value)
        return getattr(self, key)

    def next_start(self):
        # from web.configs.update import update_web
        if self.circulation > 0 and self.status:  # 当 circulation 大于 0 时，才减少 circulation
            self.change_config_storage_by_key('setup', 0)
            next_time = max(self.delay_time, self.next_times)
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], next_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
            self.change_config_storage_by_key('circulation', self.circulation - 1)
        elif self.circulation == 0:
            self.status = False

    # update_web()

    def next_task(self):
        if len(self.task_group) > self.setup and self.status:
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], self.next_times)
            self.change_config_storage_by_key('setup', self.setup + 1)
        else:
            if self.circulation > 0:
                self.next_start()
            else:
                self.status = False
#
# if __name__ == '__main__':
#     task1 = Task(2, 2)
#     task1.next_start()
#
#     task2 = Task(1, 1)
#     task2.next_start()
#     while 1:
#         pass