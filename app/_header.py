import os

import config
from nicegui import ui


def content():
    with ui.element("div").classes("text-center w-full"):
        url = "/"
        ui.button(icon="home", on_click=lambda: ui.open(url)).props(
            "color=secondary round"
        )
