from data_manager.datatypes.data import Data
import pandas as pd

class GFF3(Data):

    def load(self):

        temp_data = pd.read_table(self.file_name, comment="#", header=None)

        temp_data.columns = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]

        attributes = []

        for x in temp_data["attribute"]:

            attr_set = []
            attribute = x.split(";")

            for y in attribute:
                newAttribute = y.split("=")

                attr_set.append(newAttribute)

            attrDict = dict(attr_set)

            attributes.append(attrDict)

        temp_data["attrDict"] = attributes

        pass

    def getChain(self, chainName):

        searchQuery = "feature=='" + chainName + "'"
        chainData = self.GFFdata.ix(searchQuery)[0]
        start = chainData["start"]
        end = chainData["end"]
        chain = [start, end]

        return chain

    def getFeature(self, featureName):

        searchQuery = "feature=='" + featureName + "'"
        featureData = self.GFFdata.query(searchQuery)

        return featureData

    def getData(self):
        return self.GFFdata

    def getDictValues(self, dictKey):

        labels = []
        for x in self.GFFdata["attrDict"]:
            labels.append(x.get(dictKey))

        return labels

    def setLabels(self, newLabels):
        self.currLabels = newLabels
        return
