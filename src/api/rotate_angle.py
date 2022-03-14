# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2022/3/14 18:18
@File     ：rotate_angle.py
@Software ：PyCharm
"""
from fastapi import APIRouter
from pydantic import Field, BaseModel
from typing import Optional
from commons.RotateCaptcha import RotateCaptcha


class ImageUrlBase(BaseModel):
    url: str = Field(description='url')


router = APIRouter()

rotate_captcha_bot = RotateCaptcha()


@router.post('/get_angle')
def get_angle(req: ImageUrlBase):

    rotate_image = rotate_captcha_bot.getImgFromUrl(req.url)
    predicted_angle = rotate_captcha_bot.predictAngle(rotate_image)
    res = {'angle': predicted_angle}

    return res
