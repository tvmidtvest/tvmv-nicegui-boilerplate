import os
from contextlib import contextmanager

import config
from nicegui import ui


@contextmanager
def frame():
    with ui.element("div").classes("text-center w-full"):
        url = "/"
        ui.button(icon="home", on_click=lambda: ui.open(url)).props(
            "color=secondary round"
        )
    with ui.element("div").classes("text-center w-full md:w-1/2 mx-auto"):
        yield
