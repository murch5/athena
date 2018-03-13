import os as os

import factory_manager as fm


import logging as logging
logger = logging.getLogger(__name__)

class Data(fm.FactoryObject):

    def load(self):
        return

    def initialize(self):

        self.data = None
        self.type = None

        pass


    def do(self, data):
        self.load()
        pass
