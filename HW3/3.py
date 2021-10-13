# In this file, fill in the ... parts with lines of code. Do not
# create new functions.

from random import seed, randrange
import random
P=" ♟♜♝♞♛♚"; L,R,BL,TL="▌▐▄▀"
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m' # For drawing a white piece on a red background
WonB+='7;30;47m' # For drawing a white piece on a black background
DonR+='2;37;41m' # For drawing a dark piece on a red background
DonB+='2;37;40m' # For drawing a dark piece on a black background
GonR+='2;33;41m' # For drawing gold on a red background
GonB+='2;33;40m' # For drawing gold on a black background
RonG+='2;31;43m' # For drawing red on a gold background
RonB+='7;30;41m' # For drawing red on a black background
BonR+='0;30;41m' # For drawing black on a red background

def Black(x,w,c):
    """A function to print a chess piece on a black background.
        Inputs:
         x: A single-character string indicating the value to put in
            this square. It will be one of the following: " ", "♟",
            "♜", "♝", "♞", "♛", or "♚". (Note that " " is one of the
            options, and is used for empty squares.)
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. (We need
            to know this because the leftmost square (c=0) has gold 
            on the left side, and the rightmost square (c=7) has gold
            on the right side.

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, the one character passed in
        as x is printed, in the indicated color.
       -Finally, in the one case that c=7, a newline character is 
        printed.                                                  """

    #設定w=1=灰//w=0=白
    if w==1:
        color=DonB
    else:
        color=WonB
	#設定第一行跟最後一行的金邊還有普通的
    if c==0:
        global L,R	
        print(GonB+L+color+x,end="")
    elif c==7:
        print(color+x+GonB+R+'\033[1;m',end="\n")	#+'\033[1;m'好像是讓它不要多後面一串的背景色
    else:
        print(color+x,end="")


    
def Red(x,w,c):
    """A function to print a chess piece on a red background.
        Inputs: These are the same as the inputs for Black()
         x: A string indicating the value to put in this square. 
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. 

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, three characters always print:
         1: A "▐" character that is red on its right side, and that 
            is either gold (if c=0) or black (otherwise) on its left
            side.
         2: The character passed in as x, in the indicated color.
         3: A "▌" character that is red on its left side and that is
            either gold (if c=7) or black (otherwise) on its right
            side.
       -Finally, in the one case that c=7, a newline is printed.
        But somethings needs to be understood here. First, you don't 
        really need to print a "\n", you can just NOT use an "end=''"
        when printing this last "▌" piece. Second, you also need to 
        change the color to GonB before going to the next line, to 
        prevent colored bars from drawing on the left.            """

    #設定w=1=灰//w=0=白
    if w==1:
        color=DonR
    else:
        color=WonR
    #設定第一行跟最後一行的金邊還有普通的 然後加紅黑邊界
    if c==0:
        global L,R	
        print(GonR+L+color+x+BonR+R,end="")
    elif c==7:
        print(BonR+L+color+x+GonR+R+'\033[1;m')
    else:
        print(BonR+L+color+x+BonR+R,end="")


    
