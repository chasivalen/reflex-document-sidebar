import reflex as rx
from . import data
# Define the app state
class State(rx.State):
    sidebar_open: bool = True
    selected_version: str = data["versions"][0]
    selected_menu_item: str = "Data Fetching"  # Default selected item
    
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open
    
    def set_version(self, version: str):
        self.selected_version = version
        
    def set_selected_menu_item(self, item_title: str):
        self.selected_menu_item = item_title
