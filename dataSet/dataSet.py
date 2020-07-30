# =*= coding: utf-8 =*=
# @Time ： 2020/7/30 21:51
# @Author : hanzezhen

from abc import abstractmethod, ABCMeta

class dataSet(metaclass=ABCMeta):
    def __init__(self,data_path):
        self.path = data_path
        pass

    @abstractmethod
    def getEventType(self):
        pass

    @abstractmethod
    def getAllData(self):
        pass

    @abstractmethod
    def getDataByPerson(self):
        pass

    @abstractmethod
    def getDataByType(self):
        pass