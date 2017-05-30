import pandas as pd

from data_manager.datatypes.data import Data


class Table(Data):
    def __init__(self):
        Data.__init__(self)

    def load(self):

        if self.file_ext == "csv":
            self.data = pd.read_csv(self.filename, sep=",",header=0)


        elif self.file_ext == "tsv":
            self.data = pd.read_table(self.filename)
        elif self.file_ext == "xls" or self.file_ext == "xlsx":
            self.data = pd.read_excel(self.filename)

        return

    def filter(self, process_XML):

        return

    def extract(self, process_XML):
        return

    def subset(self, process_XML):

        axis = 0
        subset = 0

        if self.checkXML(process_XML, ".//axis"):
            axis = self.getXMLvalue(process_XML, ".//axis")
        if self.checkXML(process_XML, ".//set"):
            subset = self.getXMLvalue(process_XML, ".//set")

        if axis in ["col", "c"]:
            self.data = self.data.ix[subset]
        elif axis in ["row", "r"]:
            self.data = self.data.ix[:, subset]

        return

    def groupby_value(self, process_XML):

        delim_flag = "False"
        if self.checkXML(process_XML, ".//delim"):
            delim_flag = self.getXMLvalue(process_XML, ".//delim")

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

    processing_type = {"filter": filter, "extract": extract, "subset": subset, "groupby_val": groupby_value}

    def parse_process(self, process_type, process_XML):
        self.processing_type[process_type](self, process_XML)
        return
