from flet import *
from base64_string_icon_path import icons

hovering = False

def branch(page):
    def go_to_lessons_falsafa(e):
        import arabic.lessons.arabic_lessons_adab_falsafa.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()
    def go_to_ar_lessons_sience(e):
        import arabic.lessons.arabic_lessons_sience.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()

    def go_to_ar_lessons_oth_lng(e):
        import arabic.lessons.arabic_lessons_auther_lenguege.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()


    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1
            hovering = False
        page.update()

    def open_drawer(e):
        page.drawer.open = True
        page.update()
        page.drawer = NavigationDrawer(
            bgcolor="#2F4F5F",
            controls=[
                ListTile(
                    Container(
                        content=Column(
                            controls=[
                                ElevatedButton(
                                    bgcolor='#8A0000',
                                    color='white',
                                    height=60,
                                    on_hover=animate_buttons,
                                    content=Row(
                                        controls=[
                                            Image(src_base64=icons[13], width=50, height=50),
                                            Text('home', size=20, text_align=TextAlign.CENTER)
                                        ]
                                    )
                                ),
                                ElevatedButton(
                                    bgcolor='#8A0000',
                                    color="white",
                                    height=60,
                                    on_hover=animate_buttons,
                                    content=Row(
                                        controls=[
                                            Image(src_base64=icons[0], width=50, height=50),
                                            Text('aboutus', size=20, text_align=TextAlign.CENTER)
                                        ]
                                    )
                                ),
                                ElevatedButton(
                                    bgcolor='#8A0000',
                                    color="white",
                                    height=60,
                                    on_hover=animate_buttons,
                                    content=Row(
                                        controls=[
                                            Image(src_base64=icons[0], width=50, height=50),
                                            Text('give feedback', size=20, text_align=TextAlign.CENTER)
                                        ]
                                    )
                                ),
                            ],
                            scroll='auto'
                        )
                    )
                )
            ]
        )

    page.appbar = AppBar(
        bgcolor='#2F4F5F',
        title=Text(
            'BAC DZ - lessons',
            size=20,
            weight='bold',
            text_align=TextAlign.CENTER,
            offset=Offset(0.1, 0),
            color='white'
        ),
        leading=ElevatedButton(
            '| | |',
            on_click=open_drawer,
            on_hover=animate_buttons,
            color='black',
            bgcolor='white',
            height=40,
            width=40,
            offset=Offset(0.2, 0)
        ),
        center_title=True
    )

    # ----- Frames (cards) -----
    first_frame = Row([
        Container(
            content=Column([
                Text("sience brench", color='white', size=33 , weight='bold', text_align=TextAlign.CENTER),
                ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#2F4F2F ',
                    on_hover=animate_buttons,
                    on_click=go_to_ar_lessons_sience,
                    content=Container(
                        content=Stack([
                            Text('sience brench', size=20, text_align=TextAlign.CENTER, offset=Offset(0, 0))
                        ])
                    )
                )
            ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            border=border.all(3, 'black'),
            bgcolor='#4CAF51',
            padding=10,
            width=300,
            height=400,
            alignment=alignment.center,
            margin=margin.only(top=20)
        )
    ], alignment=MainAxisAlignment.CENTER)

    second_frame = Row([
        Container(
            content=Column([
                Text('philosophy literatur ', color='white', weight='bold', size=33,text_align=TextAlign.CENTER),
                ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#CC0000',
                    on_hover=animate_buttons,
                    on_click=go_to_lessons_falsafa,
                    content=Container(
                        content=Stack([
                            Text('philosophy literatur ', size=20, text_align=TextAlign.CENTER, offset=Offset(0, 0))
                        ])
                    ),
                    offset=Offset(0, 0.6)
                )
            ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            border=border.all(3, 'black'),
            bgcolor='#FF3737',
            padding=10,
            width=300,
            height=400,
            alignment=alignment.center,
            margin=margin.only(top=20)
        )
    ], alignment=MainAxisAlignment.CENTER)

    therd_frame = Row([
        Container(
            content=Column([
                Text('ahther lengueg', color='black', weight='bold', size=33, text_align=TextAlign.CENTER),
                ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#999900',
                    on_hover=animate_buttons,
                    on_click=go_to_ar_lessons_oth_lng,

                    content=Container(
                        content=Stack([
                            Text('ahther lengueg', size=20, text_align=TextAlign.CENTER, offset=Offset(0, 0))
                        ])
                    )
                )
            ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            border=border.all(3, 'black'),
            bgcolor='#CCCC66',
            padding=10,
            width=300,
            height=400,
            alignment=alignment.center,
            margin=margin.only(top=20)
        )
    ], alignment=MainAxisAlignment.CENTER)

    # ----- Responsive Layout -----
    def page_resaize(e):
        page.controls.clear()

        if page.width < 600:
            # Mobile: 1 per row
            page.controls.append(
                Column(
                    controls=[first_frame, second_frame, therd_frame],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )
        else:
            # PC: 2 per row, then 1 per row
            page.controls.append(
                Column(
                    controls=[
                        Row(
                            controls=[first_frame, second_frame],
                            alignment=MainAxisAlignment.CENTER,
                            spacing=50
                        ),
                        Row(
                            controls=[therd_frame],
                            alignment=MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=40,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )

        page.update()

    page.on_resize = page_resaize
    page_resaize(None)
