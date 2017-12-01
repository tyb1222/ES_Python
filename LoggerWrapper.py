# coding : utf-8

import logging
import os
import types


class LoggerWrapper(object):
    _singleton = {}

    def __new__(cls, *args, **kwargs):
        if not (cls in cls._singleton):
            cls._singleton[cls] = object.__new__(cls)
            object.__init__(args, kwargs)
        return cls._singleton[cls]

    def __init__(self):
        self.logger = logging.getLogger()
        dir_path = os.getcwd()
        handler = logging.FileHandler(os.path.join(dir_path, "service.log"))
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    __slots__ = "logger"

    def __get__(self, instance, owner):
        return types.MethodType(self.logger, instance, owner)

    @staticmethod
    def log(func):
        print dir(LoggerWrapper)

        def inner_func(*args):

            LoggerWrapper.logger(args)
            func(args)

        return inner_func
