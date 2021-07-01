import threading,time

def function():     
    print("Printing for thread", t)
    time.sleep(0.0002)
    print("Woke up",t) 


thread=[]
for x in range(100):
    thread.append("T"+str(x))
t=0
for i in thread:
    t=i
    t = threading.Thread(target=function )
    t.start()
 