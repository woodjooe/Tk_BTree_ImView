import copy

class BinaryTreeNode:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None
        self.BinaryList=list()
        self.DecimalList=list()
        self.NeededBinaryList=list()
        self.NeededDecimalList=list()

    def insert(node, newValue):
        print("TRying")
        if node.data is None:
            print("FAILing"+str(node.data))
            node.leftChild=BinaryTreeNode()
            node.rightChild=BinaryTreeNode()
            node.data=newValue
            print("FAILing"+str(node.data))
            return None
        else:
            if newValue < node.data:

                node.leftChild.insert(newValue)
            else:
                node.rightChild.insert(newValue)
                return None


    def BinaryToDecimal(self, l):
        for j in range(len(l)):
            if(l[i]=="1"):
                S+=3**(len(l)-j)*2;
            elif(l[i]=="0"):
                S-=3**(len(l)-j)*2;
        return S


    def DecimalToBinary(self, S):
        l=["","","","","","",""]
        leng=len(self.BinaryList[0])
        for j in range(leng):
            x=S%3
            S=S//3
            if(x==1):
                l[leng-j-1]="0"
            elif(x==2):
                l[leng-j-1]="1"
            else:
                l[leng-j-1]="2"

        return l


    def generateDecimalList(self):
        x=6
        N=0
        L0=self.BinaryList
        for i in range(1,x+1):
            N+=2**i
        print(L0)
        for i in range(len(L0)):
            l=L0[i]
            S=0
            for j in range(len(l)):
                if(l[j]=="1"):
                    S+=3**(len(l)-j)*2;
                elif(l[j]=="0"):
                    S-=3**(len(l)-j)*2;
            self.DecimalList.append(S)
            print(S)


    def generateNeededDecimalList(self):
        x=6
        N=0
        L0=self.NeededBinaryList
        for i in range(1,x+1):
            N+=2**i
        print(L0)
        for i in range(len(L0)):
            l=L0[i]
            S=0
            for j in range(len(l)):
                if(l[j]=="1"):
                    S+=3**(len(l)-j)*2;
                elif(l[j]=="0"):
                    S-=3**(len(l)-j)*2;
            self.NeededDecimalList.append(S)
            print(S)


    def generateBinaryList(self):
        x=6
        k=0
        l=list()
        val=["1","2","2","2","2","2","2"];
        l.append(copy.deepcopy(val))
        print(l)

        for i in range(1, x+1):
            for j1 in range(2):

                if(i>=1):
                    val[1]=str(j1)
                    if(i==1):
                        l0=copy.deepcopy(val)
                        l.append(l0)

                for j2 in range(2):

                    if(i>=2):
                        val[2]=str(j2)
                        if(i==2):
                            l0=copy.deepcopy(val)
                            l.append(l0)

                    for j3 in range(2):

                        if(i>=3):
                            val[3]=str(j3)
                            if(i==3):
                                l0=copy.deepcopy(val)
                                l.append(l0)
                        for j4 in range(2):

                            if(i>=4):
                                val[4]=str(j4)
                                if(i==4):
                                    l0=copy.deepcopy(val)
                                    l.append(l0)

                            for j5 in range(2):

                                if(i>=5):
                                    val[5]=str(j5)
                                    if(i==5):
                                        l0=copy.deepcopy(val)
                                        l.append(l0)

                                for j6 in range(2):

                                    if(i>=6):
                                        val[6]=str(j6)
                                        if(i==6):
                                            l0=copy.deepcopy(val)
                                            l.append(l0)
                                            self.NeededBinaryList.append(l0)

        print(l)
        self.BinaryList=l



    def fill_Tree(self):
        for i in range(len(self.DecimalList)):
            print("inserted value:"+str(self.DecimalList[i]))
            self.insert(self.DecimalList[i]);
            #print("inserted value:"+str(i))
            #self.insert(i);

    def search(self, value):
    # node is empty
        if self is None:
            return False
        # if element is equal to the element to be searched
        elif self.data == value:
            return True
        # element to be searched is less than the current node
        elif self.data > value:
            return search(self.leftChild, value)
        # element to be searched is greater than the current node
        else:
            return search(self.rightChild, value)
