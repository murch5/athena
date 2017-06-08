import matplotlib.pyplot as plt

from data_manager.datatypes.data import Data

import logging as logging
logger = logging.getLogger(__name__)

import scipy as scipy
import skimage.io as skimage_io


class Image(Data):

    def load(self):

        if self.file_ext == "tif":
            self.data = skimage_io.imread(self.filename,plugin="tifffile")

        self.axes = self.data.shape

        logger.debug("---Image data: Shape - " + str(self.data.shape))

        return

    def __init__(self):
        Data.__init__(self)
        self.type = "image"
        self.axes = None

        return
