import pandas as pd

from data_manager.datatypes.data import Data

import logging as logging
logger = logging.getLogger(__name__)


class Table(Data):

    def load(self):

        if self.file_ext == "csv":
            self.data = pd.read_csv(self.filename, sep=",",header=0)


        elif self.file_ext == "tsv":
            self.data = pd.read_table(self.filename)
        elif self.file_ext == "xls" or self.file_ext == "xlsx":
            self.data = pd.read_excel(self.filename)

        return

    def filter(self, process_settings):

        return

    def extract(self, process_settings):
        return

    def subset(self, process_settings):

        axis = 0
        subset = 0

        if process_settings.get("axis"):
            axis = process_settings.get("axis")
        if process_settings.get("set"):
            subset = process_settings.get("set")

        if axis in ["col", "c"]:
            self.data = self.data.ix[subset]
        elif axis in ["row", "r"]:
            self.data = self.data.ix[:, subset]

        return

    def groupby_value(self, process_settings):

        delim_flag = "False"
        if process_settings.get("delim"):
            delim_flag = process_settings.get("delim")

        if delim_flag == "True":
            self.data = self.data.str.split(";").apply(pd.Series, 1).stack()

        self.data = self.data.groupby(self.data.iloc[:, 0]).size()
        self.data.columns = ["Index", "GroupedCounts"]

    def get_index_labels(self, axis):
        labels = []
        if axis == 0:
            labels = list(self.data.index)
        elif axis == 1:
            labels = self.data.columns.values.tolist()

        t = pd.DataFrame(labels)
        t.to_csv("test3.csv",index=False)
        return labels

    def __init__(self):
        Data.__init__(self)
        self.type = "table"




