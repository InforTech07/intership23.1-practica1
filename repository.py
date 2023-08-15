""" respository json"""

import json

class JsonRepository:
    """ JsonRepository """

    def __init__(self):
        self.filename = "data.json"
    

    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file)


    def read(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data
    

    def add(self, data):
        data_list = self.read()
        data_json=json.dumps(data) #Convert python object to json
        data_list.append(data_json)
        self.write(data_list)
        

    def update(self,old_data,new_data):
        data_list=self.read()

        if old_data in data_list:
            index = data_list.index(old_data)  #Find the index of the data to be updated
            data_list[index] = new_data
            self.write(data_list)


    def list(self):
        data_list=self.read()
        return data_list
    

    def delete(self, data_id):
        data_list = self.read()

        for data in data_list:
            if data.get("id") == data_id:
                data_list.remove(data)
                self.write(data_list)
                return True
        
        return False

    

    def search_id(self,data_id):
        data_list = self.read()

        for data in data_list:
            if data.get("id") == data_id:
                return data
            
        return  "id not found"


    

    