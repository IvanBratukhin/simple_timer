import time 
print ("О чем вам напомнить? ")
text=str(input())
print("Через сколько напомнить? ")
local_time=float(input())
time.sleep(local_time)
print(text)
