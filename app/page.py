import os

import config
from nicegui import events, ui

logger = config.get_logger(__name__)


def content():

    def handle_click(e: events.GenericEventArguments) -> None:
        logger.info(f"Row clicked: {e.args}")
        ui.notification(f"Row clicked: {e.args[1]}")

    with ui.element("div").classes("mb-4"):
        columns = [
            {
                "name": "title",
                "label": "Title",
                "field": "title",
                "align": "left",
            },
            {
                "name": "year",
                "label": "Year",
                "field": "year",
                "align": "right",
            },
        ]

        data = [
            {"title": "The Shawshank Redemption", "year": 1994, "id": 1},
            {"title": "The Godfather", "year": 1972, "id": 2},
            {"title": "The Godfather: Part II", "year": 1974, "id": 3},
            {"title": "The Dark Knight", "year": 2008, "id": 4},
        ]

        table = ui.table(columns=columns, rows=data, row_key="id", title="Movies")

        table.on("row-click", lambda e: handle_click(e))

    ui.button("Go to the home page", on_click=lambda: ui.open("/"))