def DrawBoard(B,W):
    """A function to draw a chess board with its pieces.
        Inputs:
         B: This is the board. It must be a list of 8 strings, which
            indicate the 8 rows of the chessboard. The 8 strings are
            each 8 characters wide, indicating the 8 rows of the
            chessboard. The individual characters in the strings are
            any of the following: " ","♟","♜","♝","♞","♛", or "♚".
         W: This is a list of 16 complex numbers. Each number encodes
            the row/column position of one of the 16 white pieces.
            (We don't need a similar list of dark pieces, because
            anything that is not white can print as dark.

       Outputs:
        The output is to print the eight rows of the board, along 
        with two more rows for the top and bottom gold border.    """

    def DrawRow(r,B,W):
        """A function to draw a single row of the chess board.
           Input:
            r: An integer indicating the row number.
            B: This is the board.
            W: This is a list of white piece locations.

           Outputs:
            The output is the printing of the indicated row.      """


        if r%2==0:
                for c in range(8):
                    if ((r,c) in W) == True:
                        wg=0
                    else:
                        wg=1
                    if c%2==0:
                        Red(B[r][c],wg,c)
                    else:
                        Black(B[r][c],wg,c)
        else:
                for c in range(8):
                    if ((r,c) in W) == True:
                        wg=0
                    else:
                        wg=1
                    if c%2==0:
                        Black(B[r][c],wg,c)
                    else:
                        Red(B[r][c],wg,c)
   		 
	
    
    print(GonB+BL*17+'\033[1;m')
    for i in range(8):
    	DrawRow(i,B,W)
    print(GonB+TL*17+'\033[1;m')
    



################################################ new ##############################################################
#每個位置對應到的鍵值對
D={'R1':(0,0),'N1':(0,1),'B1':(0,2),'Q':(0,3),'K':(0,4),'B2':(0,5),'N2':(0,6),'R2':(0,7),'p1':(1,0),'p2':(1,1),'p3':(1,2),'p4':(1,3),'p5':(1,4),'p6':(1,5),'p7':(1,6),'p8':(1,7)}
W={'p1':(6,0),'p2':(6,1),'p3':(6,2),'p4':(6,3),'p5':(6,4),'p6':(6,5),'p7':(6,6),'p8':(6,7),'R1':(7,0),'N1':(7,1),'B1':(7,2),'Q':(7,3),'K':(7,4),'B2':(7,5),'N2':(7,6),'R2':(7,7)}

color=0
def GetAMove(color):
    global D,W
    if color%2==0:
        command=input("White: ")
        while Legal(command,color)==False:
                command=input("White: ")
    else:
        command=input("Black: ")
        while Legal(command,color)==False:
                command=input("Black: ")
    sp=command#.split('')
    y=file_name[(sp[(len(sp)-2)])]
    x=rank_name[(sp[(len(sp)-1)])]
    to=(x,y)
    fro=SemanticallyLegal(command,color)
    new_D={v:k for k, v in D.items()}
    new_W={v:k for k, v in W.items()}
    if color%2==0:#白色
        if sp[len(sp)-3]=='x':
            del D[new_D[to]]
            W[new_W[fro]]=to
        else:
            W[new_W[fro]]=to
    else:#黑色
        if sp[len(sp)-3]=='x':
            del W[new_W[to]]
            D[new_D[fro]]=to
        else:
            D[new_D[fro]]=to



def Legal(command,color):

    if SyntacticallyLegal(command)==False:
        return False
    elif SemanticallyLegal(command,color)==False:
        return False
    else:
        return True

