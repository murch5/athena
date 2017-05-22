from datatypes.data import Data
import os as os
import pandas as pd




class Table(Data):



    def __init__(self):
        Data.__init__(self)

    def load(self):

        ext = os.path.splitext(self.filename)[1]

        if ext == ".csv":
            self.data = pd.read_csv(self.filename, sep=",")

        elif ext == ".tsv":
            self.data = pd.read_table(self.filename)
        elif ext == ".xls" or ext == ".xlsx":
            self.data = pd.read_excel(self.filename)

        return

    def filter(self,process_XML):

        return

    def extract(self,process_XML):
        return

    def subset(self,process_XML):
        return

    processing_type = {"filter": filter, "extract": extract, "subset": subset}





