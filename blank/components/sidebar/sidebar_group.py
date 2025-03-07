import reflex as rx
from .sidebar_item import sidebar_menu_item

def sidebar_group(group):
    return rx.accordion.item(
        rx.accordion.trigger(
            rx.text(group["title"], font_weight="medium"),
            rx.spacer(),
            rx.accordion.icon(),
        ),
        rx.accordion.content(
            rx.vstack(
                *[
                    sidebar_menu_item(
                        item["title"], 
                        item["url"], 
                        item.get("is_active", False)
                    )
                    for item in group["items"]
                ],
                align_items="stretch",
                width="100%",
                spacing="0",
            ),
            padding_top="0.25em",
            padding_bottom="0.25em",
        ),
        width="100%",
    )
