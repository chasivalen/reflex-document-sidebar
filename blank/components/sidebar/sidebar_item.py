import reflex as rx
from .state import State


def sidebar_menu_item(title, url, is_active=False):
    return rx.link(
        rx.box(
            title,
            padding="0.5em 1em",
            border_left =rx.cond(
                State.selected_menu_item == title, 
                "1px solid blue",
                "1px solid #E0E0E0"),
            border_radius="none",
            color=rx.cond(
                State.selected_menu_item == title, 
                "#113264", 
                "inherit"
            ),
            _hover={"bg": rx.cond(
                State.selected_menu_item == title, 
                "#8EC8F6", 
                "#E0E0E0"
            )},
            width="100%",
        ),
        href=url,
        width="100%",
        on_click=lambda: State.set_selected_menu_item(title),
    )
