import os

import config
from nicegui import ui

logger = config.get_logger(__name__)


def content():
    ui.markdown("Welcome to the other page!")
    ui.button("Go to the home page", on_click=lambda: ui.open("/"))
