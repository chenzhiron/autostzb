from modules.module_duiwu.module_duiwu import module_click_zhengbing_duiwu
from modules.module_fanhui.module_fanhui import module_return_main, module_return_index
from modules.module_shili.module_shili import module_click_shili
from modules.module_zhengbing.module_zhengbing import module_zhengbing_click, module_swipe_zhengbing_click, \
    module_zhengbing_affirm_btn, module_zhengbing_computed_time, module_zhuangbing_require, module_verify_zhengbing


# 处理 添加征兵队列1个|2个|3个的阻塞拦截
def zhengbing(i):
    zhengbing_status = {
        "times": 0,
        'lists': i
    }
    module_click_shili()
    module_click_zhengbing_duiwu(i)
    module_zhengbing_click()
    if module_verify_zhengbing():
        pass
    else:
        module_swipe_zhengbing_click()
        maxtime = module_zhengbing_computed_time()
        module_zhengbing_affirm_btn()
        module_zhuangbing_require()
        zhengbing_status['times'] = maxtime
    module_return_main()
    module_return_main()
    module_return_main()
    module_return_main()
    module_return_index()
    return zhengbing_status

# if __name__ == '__main__':
#     connect_device()
#     result = zhengbing(3)
#     print(result)
