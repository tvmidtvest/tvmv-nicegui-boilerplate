import os

import _header
import config
import home
import page
from nicegui import ui

# Put this in all files that use the logger
logger = config.get_logger(__name__)


@ui.page("/")
def index_page() -> None:
    _header.content()
    home.content()


@ui.page("/page")
def index_page() -> None:
    _header.content()
    page.content()


ui.run(favicon="🚀", title="My app")
