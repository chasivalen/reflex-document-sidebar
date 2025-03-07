"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.sidebar import sidebar, dashboard_page

# Main app
def index():
    return rx.box(
        sidebar(),
        dashboard_page(),
        width="100%",
        height="100%",
        min_height="100vh",
        overflow="hidden",
    )



# Create the app
app = rx.App()
app.add_page(index)
