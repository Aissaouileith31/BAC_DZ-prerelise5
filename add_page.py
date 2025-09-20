import sqlite3
from flet import *
from base64_string_icon_path import icons



hovering=False
def add_page(page):
    page.title = "publish subject"
    page.update
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    def go_to_add_lessonse(e):
        from add_lessons_page import add_lessons
        page.controls.clear()
        add_lessons(page)
        page.update()
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
    page.drawer = NavigationDrawer(
        bgcolor="#2F4F7F",
        controls=[ListTile(Container(content=Column(controls=[
            ElevatedButton(bgcolor='#8A0000',color='white',height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[13],width=50,height=50),Text('home',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('aboutus',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('give feedback',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('Add',size=20,text_align=TextAlign.CENTER)])),
            
            ],
            scroll='auto'))

            )])

    page.appbar = AppBar(
        bgcolor='#2F4F5F',
        title=Text('BAC DZ - algeria futur',size=20,weight='bold',text_align=TextAlign.CENTER,offset=Offset(0.1,0),color='white'),
        leading=ElevatedButton('| | |',on_click=open_drawer,on_hover=animate_buttons,color='black',bgcolor='white',width=40,height=40,offset=Offset(0.2,0)),
        center_title=True)


    first_frame = Row([
        Container(
            content=Column([
                Text('add lessons and summaries',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('publish your lessons to auther student ',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#2F4F2F ',on_hover=animate_buttons,on_click=go_to_add_lessonse,content=Container(content=Stack([Image(src_base64=icons[17],width=50,height=50,top=5,left=0),Text('add lessons and summaries',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#4CAF51',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    second_frame = Row([
        Container(
            content=Column([
                Text('add subject',color='white',weight='bold',size=33),
                Text('you can also publish subject to auther student',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#CC0000',on_hover=animate_buttons,content=Container(content=Stack([Image(src_base64=icons[24],width=60,height=60,top=0,left=0),Text('add                              subject',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])),offset=Offset(0,0.6))],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#FF3737',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    def page_resaize(e):
        if page.width < 600:
            page.controls.append(Column(controls=[first_frame,second_frame]))

        else:
            page.controls.append(Row(controls=[first_frame,second_frame],alignment= MainAxisAlignment.CENTER,spacing=100))

        page.update()
    page.on_resize = page_resaize
    page_resaize(None)



































