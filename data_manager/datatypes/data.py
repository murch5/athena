import os as os


class Data:
    def __init__(self):
        self.name = None
        self.filename = None
        self.file_ext = None
        self.data = None
        self.processing_XML = None

        return

    def load(self):
        return

    def processing(self, processing_XML):
        self.processing_XML = processing_XML

        for process in self.processing_XML:
            self.process(process)

    processing_type = {}

    def get(self):
        return self.data

    def set_filename(self, filename):
        self.filename = filename
        self.file_ext = os.path.splitext(self.filename)[1][1:]

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def process(self, process_XML):
        process_type = process_XML.tag
        self.processing_type[process_type](self, process_XML)

        return

    def parse_process(self, process_type, process_XML):
        self.processing_type[process_type](self, process_XML)
        return

    @staticmethod
    def checkXML(process_XML, xml):
        check = False
        if process_XML.find(xml) is not None:
            check = True
        else:
            check = False

        return check

    @staticmethod
    def getXMLvalue(process_XML, xml):
        data = process_XML.find(xml)
        data_type = data.attrib["data_type"]
        value = None
        if data_type in ["int", "i"]:
            value = int(data.text)
        elif data_type in ["float", "f"]:
            value = float(data.text)
        elif data_type in ["bool", "b"]:
            value = bool(data.text)
        elif data_type in ["str", "s"]:
            value = str(data.text)
        elif data_type in ["list_index", "li"]:
            value = [int(x) for x in data.text.split(",")]
        elif data_type in ["range_index", "ri"]:
            value = [int(x) for x in data.text.split("-")]
        elif data_type in ["axis_name", "axis"]:
            value = [str(x) for x in data.text.split(",")]

        else:
            value = str(data.text)

        return value
