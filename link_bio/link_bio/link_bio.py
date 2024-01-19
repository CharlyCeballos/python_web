import reflex as rx
from link_bio.components.navbar import navbar

class State(rx.State):
    pass

def index() -> rx.Component:
    return navbar()
    # main_component =  rx.center(
    #     rx.text('Hola Milo!', color='green'),
    # )
    # return main_component

accent_color = "#202124"
style = { "background_color": accent_color }

app = rx.App(style=style)
app.add_page(index)
app.compile()
