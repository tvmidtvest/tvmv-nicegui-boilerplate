import os

import config
from nicegui import ui

logger = config.get_logger(__name__)


def content():
    with ui.element("div").classes("text-center w-full md:w-1/2 mx-auto"):
        ui.markdown("Welcome to the home page!")
        ui.button("Go to the other page", on_click=lambda: ui.open("/page"))
