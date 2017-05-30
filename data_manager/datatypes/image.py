import matplotlib.pyplot as plt

from data_manager.datatypes.data import Data


class Image(Data):
    def __init__(self):
        Data.__init__(self)

        return

    def load(self):
        if self.file_ext == "tif":
            self.data = plt.imread(self.filename)

        return

    processing_type = {}

    def parse_process(self, process_type, process_XML):
        self.processing_type[process_type](self, process_XML)
        return
