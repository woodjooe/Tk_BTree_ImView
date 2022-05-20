
from tkinter import *

l=list();
s=str();
d=str();
backgroundColor="#eeeeee"

ButtonPosition=(500,100)




window=Tk();

frame=Frame(window)

window.title("Image_View!")
window.geometry("1024x600+150+50")
window.resizable(width=False, height=False)

background=PhotoImage(file='images/background.png')


button=PhotoImage(file='images/buttons.png')
button_720x480=PhotoImage(file='images/buttons720x480.png')
button_1024x600=PhotoImage(file='images/buttons1024x600.png')
button_1280x720=PhotoImage(file='images/buttons1280x720.png')

antennas=PhotoImage(file='images/antennas.png')
horns=PhotoImage(file='images/horns.png')
eyes1=PhotoImage(file='images/eyes1.png')
eyes2=PhotoImage(file='images/eyes2.png')
head1=PhotoImage(file='images/head1.png')
head2=PhotoImage(file='images/head2.png')
body1=PhotoImage(file='images/body1.png')
body2=PhotoImage(file='images/body2.png')
hands1=PhotoImage(file='images/hands1.png')
hands2=PhotoImage(file='images/hands2.png')
legs1=PhotoImage(file='images/legs1.png')
legs2=PhotoImage(file='images/legs2.png')

antennas=antennas.subsample(3, 3)
horns=horns.subsample(3, 3)
eyes1=eyes1.subsample(3, 3)
eyes2=eyes2.subsample(3, 3)
head1=head1.subsample(3, 3)
head2=head2.subsample(3, 3)
body1=body1.subsample(3, 3)
body2=body2.subsample(3, 3)
hands1=hands1.subsample(3, 3)
hands2=hands2.subsample(3, 3)
legs1=legs1.subsample(3, 3)
legs2=legs2.subsample(3, 3)




frame.pack();