chess=['R','N','B','Q','K']
move=['x']
file_name={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rank_name={'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}

def SyntacticallyLegal(command):
    global chess,move,file_name,rank_name
    sp=command#.split('')
    if len(sp)==0:
        print("You need to input something")
        return False
    if sp[(len(sp)-2)] not in file_name:
            print("File name error")
            return False
    if sp[(len(sp)-1)] not in rank_name:
            print("Rank name error")
            return False

    if len(sp)==3:
        if sp[0] not in chess and sp[0] not in move:
            print("input error")
            return False
        else:
            return True
    elif len(sp)==4:
        if sp[0] not in chess:
            if sp[0] not in file_name and sp[0] not in rank_name :
                 print("input error")
                 return False
            else:
                 if sp[1] not in move:
                     print("input error")
                     return False
                 else:
                     return True
        else:
            if sp[1] not in move and sp[1] not in file_name and sp[1] not in rank_name:
                     print("input error",sp[1])
                     return False
            else:
                     return True
    elif len(sp)==5:
        if sp[2] not in move:
            print("input error")
            return False
        if sp[0] not in chess or sp[1] not in file_name and sp[1] not in rank_name :
            print("input error")
            return False
        else:
            return True
    elif len(sp)==6:
        if sp[0] not in chess or sp[1] not in file_name or sp[2] not in rank_name or sp[3] not in move :
            print("input error")
            return False
        
pDark_firsttime={'p1':1,'p2':1,'p3':1,'p4':1,'p5':1,'p6':1,'p7':1,'p8':1}
pWhite_firsttime={'p1':1,'p2':1,'p3':1,'p4':1,'p5':1,'p6':1,'p7':1,'p8':1}

def SemanticallyLegal(command,color):
    global D,W,chess,move,file_name,rank_name,pDark_firsttime,pWhite_firsttime
    sp=command#.split('')
    y=file_name[(sp[(len(sp)-2)])]
    x=rank_name[(sp[(len(sp)-1)])]
    new_D={v:k for k, v in D.items()}
    new_W={v:k for k, v in W.items()}
    if color%2==0:    #白色
         if (x,y) in D.values() and sp[(len(sp)-3)] not in move:   #沒有x不能吃其他顏色的棋子
                print("You can't move to where a piece of other color is,if you don't say 'x'")
                return False
         elif (x,y) in W.values():	#不能移到同色
                print("You can't move into a square already containing one of your own pieces")
                return False

         if len(sp)==2:
         #檢查哪個p可以走到x,y
                if (x+1,y) in W.values():
                   if new_W[(x+1,y)] in pWhite_firsttime:
                       pWhite_firsttime[new_W[(x+1,y)]]=0
                       return (x+1,y)
                elif (x+2,y) in W.values() and new_W[(x+2,y)] in pWhite_firsttime:
                       if pWhite_firsttime[new_W[(x+2,y)]]==0:
                           if (x+1,y) not in D.values() and (x+1,y) not in W.values():
                                 return (x+2,y)
                           else:
                                 print("No Pawn can move to there")
                                 return False
                       else:
                            print("Pawn can't move two squares at the first time")
                            return False
                else:
                       print("No Pawn can move to there")
                       return False

         else:
            if sp[(len(sp)-3)] not in move:    #檢查走的動作有沒有出錯
                  if sp[0] not in chess:     #檢查可否移動到那裡、 有沒有指定
                     print("You didn't chose which chess you want to move. If you want to move Pawn, you don't need to input its file name and rank name.")
                     return False
                  elif sp[0]=='R':
                     print("haven't done yet")
                  elif sp[0]=='N':
                     print("haven't done yet")
                  elif sp[0]=='B':
                     print("haven't done yet")
                  elif sp[0]=='Q':
                     if len(sp)==3:
                           print("haven't done yet")
                     elif len(sp)==4:
                         if sp[1] in file_name :
                            for i in range(8):
                                 if (i,file_name[sp[0]]) in W.values():
                                   if new_W[(i,file_name[sp[0]])]=='Q':
                                     for t in range(-8,8):
                                        if (x,y)==(i+t,file_name[sp[0]]+t) :
                                           return (i+t,file_name[sp[0]]+t)
                                        elif (x,y)==(i,file_name[sp[0]]+t):
                                           return (i,file_name[sp[0]]+t)
                                        elif (x,y)==(i+t,file_name[sp[0]]):
                                           return (i+t,file_name[sp[0]])
                                        else:
                                           print("error")
                                           return False
                                 else:
                                        print("error")
                         else:
                               for i in range(8):
                                   if (rank_name[sp[0]],i) in W.values() and new_W[(i,file_name[sp[0]])]=='Q':
                                     for t in range(-8,8):
                                        if (x,y)==(rank_name[sp[0]]+t,i+t) :
                                           return (rank_name[sp[0]]+t,i+t)
                                        elif (x,y)==(rank_name[sp[0]]+t,i):
                                           return (rank_name[sp[0]]+t,i)
                                        elif (x,y)==(rank_name[sp[0]],i+t):
                                           return (rank_name[sp[0]],i+t)
                                        else:
                                           print("error")
                                           return False
                                   else:
                                        print("error")
                     elif len(sp)==5:
                         if (rank_name[sp[1]],file_name[sp[0]]) in W.values() and new_W[(rank_name[sp[1]],file_name[sp[0]])]=='Q':
                             for t in range(-8,8):
                               if (x,y)==(rank_name[sp[1]]+t,file_name[sp[0]]+t) :
                                    return (rank_name[sp[1]]+t,file_name[sp[0]]+t)
                               elif (x,y)==(rank_name[sp[1]]+t,file_name[sp[0]]):
                                    return (rank_name[sp[1]]+t,file_name[sp[0]])
                               elif (x,y)==(rank_name[sp[1]],file_name[sp[0]]+t):
                                    return (rank_name[sp[1]],file_name[sp[0]]+t)
                               else:
                                    print("error")
                                    return False
                         else:
                               print("error")
                     else:
                         print("input error")
                         return False

                  elif sp[0]=='K':
                     print("haven't done yet")
            else:                 #檢查吃的動作
                     print("haven't done yet")

    else:  #黑色
         if (x,y) in W.values() and sp[(len(sp)-3)] not in move:   #沒有x不能吃其他顏色的棋子
                print("You can't move to where a piece of other color is,if you don't say 'x'")
                return False
         elif (x,y) in D.values():	#不能移到同色棋子的位置
                print("You can't move into a square already containing one of your own pieces")
                return False

         if len(sp)==2:
         #檢查哪個p可以走到goto 若有兩個false
                if (x-1,y) in D.values():
                   if new_D[(x-1,y)] in pDark_firsttime:
                       pDark_firsttime[new_D[(x-1,y)]]=0         
                       return (x-1,y)
                elif (x-2,y) in D.values() and new_D[(x-2,y)] in pDark_firsttime:
                       if pDark_firsttime[new_D[(x-2,y)]]==0:
                            if (x-1,y) not in D.values() and (x-1,y) not in W.values():
                                 return (x-2,y)
                            else:
                                 print("No Pawn can move to there")
                                 return False
                       else:
                            print("Pawn can't move two squares at the first time")
                            return False
                else:
                       print("No Pawn can move to there")
                       return False
         else:
            if sp[(len(sp)-3)] in move:
             #檢查吃對方的動作有沒有出錯
                     print("haven't done yet")
            else:
                 if sp[0] in chess:
                     #檢查可否移動到那裡、 有沒有指定
                     print("haven't done yet")

	
def PlayGame(D,W):
 global color
 while True:
    #每個英文符號對應到的圖案
    loopnumber=['R1','N1','B1','Q','K','B2','N2','R2','p1','p2','p3','p4','p5','p6','p7','p8']
    Board_pic={'p1':"♟",'p2':"♟",'p3':"♟",'p4':"♟",'p5':"♟",'p6':"♟",'p7':"♟",'p8':"♟",'R1':"♜",'R2':"♜",'N1':"♞",'N2':"♞",'B1':"♝",'B2':"♝",'K':"♚",'Q':"♛"}
    B=[]
    White= W.values()
    for i in range(8):
        B+=[""]
    for i in range(8):
        for j in range(8):
             if (i,j)in W.values():
                 for n in range(16):
                      if W[(loopnumber[n])]==(i,j):
                           B[i]=B[i][:j+1]+Board_pic[(loopnumber[n])]
             elif (i,j)in D.values():
                 for n in range(16):
                      if D[(loopnumber[n])]==(i,j):
                           B[i]=B[i][:j+1]+Board_pic[(loopnumber[n])]
             else:
                 B[i]=B[i][:j+1]+" " 
    DrawBoard(B,White)	
    GetAMove(color)
    color+=1

PlayGame(D,W)
