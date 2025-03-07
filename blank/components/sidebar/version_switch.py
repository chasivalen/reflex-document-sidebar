import reflex as rx
from .state import State
from . import data

def version_switcher():
    return rx.menu.root(
        rx.menu.trigger(
            rx.hstack(
                rx.box(
                    rx.icon("gallery-vertical-end", size=16),
                    bg="blue.500",
                    color="white",
                    border_radius="lg",
                    padding="2",
                    aspect_ratio="1/1",
                ),
                rx.vstack(
                    rx.text("Documentation", font_weight="semibold"),
                    rx.text(f"v{State.selected_version}", font_size="sm"),
                    align_items="flex-start",
                    spacing="0",
                ),
                rx.spacer(),
                rx.icon("chevron-down"),
                width="100%",
            ),
            width="100%",
        ),
        rx.menu.content(
            *[
                rx.menu.item(
                    rx.hstack(
                        rx.text(f"v{version}"),
                        rx.spacer(),
                        rx.cond(
                            State.selected_version == version,
                            rx.icon("check"),
                            rx.text(""),
                        ),
                    ),
                    on_click=lambda v=version: State.set_version(v),
                )
                for version in data["versions"]
            ],
            width="100%"
        ),
        width="100%",
    )