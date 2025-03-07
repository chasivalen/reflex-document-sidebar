import reflex as rx
from . import data
from .search_form import search_form
from .sidebar_group import sidebar_group
from .version_switch import version_switcher
from .state import State

def sidebar():
    return rx.box(
        rx.vstack(
            rx.vstack(
                version_switcher(),
                search_form(),
                padding="1em",
                width="100%",
                spacing="3",
            ),
            rx.accordion.root(
                *[sidebar_group(group) for group in data["nav_main"]],
                allow_multiple=True,
                default_index=[0, 1, 2, 3],  # All expanded by default
                width="100%",
                variant="ghost",
                color_scheme="gray",
                type="multiple",
            ),
            align_items="stretch",
            height="100%",
            width="100%",
            spacing="0",
            overflow_y="auto",
        ),
        height="100vh",
        width=rx.cond(State.sidebar_open, "300px", "0px"),
        transition="width 0.3s",
        overflow="hidden",
        position="fixed",
        top="0",
        left="0",
        bg="white",
        z_index="999",
    )