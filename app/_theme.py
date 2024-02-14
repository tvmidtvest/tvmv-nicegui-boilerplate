import os
from contextlib import contextmanager

import config
from nicegui import ui


@contextmanager
def frame():
    with ui.header().classes("justify-between text-white items-center"):
        ui.button(icon="home", on_click=lambda: ui.open("/")).props(
            "color=positive round size=sm"
        )
        ui.label("Modularization Example").classes("font-bold text-lg")

    with ui.element("div").classes("text-center w-full md:w-1/2 mx-auto"):
        yield
