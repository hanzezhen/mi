# =*= coding: utf-8 =*=
# @Time ： 2020/7/30 21:46
# @Author : hanzezhen

from abc import abstractmethod, ABCMeta

class Model(metaclass=ABCMeta):
    def __init__(self):
        self.is_trained = False
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def test(self):
        assert self.is_trained
        pass

    @abstractmethod
    def valid(self):
        assert self.is_trained
        pass

    @abstractmethod
    def loadModelPara(self):
        pass