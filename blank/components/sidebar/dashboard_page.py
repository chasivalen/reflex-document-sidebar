import reflex as rx
from .state import State
from .breadcrumb import breadcrumb
def dashboard_page():
    return rx.box(
        rx.hstack(
            rx.button(
                rx.icon("menu"),
                on_click=State.toggle_sidebar,
                variant="ghost",
            ),
            rx.divider(orientation="vertical", height="1em"),
            breadcrumb(),
            padding="1em",
            border_bottom="1px solid #eaeaea",
        ),
        rx.box(
            rx.grid(
                rx.box(height="200px", bg="gray.100", border_radius="xl"),
                rx.box(height="200px", bg="gray.100", border_radius="xl"),
                rx.box(height="200px", bg="gray.100", border_radius="xl"),
                columns=rx.breakpoints(initial="1",sm="3"),
                spacing="4",
            ),
            rx.box(
                height=rx.breakpoints(initial="100vh", sm="auto"),
                min_height=rx.breakpoints(initial="auto", sm="300px"),
                bg="gray.100",
                border_radius="xl",
                margin_top="1em",
            ),
            padding="1em",
        ),
        margin_left=rx.cond(State.sidebar_open, "300px", "0px"),
        transition="margin-left 0.3s",
        width="100%",
        height="calc(100vh - 20px)",
        max_height="100vh",
        overflow_y="auto",
    )
