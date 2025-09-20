"""---the lessons page---"""

from flet import *
from base64_string_icon_path import icons
import sys

#the animated butoon function global varibel
hovering = False

def lessons(page):
    """---the main lessons page ---"""
    page.padding = 1

    def go_to_ar_lesons(e):
        #function to go to the arabic lessonse file in arabic file

        from arabic.branch import branch
        page.controls.clear()
        branch(page)
        page.update()

    def go_to_home(e):
        #function for back button in the drawer and the back button

        from home import home
        page.controls.clear()
        home(page)
        page.update()
        
    def animate_buttons(e):
        #the function responsable for the animating buttons
        global hovering
        if e.data == 'true' and not hovering:

            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale=1
            hovering = False
        page.update()

    
    def open_drawer(e):
        #the draweer opening  function 
        page.drawer.open = True
        page.update()
    #the page draer     
    page.drawer = NavigationDrawer(
        bgcolor="#2F4F5F",
        controls=[ListTile(Container(content=Column(controls=[
            ElevatedButton(bgcolor='#8A0000',color='white',height=60,on_hover=animate_buttons,on_click=go_to_home,content=Row(controls=[Image(src_base64=icons[13],width=50,height=50),Text('home',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('aboutus',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('give feedback',size=20,text_align=TextAlign.CENTER)])),
            ],
            scroll='auto'))

            )])

    page.appbar = AppBar(
        bgcolor='#2F4F5F',
        title=Text('BAC DZ - lessons',size=20,weight='bold',text_align=TextAlign.CENTER,offset=Offset(0.1,0),color='white'),
        leading=ElevatedButton('| | |',on_click=open_drawer,on_hover=animate_buttons,color='black',bgcolor='white',height=40,width=40,offset=Offset(0.2,0)),
        center_title=True)
    
    """from first_frame to twenyone_frame all code the same just
    the button function use the first frame as a guid to all
    rest frame"""

    first_frame = Row([
        #row is a line 
        Container(
            #openning a container
            content=Column([
                #content is what in container 
                #use colume for an 90D line

                #text 
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('Arabic',color='white',size=31,text_align=TextAlign.CENTER),
                #button
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,on_click=go_to_ar_lesons,content=Row(controls=[Image(src_base64=icons[2],width=50,height=50),Text('Arabic',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                #adjust the position of the column
                alignment = MainAxisAlignment.CENTER,#align in the center
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            #adjust the position and CSS of the container
            border=border.all(3,'black'),#make frame border black
            bgcolor="#FFB74D",#background coulour of the frame
            padding=10,#المسافة بين العناصر و الحدود
            width=300,
            height=400,
            alignment = alignment.center,#align the frame in the center
            margin = margin.only(top=20)# offset the frame in top
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    second_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('math',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[18],width=50,height=50),Text('Math',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    
        
    therd_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('sience',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[21],width=60,height=60),Text('sience',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )
    
    
    fourth_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('fizics',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[10],width=60,height=60),Text('fizics',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    fifth_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('islamic iducation',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[15],width=60,height=60),Text('islamic',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    six_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('history & geo',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[12],width=60,height=60),Text('history & geo',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    seven_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('english',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[7],width=60,height=60),Text('english',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    eghit_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('frensh',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[11],width=60,height=60),Text('frensh',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            bgcolor="#81C784",
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    nine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('city eng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[3],width=60,height=60),Text('city eng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    ten_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('mecanic eng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[19],width=60,height=60),Text('mecanic eng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    eleven_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('electic eng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[6],width=60,height=60),Text('electic eng ',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    twelve_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('prosess eng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('prosess eng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    thertine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('economy',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[5],width=60,height=60),Text('economy',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    fourtine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('econommic & managemaent',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('managemaent',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    feftine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('acounting managemaent',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[20],width=60,height=60),Text('acounting',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    sixtine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('germany lng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('germany lng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    seventine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('italy lng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('italy lng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    eghtine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('spaine lng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('spaine lng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    nintine_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('amazigh lng',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[23],width=60,height=60),Text('amazigh lng',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
        
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    tweni_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('art',color='white',size=31,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[14],width=60,height=60),Text('art',size=20,text_align=TextAlign.CENTER,offset=Offset(0,0))]))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor="#81C784",
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
            page.controls.append(Column(controls=[first_frame,second_frame,therd_frame,fourth_frame,fifth_frame,six_frame,seven_frame,eghit_frame,nine_frame,ten_frame,eleven_frame,twelve_frame,thertine_frame,fourtine_frame,feftine_frame,sixtine_frame,seventine_frame,eghtine_frame,nintine_frame,tweni_frame]))
            page.add(ElevatedButton(width=200,height=60,color='white',bgcolor='#',on_hover=animate_buttons,on_click=go_to_home,content=Text('Back',size=20,text_align=TextAlign.CENTER))
)
        else:
            page.controls.append(Row(controls=[first_frame,second_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[fourth_frame,therd_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[fifth_frame,six_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[seven_frame,eghit_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[nine_frame,ten_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[eleven_frame,twelve_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[thertine_frame,fourtine_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[feftine_frame,sixtine_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[seventine_frame,eghtine_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[nintine_frame,tweni_frame],alignment= MainAxisAlignment.CENTER,spacing=100))

            
            
            page.add(ElevatedButton(width=200,height=60,color='white',bgcolor='#81C784',on_hover=animate_buttons,on_click=go_to_home,content=Text('Back',size=20,text_align=TextAlign.CENTER))
)



        page.update()
    page.on_resize = page_resaize
    page_resaize(None)
    



    page.update()