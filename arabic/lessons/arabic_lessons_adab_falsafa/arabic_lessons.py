from flet import *
import sqlite3 as sq
from base64_string_icon_path import icons

hovering = False

def arabic_lessons(page):
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()

    def animate_buttons(e):
        global hovering
        if e.data == "true" and not hovering:
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1
            hovering = False
            page.update()

    def open_drawer(e):
        page.drawer.open = True
        page.update()

    # Define drawer first
    page.drawer = NavigationDrawer(
        bgcolor="#2F4F5F",
        controls=[
            ListTile(
                Container(
                    content=Column(
                        controls=[
                            ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                on_click=go_to_home,
                                content=Row(
                                    controls=[
                                        Image(src_base64=icons[13], width=50, height=50),
                                        Text("home", size=20, text_align=TextAlign.CENTER),
                                    ]
                                ),
                            ),
                            ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=Row(
                                    controls=[
                                        Image(src_base64=icons[0], width=50, height=50),
                                        Text("about us", size=20, text_align=TextAlign.CENTER),
                                    ]
                                ),
                            ),
                            ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=Row(
                                    controls=[
                                        Image(src_base64=icons[0], width=50, height=50),
                                        Text("give feedback", size=20, text_align=TextAlign.CENTER),
                                    ]
                                ),
                            ),
                        ],
                        scroll="auto",
                    )
                )
            )
        ],
    )

    # AppBar
    page.appbar = AppBar(
        bgcolor="#2F4F5F",
        title=Text(
            "BAC DZ - lessons",
            size=20,
            weight="bold",
            text_align=TextAlign.CENTER,
            offset=Offset(0.1, 0),
            color="white",
        ),
        leading=ElevatedButton(
            "| | |",
            on_click=open_drawer,
            on_hover=animate_buttons,
            color="black",
            bgcolor="white",
            height=40,
            width=40,
            offset=Offset(0.2, 0),
        ),
        center_title=True,
    )

    # Database
    arabic_db_path = r"arabic/lessons/arabic_lessons_adab_falsafa/arabic_lessons.db"
    conn = sq.connect(arabic_db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT link FROM arabic_lessons")
    links = cursor.fetchall()

    i = 0
    for link in links:
        i += 1
        page.controls.append(
            Container(
                content=ElevatedButton(
                    expand=True,
                    width=400,
                    height=80,
                    color="white",
                    bgcolor="#2F4F2F",
                    on_hover=animate_buttons,
                    on_click=lambda e, link=link[0]: page.launch_url(link),
                    content=Container(
                        content=Stack(
                            [
                                Image(src_base64=icons[17], width=50, height=50, top=5, left=0),
                                Text(
                                    f"lessons in                                                                                                            arabic N:{i}",
                                    size=20,
                                    text_align=TextAlign.CENTER,
                                    offset=Offset(0.0, 0),
                                ),
                            ]
                        )
                    ),
                ),
                alignment=alignment.center,
            )
        )

    page.update()
