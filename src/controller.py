""" controller for the application"""
from model import Mouse
from model import Keyboard
from model import Monitor
from model import Speaker

from repository import JsonRepository

# Input Devices
class MouseController:
    def __init__(self) -> None:
        self.mouse_model = Mouse()

    def list_mouse(self):
        mouses = self.mouse_model.list_mouse()
        return mouses

    def create_mouse(self, name, brand, units):
        mouse = self.mouse_model.Mouse(name, brand, units)
        msg = mouse.save_mouse()
        return msg

    def search_id(self, id):
        mouse = self.mouse_model.search_id(id)
        return mouse

    def update_mouse(self, id, name, bread, units):
        msg = self.mouse_model.update_mouse(id, name, bread, units)
        return msg

    def delete(self, id):
        msg = self.mouse_model.delete(id)
        return msg
    
class KeyboardController:
    def __init__(self) -> None:
        self.keyboard_model = Keyboard()

    def get_keyboards(self):
        keyboards = self.keyboard_model.list_keyboard()
        return keyboards

    def create_keyboard(self, name, brand, units):
        keyboard = Keyboard(name, brand, units)
        msg = keyboard.save_mouse()
        return msg

    def get_keyboard(self, id):
        keyboard = self.keyboard_model.search_id(id)
        return keyboard

    def update_keyboard(self, id, name, bread):
        msg = self.keyboard_model.update_mouse(id, name, bread)
        return msg

    def delete_keyboard(self, id):
        msg = self.keyboard_model.delete(id)
        return msg

# Output Devices
class MonitorController:
    def __init__(self) -> None:
        self.mouse_model = JsonRepository()

    def get_monitors(self):
        monitors = self.mouse_model.list_keyboard()
        return monitors

    def create_monitor(self, name, brand, units):
        self.id+=1 
        monitor = Monitor(name, brand, units)
        monitor.id = self.id
        msg = self.mouse_model.save_keyboard()
        return msg

    def get_monitor(self, id):
        monitor = self.mouse_model.search_id(id)
        return monitor

    def update_monitor(self, id, name, bread, units):
        self.mouse_model.update_mouse(id, name, bread, units)
        return "Updated succesfully!"

    def delete_monitor(self, id):
        self.mouse_model.delete(id, )
        return "Deleted successfully!"

class SpeakerController:
    def __init__(self) -> None:
        self.speaker_model = Speaker()

    def get_speakers(self):
        speakers = self.speaker_model.list_speaker()
        return speakers

    def create_speaker(self, name, brand):
        self.id+=1 
        speaker = Speaker(name, brand)
        speaker.id = self.id
        msg = self.speaker_model.save_speaker()
        return msg

    def get_speaker(self, id):
        speaker = self.speaker_model.search_id(id)
        return speaker

    def update_speaker(self, id, name, bread, units):
        msg = self.speaker_model.update_speaker(id, name, bread, units)
        return msg

    def delete_speaker(self, id):
        msg = self.speaker_model.delete(id)
        return msg