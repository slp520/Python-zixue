#coding=utf-8
from time import sleep,ctime
import threading

def music(func):
    for i in range(2):
        print ('Start Playing:%s!%s'%(func,ctime()))
        sleep(3)

def movie(func):
    for i in range(2):
        print('Start Playing:%s!%s' %(func, ctime()))
        sleep(5)

def player(name):
    r=name.split('.')[1]
    if r=='mp3':
        music(name)
    elif r=='mp4':
        movie(name)
    else:
        print("error,The name can not find!")

list=['忘情水.mp3','阿凡达.mp4']
threads=[]
files=range(len(list))
for i in files:
    t=threading.Thread(target=player,args=(list[i],))
    threads.append(t)

if __name__=='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

print ('end:%s' %ctime())