import reflex as rx
import datetime

hoy = datetime.date.today()
desde = 2019
experiencia = hoy.year - desde

style = {
    "background_color": "#202124",
    "color": "white"
    }

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Carlos Ceballos"),
        rx.text("Hola 🤟 Mi nombre es Carlos Ceballos."),
        rx.text("Soy desarrollador Full Stack."),
        rx.text(f"Tengo más de {experiencia} años de experiencia en desarrollo."),
        rx.text("He trabajado con empesas nacionales y multinacinales."),
        rx.text("A continuación encontrarás todos mis enlaces de interés."),
        rx.text("¡Bienvenid@!"),
        style=style
    )

