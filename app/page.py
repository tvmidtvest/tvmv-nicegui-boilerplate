import os

import config
from nicegui import ui

logger = config.get_logger(__name__)


def content():

    with ui.element("div").classes("text-center w-full md:w-1/2 mx-auto"):
        ui.markdown("Welcome to the other page!")
        ui.button("Go to the home page", on_click=lambda: ui.open("/"))

    my_var = os.environ.get("MY_VAR", "default value")

    logger.info(f"Page content was displayed: {my_var}")
