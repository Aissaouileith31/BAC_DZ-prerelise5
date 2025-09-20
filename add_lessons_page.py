import sqlite3
import flet as ft
from flet import *
from base64_string_icon_path import icons

hovering = False

def add_lessons(page):
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    page.title = "Link App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 300



    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:

            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale=1
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



    dropdown_value=None

    # Header Text
    title_text = ft.Text(
        "Add Arabic Lesson Link",
        size=22,
        weight="bold",
        color="blue"
    )

    # Input Field
    link_field = ft.TextField(
        hint_text="Paste the Google Drive link here",
        width=350,
        filled=True
    )
    def dropdown_change(e):
        nonlocal dropdown_value
        dropdown_value= e.control.value

    def publishe(e):
        link = link_field.value.strip()
        if not link:
            page.controls.append(ft.Text("⚠️ Please enter a link.", color="red"))
            page.update()
            return
        

        if dropdown_value=='arabic':
            if options_group.value=='sience_brensh':

        
                try:
                    arabic_db_path ='arabic/lessons/arabic_lessons_sience/arabic_lessons.db'
                    conn = sqlite3.connect(arabic_db_path)
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                    conn.commit()
                    conn.close()

                    link_field.value = ''
                    page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
                except Exception as ex:
                    page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))

                    page.update()

            elif options_group.value == "authe_lenguege":
                try:
                    arabic_db_path = r'arabic/lessons/arabic_lessons_auther_lenguege/arabic_lessons.db'
                    conn = sqlite3.connect(arabic_db_path)
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                    conn.commit()
                    conn.close()

                    link_field.value = ''
                    page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
                except Exception as ex:
                    page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))

                    page.update()
                

                  
    

    # Submit Button
    submit_button = ft.ElevatedButton(
        text="Publish",
        on_click=publishe,
        bgcolor="blue",
        color="white"
    )

    options_group = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Row([ft.Radio(value="sience_brensh", label="Science branch")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Radio(value="philosophy_literatur", label="Philosophy & Literature")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Radio(value="authe_lenguege", label="Other language")], alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=10,
        )
    )

    subject = ft.Dropdown(label='chouse the subject',width=200,options=[ft.dropdown.Option('arabic'),
        ft.dropdown.Option('math'),ft.dropdown.Option('since'),
        ft.dropdown.Option('phyzic'),ft.dropdown.Option('history & geo'),
        ft.dropdown.Option('eslamic ed'),ft.dropdown.Option('electric eng'),
        ft.dropdown.Option('mecanic eng'),ft.dropdown.Option('civil eng'),
        ft.dropdown.Option('prosess eng'),ft.dropdown.Option('english'),
        ft.dropdown.Option('frensh'),ft.dropdown.Option('economy'),
        ft.dropdown.Option('law'),ft.dropdown.Option('econommic & managemaent'),
        ft.dropdown.Option('acounting '),ft.dropdown.Option('germany'),
        ft.dropdown.Option('spanish'),ft.dropdown.Option('italy'),
        ft.dropdown.Option('art'), ft.dropdown.Option('amazigh')

        ],on_change=dropdown_change)

    page.controls = [
        ft.Container(
            content=ft.Column(
                [
                    title_text,
                    link_field,
                    subject,
                    ft.Text('chouse breansh',size=22,text_align=ft.TextAlign.CENTER),
                    options_group,
                    submit_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            alignment=ft.alignment.center,
        )
    ]
    page.update()



