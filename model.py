""" models for app"""
from repository import JsonRepository
######Input Divace##########
class InputDevice:
    """Input device class"""
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.repository = JsonRepository()

class Mouse(InputDevice):
    """Mouse class"""
    def __init__(self, name, brand ):
        super().__init__(name, brand)
        self.id = 0;
        self.units = 0;

    def save_mouse(self):
        data ={
            "name": self.name,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.repository.add(data)
    
    def update_mouse(self, new_name=None, new_brand=None, new_units=None):
        old_data = {
            "name": self.name,
            "brand": self.brand
        }
        if new_name:
            old_data["name"] = self.name
        if new_brand:
            old_data["brand"] = self.brand
        if new_units is not None:
            self.units = new_units

        new_data = {
            "name": old_data["name"],
            "brand": old_data["brand"],
            "id": self.id,
            "units": self.units
        }
        self.repository.update(old_data, new_data)
        
    def list_mouse(self):
        return self.repository.list()
    
    def delete_mouse(self):
        data = {
            "id": self.id,
        }
        self.repository.delete(data)
        
    def search_mouse(self):
        data = {
            "id": self.id,
        }
        return self.repository.search(data)
    
    
class keyboard(InputDevice):
    """Keyboard class"""
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.id = 0;
        self.units = 0;
        
    def save_keyboard(self):
        data ={
            "name": self.name,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.repository.add(data)
    
    def update_keyboard(self, new_name=None, new_brand=None, new_units=None):
        old_data = {
            "name": self.name,
            "brand": self.brand
        }
        if new_name:
            old_data["name"] = self.name
        if new_brand:
            old_data["brand"] = self.brand
        if new_units is not None:
            self.units = new_units

        new_data = {
            "name": old_data["name"],
            "brand": old_data["brand"],
            "id": self.id,
            "units": self.units
        }
        self.repository.update(old_data, new_data)
        
    def list_keyboard(self):
        return self.repository.list()
    
    def delete_keyboard(self):
        data = {
            "id": self.id
        }
        self.repository.delete(data)
        
    def search_keyboard(self, data):
        data = {
            "id": self.id
        }
        return self.repository.search(data)
    
#########Output Divace###### 
class OutputDevice: 
    """Output device class"""
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.repository = JsonRepository()   

class Monitor(OutputDevice):
    """Monitor class"""
    def __init__(self, name, brand):
        super().__init__(name,brand)
        self.id = 0;
        self.units = 0;

    def save_monitor(self):
        data ={
            "name": self.name,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.repository.add(data)
    
    def update_monitor(self, new_name=None, new_brand=None, new_units=None):
        old_data = {
            "name": self.name,
            "brand": self.brand
        }
        if new_name:
            old_data["name"] = self.name
        if new_brand:
            old_data["brand"] = self.brand
        if new_units is not None:
            self.units = new_units

        new_data = {
            "name": old_data["name"],
            "brand": old_data["brand"],
            "id": self.id,
            "units": self.units
        }
        self.repository.update(old_data, new_data)
        
    def list_monitor(self):
        return self.repository.list()
    
    def delete_monitor(self):
        data = {
            "id": self.id,
        }
        self.repository.delete(data)
        
    def search_monitor(self):
        data = {
            "id": self.id,
        }
        return self.repository.search(data)
        
class Speaker(OutputDevice):
    """Speaker class"""
    def __init__(self, name, brand):
        super().__init__(name,brand)
        self.id = 0;
        self.units = 0;
    
    def save_speaker(self):
        data ={
            "name": self.name,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.repository.add(data)
    
    def update_speaker(self, new_name=None, new_brand=None, new_units=None):
        old_data = {
            "name": self.name,
            "brand": self.brand
        }
        if new_name:
            old_data["name"] = self.name
        if new_brand:
            old_data["brand"] = self.brand
        if new_units is not None:
            self.units = new_units

        new_data = {
            "name": old_data["name"],
            "brand": old_data["brand"],
            "id": self.id,
            "units": self.units
        }
        self.repository.update(old_data, new_data)
        
    def list_speaker(self):
        return self.repository.list()
    
    def delete_speaker(self):
        data = {
            "id" : self.id
        }
        self.repository.delete(data)
        
    def search_speaker(self):
        data = {
            "id":self.id,
        }
        return self.repository.search(data) 

class Computer:
    def __int__(self, name, brand, mouse, keyboard, monitor, speaker):
        self.name = name
        self.brand = brand
        self.mouse = mouse
        self.keyboard = keyboard
        self.monitor = monitor
        self.speaker = speaker
        self.id = 0;
        self.units = 0;
        self.repository = JsonRepository()
        
    def save_computer(self):
        data = {
        "name": self.name,
        "brand": self.brand,
        "mouse": {
            "name": self.mouse.name,
            "brand": self.mouse.brand,
            "id": self.mouse.id,
            "units": self.mouse.units
        },
        "keyboard":{
            "name": self.keyboard.name,
            "brand": self.keyboard.brand,
            "id": self.keyboard.id,
            "units": self.keyboard.units
        },
        "monitor":{
            "name": self.monitor.name,
            "brand": self.monitor.brand,
            "id": self.monitor.id,
            "units": self.monitor.units
        },
        "speaker":{
            "name": self.speaker.name,
            "brand": self.speaker.brand,
            "id": self.speaker.id,
            "units": self.speaker.units
        },
        "id": self.id,
        "units": self.units
        
        }
        return self.repository.add(data)
    def update_computer(self, new_name=None, new_brand=None, new_mouse=None, new_keyboard=None, new_monitor=None, new_speaker=None, new_units=None):
        old_data = {
            "name": self.name,
            "brand": self.brand,
            "mouse": {
                "name": self.mouse.name,
                "brand": self.mouse.brand,
                "id": self.mouse.id,
                "units": self.mouse.units
            },
            "keyboard": {
                "name": self.keyboard.name if self.keyboard else None,
                "brand": self.keyboard.brand if self.keyboard else None,
                "id": self.keyboard.id if self.keyboard else None,
                "units": self.keyboard.units if self.keyboard else None
            },
            "monitor": {
                "name": self.monitor.name if self.monitor else None,
                "brand": self.monitor.brand if self.monitor else None,
                "id": self.monitor.id if self.monitor else None,
                "units": self.monitor.units if self.monitor else None
            },
            "speaker": {
                "name": self.speaker.name if self.speaker else None,
                "brand": self.speaker.brand if self.speaker else None,
                "id": self.speaker.id if self.speaker else None,
                "units": self.speaker.units if self.speaker else None
            },
            "units": self.units
            
        }

        if new_name:
            old_data["name"] = new_name
        if new_brand:
            old_data["brand"] = new_brand
        if new_mouse:
            old_data["mouse"] = {
                "name": new_mouse.name,
                "brand": new_mouse.brand,
                "id": new_mouse.id,
                "units": new_mouse.units
            }
        if new_keyboard:
            old_data["keyboard"] = {
                "name": new_keyboard.name,
                "brand": new_keyboard.brand,
                "id": new_keyboard.id,
                "units": new_keyboard.units
            }
        if new_monitor:
            old_data["monitor"] = {
                "name": new_monitor.name,
                "brand": new_monitor.brand,
                "id": new_monitor.id,
                "units": new_monitor.units
            }
        if new_speaker:
            old_data["speaker"] = {
                "name": new_speaker.name,
                "brand": new_speaker.brand,
                "id": new_speaker.id,
                "units": new_speaker.units
            }
        if new_units:
            old_data["units"] = new_units

        new_data = {
            "name": old_data["name"],
            "brand": old_data["brand"],
            "mouse": old_data["mouse"],
            "keyboard": old_data["keyboard"],
            "monitor": old_data["monitor"],
            "speaker": old_data["speaker"],
            "units" : old_data["units"]
            
        }
        self.repository.update(old_data, new_data)
        
    def list_computer(self):
        return self.repository.list()
    
    def delete_computer(self):
        data = {
            "id": self.id
        }
        self.repository.delete(data)
        
    def search(self):
        data = {
            "id":self.id
        }
        return self.repository.search(data)