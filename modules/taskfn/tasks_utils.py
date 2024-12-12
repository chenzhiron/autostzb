import cv2
import numpy as np
from ..ocr.main import ocr_format_val
from ..utils import formatDate


def battle_time(img,v):
  # 战报时间
		times = formatDate(ocr_format_val(np.array(img.crop([800, v + 195 + 300, 1072, v + 195 + 300+50])))) or \
				formatDate(ocr_format_val(np.array(img.crop([800, v + 195 + 230,1072, v + 195 + 230 + 50]))))
		if times is None:
			print('warning: battle times is not')
			return 10**100
		return times


class BaseTypeImg:
	def __init__(self):
		self.attack_template_img = cv2.imread('./modules/imgs/attack_template.png', cv2.IMREAD_COLOR)
		self.defense_template_img = cv2.imread('./modules/imgs/defense_template.png', cv2.IMREAD_COLOR)
		self.exploit_template_img = cv2.imread('./modules/imgs/condinate.png', cv2.IMREAD_COLOR)
