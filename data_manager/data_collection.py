import data_manager as dm
import data_manager.datatypes as dt
import os as os
import sys as sys
import xml.etree.ElementTree as et
import io_util as io_util

import logging as logging

logger = logging.getLogger(__name__)


class DataCollection:

    def __init__(self):
        self.data_handler = dm.DataManager(dm)
        self.data_XML = None

        pass

    def load_data(self, input):

        logger.debug("Loading data from input: " + str(input))

        def create_data_record(path):

            data_record_new = {}

            file_name = io_util.path_util.get_name_from_path(path)
            mimetype = io_util.path_util.check_file_mime(path)
            type = dt.datatype_map.get(mimetype)
            base_name, ext = file_name.split(".", 1)

            data_record_new.update({"data": {"name": base_name, "type": type, "path": path, "mimetype": mimetype,
                                             "ext": ext, "file_name_full": file_name}})

            logger.debug("New data record: " + str(data_record_new))

            return data_record_new

        def create_buffer_record(buffer):

            data_record_new = {}

            name = "std_in"
            mimetype = "stream"
            type = "Table"
            base_name = "default"
            ext = None

            data_record_new.update({"data": {"name": base_name, "type": type, "path": buffer, "mimetype": mimetype,
                                             "ext": ext}})

            logger.debug("New buffer record: " + str(data_record_new))

            return data_record_new

        if isinstance(input, list):

            logger.debug("Input list detected")

            root = et.Element("root")
            self.data_XML = et.ElementTree(root)

            for file in input:
                print(file)
                data_record = create_data_record(file)
                print(data_record)
                data_XML_file = io_util.xml_parse.dict_to_xml(data_record)
                print("test")
                root.append(data_XML_file.getroot())

            pass
        elif isinstance(input, str):

            if os.path.exists(input):
                if os.path.isdir(input):
                    pass
                elif os.path.isfile(input):

                    data_record = create_data_record(input)

                    if data_record.get("data").get("mimetype") == "application/xml":

                        self.data_XML = et.parse(input)

                        for data_entry in self.data_XML.iterfind(".//data"):
                            path = data_entry.findtext("path")
                            data_record_new = create_data_record(path)
                            mime_type = et.Element("mimetype")
                            mime_type.text = data_record_new.get("data").get("mimetype")
                            data_entry.append(mime_type)

                        logger.debug("Data format: XML")

                    else:
                        self.data_XML = io_util.xml_parse.dict_to_xml(data_record)
                        logger.debug("Data format: single file")
                        print(data_record)

                pass
            elif input == "stdin":
                logger.debug("Data format: stdin")
                data_record = create_buffer_record(sys.stdin)
                logger.debug(data_record)
                data_record_dict = data_record.get("data")
                self.data_handler.add(data_record_dict.get("type"), data_record_dict)
                pass

        if input != "stdin":
            self.data_handler.populate_from_xml(self.data_XML.iterfind(".//data"), nested_type=".//type")

        logger.debug("Lazy loading data structures from XML...")

        self.data_handler.call_all("load")

        pass

    def get_data_dict(self):

        data_dict = {}

        name_datasets = self.data_handler.get_all("name")
        data_datasets = self.data_handler.get_all("data")

        data_dict = dict(zip(name_datasets, data_datasets))

        return data_dict

    def add_path_to_xml(self, xml, file_list):

        file_list_dict = {}

        for file in file_list:
            filename, ext = os.path.splitext(os.path.basename(file))
            file_list_dict.update({filename: [ext, file]})

        for dataset in xml.iterfind("dataset"):
            dataset_name = dataset.findtext("name")
            file_path = et.Element("path")
            file_path.text = file_list_dict.get(dataset_name)[1]
            file_ext = et.Element("ext")
            file_ext.text = file_list_dict.get(dataset_name)[0][1:]
            dataset.insert(0, file_path)
            dataset.insert(0, file_ext)

        return xml

    def get_data_manager(self):
        return self.data_handler
