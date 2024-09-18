# coding: utf-8
"""

Abstract::
    -
History::
    - Ver.      Date            Author        History
    -
"""
# 標準ライブラリ

# 関連外部ライブラリ
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

class SDService:
    """
    StableDiffusionをラップしたクラス
    """

    def __init__(self):
        """
        クラスのコンストラクタ
        """
        self.__model_id = "CompVis/stable-diffusion-v1-4"
        self.__step_no = 15
        self.__scheduler = EulerDiscreteScheduler.from_pretrained(self.__model_id, subfolder="scheduler")
        self.__pipe = StableDiffusionPipeline.from_pretrained(self.__model_id, scheduler=self.__scheduler) #, torch_dtype=torch.float16
        self.__pipe = self.__pipe.to("cpu")

    def create_img(self, text):
        """Create Image
        """
        try:
            prompt = text
            image = self.__pipe(prompt, num_inference_steps=self.__step_no).images[0]
            return image
        except Exception as e:
            raise e

