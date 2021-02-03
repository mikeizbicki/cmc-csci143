import os 
import time

time.sleep(10)

print('forking...')

n = os.fork() 

time.sleep(10)

if n > 0:
    print('parent process: n='+str(n)+', pid='+str(os.getpid()))
elif n==0:
    print('child process: n='+str(n)+', pid='+str(os.getpid()))
else:
    print('could not fork')


