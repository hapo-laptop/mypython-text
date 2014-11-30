import random
import matplotlib.pyplot as plt

win,lose,draw,n=0,0,0,0

def cp(x,y):#compare the result
    global win,lose,draw
    if y ==x%3+1:
        print 'You Win'
        win+=1
    elif y ==(x%3-1)%3:
        print 'You Lost'
        lose+=1
    else:
        print 'it is draw'
        draw+=1

print '1:Rock 2:Scissors 3:Paper q:quit'
dic={1:'shitou',2:'jiandao',3:'bu'}
MyChoice=raw_input('please input the number:')
while True:#loop
    if MyChoice is 'q':#if the input is 'q',the game is over
        print 'Game Over'
        break
    elif type(eval(MyChoice)) is int:
        Choice=random.choice(range(3))+1
        cp(int(MyChoice),Choice)
        n+=1
    elif type(eval(MyChoice)) is tuple :
        for i in eval(MyChoice):
            Choice=random.choice(range(3))+1
            cp(i,Choice)
            n+=1
    else:
        print 'Your input has error'
    MyChoice=raw_input('please input the number:')
#plot
plt.bar(range(3),[float(win)/n,float(draw)/n,float(lose)/n],width=0.4,\
        color='r',align='center')
plt.xlabel('the result')
plt.ylabel('the scale')
plt.xticks(range(3),['win','draw','lose'])
plt.show()
