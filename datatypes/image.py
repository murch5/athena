from datatypes.data import Data
import os as os
import pandas as pd

class Image(Data):

    def __init__(self):
        Data.__init__(self)
        self.filename = None
        self.data = None

        return

    def load(self):
        return