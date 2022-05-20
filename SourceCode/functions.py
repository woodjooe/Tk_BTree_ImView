from setUp import *
from TreeClass import *


def homeScreen(): pass
def settingsScreen():pass

def changeSize0(x,y,a,b):

    s=str(x)+"x"+str(y)+"+"+str(a)+"+"+str(b);
    window.geometry(s)

    window.resizable(width=False, height=False)



def clear_frame():
    if(frame.winfo_children()):
        for widgets in frame.winfo_children():
            widgets.destroy()


def make_Tree():

    T=BinaryTreeNode();
    T.fill_Tree(x,l);
    print("T has !!! "+str(T.data)+" and "+str(T.rightChild.data))
    return T
