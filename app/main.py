import os

import _theme
import config
import home
import page
from nicegui import ui

# Put this in all files that use the logger
logger = config.get_logger(__name__)


@ui.page("/")
def index_page() -> None:
    with _theme.frame():
        home.content()


@ui.page("/page")
def index_page() -> None:
    with _theme.frame():
        page.content()


ui.run(favicon="🚀", title="My app")
