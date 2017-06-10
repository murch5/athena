import os as os

import factory_manager as fm

import logging as logging
logger = logging.getLogger(__name__)

class Data(fm.FactoryObject):

    def load(self):
        return

    def process_data(self):
        self.data = self.process_manager.pass_thru_stack(self.data)
        pass

    def set_process_manager(self, process_manager):
        self.process_manager = process_manager
        pass

    def initialize_attr(self):

        self.data = None
        self.process_manager = None
        self.type = None

        pass

    def do(self, data):
        self.load()
        pass
