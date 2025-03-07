import reflex as rx 
from .state import State
def breadcrumb(is_current: bool = True):
    return rx.hstack(
        rx.link(
            "Building Your Application", href="#",
        ),
        rx.icon("chevron-right", size=20),
        rx.link(State.selected_menu_item,  href="#", color_scheme=rx.cond(is_current, "red", "gray")
        ),
        spacing="1",
        align="center"
    )
