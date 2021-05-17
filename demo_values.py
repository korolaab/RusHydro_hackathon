import random
import datetime
import csv
import numpy as np 
with open("data.csv","r") as f:
    reader = csv.reader(f,delimiter=',')
    data=list(reader)
name = data[0]
N = len(data[0])
data = np.array(data[1:],dtype=np.object)
#print(data)
#exit()
start = datetime.datetime(2020, 7, 14, 12, 30)
end = datetime.datetime.now()
sensor_id=1
Mode=["PV power off","Wait","Normal"]
def output(d,j,v):
    if(name[j] =="Mode"):
        print("%s,%d,%s,%s"%(d.strftime("%Y-%m-%d %H:%M:%S"),sensor_id,name[j],Mode.index(v) ))
    else:
        print("%s,%d,%s,%s"%(d.strftime("%Y-%m-%d %H:%M:%S"),sensor_id,name[j],v))

while (start <= end):
    if(start.hour<=7 or start.hour>=20):
        out = data[1,0:]
        for i in range(1,N):
       #     print(out[i],end=',')
        #print(out[N-1])
            output(start,i,out[i])
    else:
        n = random.randint(784,885)
        out = data[n,0:]
        for i in range(1,N):
         #   print(out[i],end=',')
        #print(out[N-1])
            output(start,i,out[i])

    start = start + datetime.timedelta(minutes=5)

