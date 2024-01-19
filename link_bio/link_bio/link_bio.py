import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header()
    )
    # main_component =  rx.center(
    #     rx.text("Hola Milo!"", color="green"),
    # )
    # return main_component

color_tiffany = "#46c9c5"
style = { "background_color": color_tiffany }

app = rx.App(style=style)
app.add_page(index)
app.compile()
