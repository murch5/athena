import os as os

import factory_manager as fm
import process as process

import logging as logging
logger = logging.getLogger(__name__)

class Data(fm.FactoryObject):

    def load(self):
        return

    def process_data(self):
        self.data = self.process_manager.pass_thru_stack(self.data)
        pass

    def initialize(self):

        self.data = None
        self.type = None
        self.process_manager = None
        pass

    def build_process_stack(self):

        self.process_manager = process.ProcessManager(process)
        self.process_manager.populate_from_xml(self.xml.find("processing"))
        pass

    def do(self, data):
        self.load()
        pass
