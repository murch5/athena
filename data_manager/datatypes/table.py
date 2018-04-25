import pandas as pd

from data_manager.datatypes.data import Data

import logging as logging
logger = logging.getLogger(__name__)


class Table(Data):

    def load(self):

        if self.mimetype == "text/csv":
            self.data = pd.read_csv(self.path, sep=",", header=0)
        elif self.mimetype == "tsv":
            self.data = pd.read_table(self.path)
        elif self.mimetype == "xls" or self.mimetype == "xlsx":
            self.data = pd.read_excel(self.path)
        elif self.mimetype == "stream":
            self.data = pd.read_json(self.path, orient="split")

        return

    def get_index_labels(self, axis):
        labels = []
        if axis == 0:
            labels = list(self.data.index)
        elif axis == 1:
            labels = self.data.columns.values.tolist()

        return labels





