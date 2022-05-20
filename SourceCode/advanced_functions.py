from functions import *
from TreeClass import *


def Donate(C):
    global d
    d="Thank you for !!!!... 0 DT!"
    homeScreen();




def changeSize(x,y,a,b):
    changeSize0(x,y,a,b)
    settingsScreen()


def settingsScreen():

    window.update_idletasks()
    clear_frame()
    C = Canvas(frame,bd=2,confine=True,width=window.winfo_width(),height=window.winfo_height())

    C.create_image(window.winfo_width()/2,window.winfo_height()/2,image=background)

    posB=(ButtonPosition[0]*((window.winfo_width())/1024),
    ButtonPosition[1]*(window.winfo_height()/600))

    level_1_Resolution=Button(frame,text="720 × 480",
    image=button,
    command=lambda: changeSize(720,480,300,100),
    fg='black',
    compound='center')

    level_2_Resolution=Button(frame,text="1024 × 600",
    image=button,
    command=lambda: changeSize(1024,600,150,50),
    fg='black',
    compound='center')

    level_3_Resolution=Button(frame,text="1280 × 720",
    image=button,
    command=lambda: changeSize(1200,720,150,50),
    fg='black',
    compound='center')

    back=Button(frame,text="Back to main",
    image=button,
    command=Show_Image,
    fg='black',
    compound='center');

    C.pack()

    level_1_Resolution.place(x=posB[0]-100,y=posB[1])
    level_2_Resolution.place(x=posB[0]-100,y=posB[1]+100)
    level_3_Resolution.place(x=posB[0]-100,y=posB[1]+200)
    back.place(x=posB[0]-100,y=window.winfo_height()-100)

def resetBinaryTree():
    global T
    global l
    l=["1","0","0","0","0","0","0"]
    T=BinaryTreeNode()

    T.generateBinaryList()
    T.generateDecimalList()
    T.generateNeededDecimalList()


    T.fill_Tree()

def antennas_horns(ch):
    l[1]=ch
    Show_Image()

def eyes1_eyes2(ch):
    l[2]=ch
    Show_Image()

def head1_head2(ch):
    l[3]=ch
    Show_Image()

def body1_body2(ch):
    l[4]=ch
    Show_Image()

def hands1_hands2(ch):
    l[5]=ch
    Show_Image()

def legs1_legs2(ch):
    l[6]=ch
    Show_Image()



def Show_Image():

    window.update_idletasks()
    clear_frame()
    C = Canvas(frame,bd=2,confine=True,width=window.winfo_width(),height=window.winfo_height())

    C.create_image(window.winfo_width()/2,window.winfo_height()/2,image=background)

    coord1=-50
    coord2=+50

    if( int(l[1]) ):
        C.create_image(coord1,coord2,anchor=NW,image=antennas)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=horns)
    if( int(l[2]) ):
        C.create_image(coord1,coord2,anchor=NW,image=eyes1)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=eyes2)
    if( int(l[3]) ):
        C.create_image(coord1,coord2,anchor=NW,image=head1)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=head2)
    if( int(l[4]) ):
        C.create_image(coord1,coord2,anchor=NW,image=body1)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=body2)
    if( int(l[5]) ):
        C.create_image(coord1,coord2,anchor=NW,image=hands1)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=hands2)
    if( int(l[6]) ):
        C.create_image(coord1,coord2,anchor=NW,image=legs1)
    else:
        C.create_image(coord1,coord2,anchor=NW,image=legs2)



    posB=(ButtonPosition[0]*((window.winfo_width())/1024),
    ButtonPosition[1]*(window.winfo_height()/600))



    entryMessageE=Entry(frame,font=("Arial",10,"bold"))


    antennas_Button=Button(frame, text="antennas",
    width=200, height=15,
    image=button,
    command=lambda: antennas_horns("1"),
    fg='purple',
    compound='center',
    )
    horns_Button=Button(frame, text="horns",
    width=200, height=15,
    image=button,
    command=lambda: antennas_horns("0"),
    fg='purple',
    compound='center',
    )
    eyes1_Button=Button(frame, text="sharp eyes",
    width=200, height=15,
    image=button,
    command=lambda: eyes1_eyes2("1"),
    fg='purple',
    compound='center',
    )
    eyes2_Button=Button(frame, text="round eyes",
    width=200, height=15,
    image=button,
    command=lambda: eyes1_eyes2("0"),
    fg='black',
    compound='center',
    )
    head1_Button=Button(frame, text="round head",
    width=200, height=15,
    image=button,
    command=lambda: head1_head2("1"),
    fg='purple',
    compound='center',
    )
    head2_Button=Button(frame, text="sharp head",
    width=200, height=15,
    image=button,
    command=lambda: head1_head2("0"),
    fg='purple',
    compound='center',
    )
    body1_Button=Button(frame, text="round body",
    width=200, height=15,
    image=button,
    command=lambda: body1_body2("1"),
    fg='purple',
    compound='center',
    )
    body2_Button=Button(frame, text="slim body",
    width=200, height=15,
    image=button,
    command=lambda: body1_body2("0"),
    fg='purple',
    compound='center',
    )
    hands1_Button=Button(frame, text="2 arms",
    width=200, height=15,
    image=button,
    command=lambda: hands1_hands2("1"),
    fg='purple',
    compound='center',
    )
    hands2_Button=Button(frame, text="4 arms",
    width=200, height=15,
    image=button,
    command=lambda: hands1_hands2("0"),
    fg='purple',
    compound='center',
    )
    legs1_Button=Button(frame, text="2 legs",
    width=200, height=15,
    image=button,
    command=lambda: legs1_legs2("1"),
    fg='purple',
    compound='center',
    )
    legs2_Button=Button(frame, text="4 legs",
    width=200, height=15,
    image=button,
    command=lambda: legs1_legs2("0"),
    fg='purple',
    compound='center',
    )


    back=Button(frame,text="Back to settings",
    width=200, height=15,
    image=button,
    command=settingsScreen,
    fg='#333333',
    compound='center',);


    C.create_text(300, 500, text=s, fill="green", font=('Helvetica 15 bold'))
    C.pack()

    #ShowMessageE.place(x=posB[0]+300,y=posB[1]+15,width=200)

    antennas_Button.place(x=posB[0]+100,y=posB[1])
    horns_Button.place(x=posB[0]+300,y=posB[1])
    eyes1_Button.place(x=posB[0]+100,y=posB[1]+30)
    eyes2_Button.place(x=posB[0]+300,y=posB[1]+30)
    head1_Button.place(x=posB[0]+100,y=posB[1]+60)
    head2_Button.place(x=posB[0]+300,y=posB[1]+60)
    body1_Button.place(x=posB[0]+100,y=posB[1]+90)
    body2_Button.place(x=posB[0]+300,y=posB[1]+90)
    hands1_Button.place(x=posB[0]+100,y=posB[1]+120)
    hands2_Button.place(x=posB[0]+300,y=posB[1]+120)
    legs1_Button.place(x=posB[0]+100,y=posB[1]+150)
    legs2_Button.place(x=posB[0]+300,y=posB[1]+150)


    back.place(x=posB[0]+200,y=window.winfo_height()-100)
