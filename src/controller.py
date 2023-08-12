""" controller for the application"""
from model import Mouse
from model import Keyboard
from model import Monitor
from model import Speaker

from repository import JsonRepository

# Input Devices
class MouseController:
    def __init__(self) -> None:
        self.respository = JsonRepository()
        self.id = 0
        self.input_devices =  "input_devices"
        self.mouses = "mouses"

    def get_mouses(self):
        mouses = self.respository.get_all(self.input_devices, self.mouses)
        return mouses

    def create_mouse(self, name, brand):
        self.id+=1 
        mouse = Mouse(name, brand)
        mouse.id = self.id
        self.respository.add(mouse.__dict__, self.input_devices, self.mouses)
        return "Created successfully!"

    def get_mouse(self, id):
        mouse = self.respository.get(id, self.input_devices, self.mouses)
        return mouse

    def update_mouse(self, id, name, bread):
        self.respository.update(id, name, bread, self.input_devices, self.mouses)
        return "Updated succesfully!"

    def delete_mouse(self, id):
        self.respository.delete(id, self.input_devices, self.mouses)
        return "Deleted successfully!"
    
class KeyboardController:
    def __init__(self) -> None:
        self.respository = JsonRepository()
        self.id = 0
        self.input_devices =  "input_devices"
        self.keyboards = "keyboards"

    def get_keyboards(self):
        keyboards = self.respository.get_all(self.input_devices, self.keyboards)
        return keyboards

    def create_keyboard(self, name, brand):
        self.id+=1 
        keyboard = Keyboard(name, brand)
        keyboard.id = self.id
        self.respository.add(keyboard.__dict__, self.input_devices, self.keyboards)
        return "Created successfully!"

    def get_keyboard(self, id):
        keyboard = self.respository.get(id, self.input_devices, self.keyboards)
        return keyboard

    def update_keyboard(self, id, name, bread):
        self.respository.update(id, name, bread, self.input_devices, self.keyboards)
        return "Updated succesfully!"

    def delete_keyboard(self, id):
        self.respository.delete(id, self.input_devices, self.keyboards)
        return "Deleted successfully!"

# Output Devices
class MonitorController:
    def __init__(self) -> None:
        self.respository = JsonRepository()
        self.id = 0
        self.output_devices =  "output_devices"
        self.monitors = "monitors"

    def get_monitors(self):
        monitors = self.respository.get_all(self.output_devices, self.monitors)
        return monitors

    def create_monitor(self, name, brand):
        self.id+=1 
        monitor = Monitor(name, brand)
        monitor.id = self.id
        self.respository.add(monitor.__dict__, self.output_devices, self.monitors)
        return "Created successfully!"

    def get_monitor(self, id):
        monitor = self.respository.get(id, self.output_devices, self.monitors)
        return monitor

    def update_monitor(self, id, name, bread):
        self.respository.update(id, name, bread, self.output_devices, self.monitors)
        return "Updated succesfully!"

    def delete_monitor(self, id):
        self.respository.delete(id, self.output_devices, self.monitors)
        return "Deleted successfully!"

class SpeakerController:
    def __init__(self) -> None:
        self.respository = JsonRepository()
        self.id = 0
        self.output_devices =  "output_devices"
        self.speakers = "speakers"

    def get_speakers(self):
        speakers = self.respository.get_all(self.output_devices, self.speakers)
        return speakers

    def create_speaker(self, name, brand):
        self.id+=1 
        speaker = Speaker(name, brand)
        speaker.id = self.id
        self.respository.add(speaker.__dict__, self.output_devices, self.speakers)
        return "Created successfully!"

    def get_speaker(self, id):
        speaker = self.respository.get(id, self.output_devices, self.speakers)
        return speaker

    def update_speaker(self, id, name, bread):
        self.respository.update(id, name, bread, self.output_devices, self.speakers)
        return "Updated succesfully!"

    def delete_speaker(self, id):
        self.respository.delete(id, self.output_devices, self.speakers)
        return "Deleted successfully!"