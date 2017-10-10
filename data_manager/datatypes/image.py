import matplotlib.pyplot as plt

from data_manager.datatypes.data import Data

import json as json

import logging as logging
logger = logging.getLogger(__name__)

import scipy as scipy
import skimage.io as skimage_io
import skimage.external.tifffile as tff

class Image(Data):

    def load(self):


        if self.ext == "tif":

            #self.data = skimage_io.imread(self.file_name,plugin="tifffile")

            with tff.TiffFile(self.path) as tiff:
                for tiff_page in tiff:
                    pass
                    #print(tiff_page.page_name)
                self.data = tiff.asarray()

                self.metadata = tiff[0].image_description
                self.info = tiff[0].info()


            #logging.debug(self.info)

        self.axes = self.data.shape

        logging.debug("---Image data: Shape - " + str(self.data.shape))

        return

