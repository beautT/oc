import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret,frame = cap.read()

L = len(frame)
W = len(frame[0])
print(L,W)

SIZE = 100
X0 = int(W/2-1.5*SIZE)
Y0 = int(L/2-1.5*SIZE)
R = int(SIZE/2)
chessboard = [[0,0,0],[0,0,0],[0,0,0]]
print(chessboard)

playsteps = 0

def mouse_dclick(event,x,y,flags,param):
    global  playsteps
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if x>X0 and y>Y0 and x<(X0+SIZE*3) and y<(Y0+SIZE*3):
            i=int((x-X0)/SIZE)
            j=int((y-Y0)/SIZE)
            if chessboard[i][j]==0:
                player = playsteps%2+1
                print("mc",player)
                chessboard[i][j]=player
                playsteps+=1
#            if event == cv2.EVENT_LBUTTONDBLCLK:
#                print("get L")
#                chessboard[i][j]=1
#            elif event==cv2.EVENT_RBUTTONDBLCLK:
#                chessboard[i][j]=2
#                print("get R")
        
# 创建图像与窗口并将窗口与回调函数绑定
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse_dclick)

while(True):
    ret,frame = cap.read()
    #画棋盘和棋子
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame,(i*SIZE+X0,j*SIZE+Y0),(i*SIZE+SIZE+X0,j*SIZE+SIZE+Y0),(255,128,255),2)
            if chessboard[i][j]==1:
                cv2.circle(frame,(i*SIZE+X0+R,j*SIZE+Y0+R),R,(255,0,0),-1)
            elif chessboard[i][j]==2:
                cv2.circle(frame,(i*SIZE+X0+R,j*SIZE+Y0+R),R,(255,0,0),3)
                
    cv2.imshow('frame',frame)
    winner = 0
    for i in range(3):
        counter1 = 0
        counter2 = 0
        for j in range(3): #遍历每行是否相等叠加
            if chessboard[i][j] == 1:
                counter1+=1
            elif chessboard[i][j]==2:
                counter2+=1
        if counter1==3:
            winner=1
            break
        elif counter2==3:
            winner=2
            break
    if winner !=0:
        print(winner)
        break
    for j in range(3):
        counter1=0
        counter2=0
        for i in range(3):
            if chessboard[i][j]==1:
                counter1+=1
            elif chessboard[i][j]==2:
                counter2+=1
        if counter1==3:
            winner=1
            break
        elif counter2==3:
            winner=2
            break
    if winner !=0:
        print(winner)
        break
            
            
    if cv2.waitKey(1000)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
