import pandas as pd


class DataManager:
    def __init__(self):
        self.data_list = []
        self.data_name_dict = {}

    def add_data(self, data):
        self.data_list.append(data)
        self.data_name_dict.update({data.get_name(): len(self.data_list) - 1})
        return

    def get(self):
        return self.data_list[0].get()

    def get_data_obj(self):
        return self.data_list[0]

    def get_byname(self, name):
        return self.data_list[self.data_name_dict[name]].get()

    def get_data_obj_byname(self, name):
        return self.data_list[self.data_name_dict[name]]

    def map_value(self, value, data_map):
        search = "key==" + str(value)
        val = data_map.query(search)
        return val
        # return data_map.query(value)[1]

    def get_data_dict(self):
        return self.data_name_dict

    def map_transform(self, data_in, data_map):

        data_out = None


        if isinstance(data_map, pd.DataFrame):
            print("data_map is data frame")

            data_map_dict = dict(zip(data_map.iloc[:,0], data_map.iloc[:, 1]))
        else:
            print("data_map is already dict")
            data_map_dict = data_map

        print(data_map_dict)
        if isinstance(data_in, pd.Series):
            data_out = data_in.map(data_map_dict)
        elif isinstance(data_in, pd.DataFrame):
            data_out = data_in.applymap(self.map_value)

        return data_out
