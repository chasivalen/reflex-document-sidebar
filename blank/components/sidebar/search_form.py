import reflex as rx

def search_form():
    return rx.form(
        rx.hstack(
            rx.icon("search", color="gray"),
            rx.input(
                placeholder="Search the docs...",
                width="100%",
                padding_left="2em",
            ),
            position="relative",
        ),
        width="100%",
    )