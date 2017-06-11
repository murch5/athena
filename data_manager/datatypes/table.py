import pandas as pd

from data_manager.datatypes.data import Data

import logging as logging
logger = logging.getLogger(__name__)


class Table(Data):

    def load(self):

        if self.file_ext == "csv":
            self.data = pd.read_csv(self.file_name, sep=",",header=0)


        elif self.file_ext == "tsv":
            self.data = pd.read_table(self.file_name)
        elif self.file_ext == "xls" or self.file_ext == "xlsx":
            self.data = pd.read_excel(self.file_name)

        return

    def get_index_labels(self, axis):
        labels = []
        if axis == 0:
            labels = list(self.data.index)
        elif axis == 1:
            labels = self.data.columns.values.tolist()

        t = pd.DataFrame(labels)
        t.to_csv("test3.csv",index=False)
        return labels





