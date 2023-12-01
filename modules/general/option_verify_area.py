# 点击空白，回到静态页
address_empty = (360, 360)

# 坐标跟扫荡
# 右上角的展开标记 按钮
address_area_start = (1220, 85)
# 识别中间的标记
address_sign_verify = (965, 100, 1060, 140)
# 点击中间的标记
address_sign_area = (1010, 120)

# 标记第一个坐标
address_sign_land_area = (900, 200)

# 截图扫荡/出证 区域的 大致范围
address_execute_order_area = (820, 200, 1150, 510)

# 选择部队出征，分别代表 5只编队5种可能性
address_execute_list = [
    [(640, 600)],
    [(540, 600), (750, 600)],
    [(460, 600), (650, 600), (840, 600)],
    [(340, 600), (540, 600), (730, 600), (930, 600)],
    [(265, 600), (460, 600), (640, 600), (850, 600), (1040, 600)]
]

# 选择编队页面右上角 当前解锁了几队
bianduilists = (1060, 140, 1120, 176)

computed_going_time_area = (615, 520, 710, 555)
computed_going_list_area = (0, 540, 200, 600)

# 部队出征/扫荡 最后一个页面
address_going_require = (1120, 660)

# 选择部队页面，如果当前部队 没有体力，对应识别时间冷却 5种可能性
tili_area = [
    [(590, 590, 690, 625)],
    [(495, 590, 595, 625), (685, 590, 785, 625)],
    [(390, 590, 500, 625), (580, 590, 680, 625), (780, 590, 885, 625)],
    [(285, 590, 395, 625), (475, 590, 575, 625), (675, 590, 775, 625), (875, 590, 980, 625)],
    [(185, 590, 300, 625), (400, 590, 500, 625), (600, 590, 700, 625), (800, 590, 900, 625), (1000, 590, 1100, 625)]
]

# ——--------------------------------------------
# 战报
discern_time_area = (850, 180, 1150, 240)
# 主页面右下角战报位置
click_draw_area = (110, 540)

# 战报第一个页面 识别区域  个人战报
person_battle_area = (0, 0, 500, 65)
# 首封战报位置
click_draw_detail_area = (600, 270)

# 我方人数
person_status_number_area = (0, 100, 160, 145)
# 敌方人数
enemy_status_number_area = (1120, 100, 1280, 145)
# 战报的状态 胜利 平局 战败
status_area = (580, 90, 690, 150)

# ——--------------------------------------------
# 点击势力的坐标
shili_click = (326, 640)

# ——--------------------------------------------
# 点击势力后 进入第一个页面，左上角征兵
zhengbing_page_verify_area = (0, 0, 200, 60)
# 第一个部队坐标
click_list_x_y = (150, 260)
# 部队 征兵 按钮的位置
zhengbing_page_area = (575, 470, 705, 520)
# 征兵按钮点击的位置
zhengbing_click_xy = (650, 500)
# 判断征兵滑块区域是否可以滑动
zhengbing_page_swipe_verify = (1000, 630, 1130, 670)
# 点击确认征兵按钮
zhengbing_page_swipe_sure_xy = (1080, 650)
# 征兵滑块区域
zhengbing_page_swipe = ((410, 435, 850, 435),
                        (410, 545, 850, 435),
                        (410, 650, 850, 435))
# 征兵时间
zhengbing_time_area = (760, 385, 848, 635)

# 征兵确认区域 / 去往战报平局确定区域
queding_area = (700, 450, 880, 500)
# 征兵点击位置
queding_area_xy = (750, 480)
# ——--------------------------------------------
# 招募 位置
zhaomu_area = (1140, 670, 1210, 705)

# 点击返回首页的按钮位置 该点击区域位置不同尺寸展示位置不明， 但点击效果有
return_area = (1200, 60)

# 平局点击编队，需要点查到是否点击到位，出现 扫荡或者出征字眼在点击中心点
retreat_area_require = (800, 200, 1060, 400)
# 战报平局模块
retreat_area = (1040, 300, 1130, 330)
# 点击部队撤退区域
retreat_click_area = (1040, 290, 1280, 330)
# 点击部队撤退基准坐标
retreat_click_area_xy = (1080, 315)
# 确认 点击部队撤退基准区域
retreat_append_click = (1110, 640, 1200, 680)
# 确认 撤退基准坐标
retreat_append_click_xy = (1150, 660)
# 战报战斗地点点击位置
battle_site = (770, 690)

# 当前土地，屏幕中心点
retreat_require_click = (640, 360)

# 取消第四个标记，认为出征成功
cancel_sign = (1150, 405)
# 第四个标记基准区域
chuzheng_area =(880, 375, 1050, 430)