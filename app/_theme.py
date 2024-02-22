import os
from contextlib import contextmanager

import config
from nicegui import ui


@contextmanager
def frame():
    with ui.header().classes("text-white items-center"):
        with ui.element("div").classes(
            "flex items-center justify-between w-full md:w-1/2 mx-auto"
        ):
            ui.button(icon="home", on_click=lambda: ui.open("/")).props("round size=sm")
            ui.label(os.environ.get("APP_NAME", "My App")).classes("font-bold text-lg")

    with ui.element("div").classes("w-full md:w-1/2 mx-auto"):
        yield
