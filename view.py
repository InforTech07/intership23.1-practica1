""" view application"""

# from controller import MouseController, KeyBoardController, MonitorController, SpeakerController, ComputerController
from controller import MouseController

class IndexView:
    def __init__(self) -> None:
        self.mouse_ctl = MouseController()

    def new_order(self):
        new_mouse = self.mouse_ctl.create_mouse("mouse 3", "brand 3")
        print(new_mouse.name)

    def list_mouse(self):
        mouses = self.mouse_ctl.list_mouse()
        print(mouses)
    
    def update_mouse(self):
        mouse = self.mouse_ctl.update_mouse("mouse 4", "brand 4")
        print(mouse)

    def delete_mouse(self):
        mouse = self.mouse_ctl.delete_mouse(self.id)
        print("delete")

    def find_mouse(self, data):
        mouses = self.mouse_ctl.find_mouse(data)
        print(mouses)

if __name__ == "__main__":
    index_view = IndexView()
    index_view.new_order()
    index_view.list_mouse()

# mouse
# keyboard
# monitor 
# speaker
# computer