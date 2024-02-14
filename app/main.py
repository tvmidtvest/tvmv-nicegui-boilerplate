import os

import config
import home
import page
import theme
from nicegui import ui

# Put this in all files that use the logger
logger = config.get_logger(__name__)


@ui.page("/")
def index_page() -> None:
    with theme.frame():
        home.content()


@ui.page("/page")
def index_page() -> None:
    with theme.frame():
        page.content()


ui.run(favicon="🚀", title="My app")
