

class Data():

    def __init__(self):
        self.name = None
        self.filename = None
        self.data = None
        self.processing_XML = None


        return

    def load(self):
        return

    def processing(self, processing_XML):
        self.processing_XML = processing_XML

        processing_steps = self.processing_XML.findall(".//")

        for process in processing_steps:
            self.process(process)

    processing_type = {}

    def get(self):
        return self.data

    def set_filename(self,filename):
        self.filename = filename

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def process(self, process_XML):
        process_type = process_XML.tag
        self.processing_type[process_type](self,process_XML.findall(".//"))

        return
