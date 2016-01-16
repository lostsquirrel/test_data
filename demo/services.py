# -*- coding:utf-8 -*-
from demo import models
from simpletor import utils
def getMyMtServcieList(page, size):
    first = (page - 1) * size
    last = first + size;

    return  dict(resultList=models.myMtServiceList[first:last],totalRecord=len(models.myMtServiceList))


def getMyMtTypes():
    return models.myMtTypes

def getMtById(mt_id):
    return models.mtDetail