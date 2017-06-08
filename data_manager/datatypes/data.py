import os as os

import logging as logging
logger = logging.getLogger(__name__)

class Data:

    def load(self):
        return

    def evaluate_process_stack(self):

        self.data = self.process_manager.pass_thru_stack(self.data)
        logger.debug("------ Processed data shape: " + str(self.data.shape))
        pass

    def get(self):
        return self.data

    def set_process_manager(self, process_manager):
        self.process_manager = process_manager
        pass

    def set_filename(self, filename):
        self.filename = filename
        self.file_ext = os.path.splitext(self.filename)[1][1:]

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __init__(self):
        self.name = None
        self.filename = None
        self.file_ext = None
        self.data = None
        self.processing_stack = None
        self.type = None

        self.processing_type = {}

        self.process_manager = None
        return
