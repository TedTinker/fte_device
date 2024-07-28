from custom_window import CustomWindow
import pygame_gui
import pygame
import json



class ZoneWindow(CustomWindow):
    def __init__(self, manager, name="Zone", label="Zone", position=(100, 100), size=(300, 200)):
        super().__init__(manager, name, label, position, size)
        # Additional initialization for ZoneWindow if needed

    def load(self, data):
        self.name_entry.set_text(data['name'])
        self.label = data['label']
        # Load any additional data specific to ZoneWindow