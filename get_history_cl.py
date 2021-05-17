import json
from datetime import datetime
import requests
import subprocess
with open("/root/openweather.key","r") as f:
    key = f.read()
key = key[:-1]
latt = 55.755159
long = 37.709212



query = '''clickhouse-client -d solar --password RusHydro -q" SELECT
    sum(x)/12/1000 as Generated_Energy
FROM solar.telemetry
WHERE toDate(t)=toDate(subtractDays(now(),1)) and x>0 and parameter_name like '%AC Power%' and id==1"
'''


string_data=requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly,alerts&appid={}".format(latt,long,key)).text
data = json.loads(string_data)
E_cur = float(subprocess.Popen(query,stdout=subprocess.PIPE,shell=True).stdout.read())
#print(data)
t_cur =data["current"]["sunrise"] - data["current"]["sunset"]
t_tom = data["daily"][1]["sunrise"] - data["daily"][1]["sunset"]
clouds_cur =data["current"]["clouds"]
clouds_tom = data["daily"][1]["clouds"]
#print(t_cur)
#print(t_tom)
#print(clouds_cur)
#print(clouds_tom)
#print(E_cur)
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),end=',')
print("1,Generation_prediction",end=',')
print("%f"%(E_cur*t_tom/t_cur*(1+clouds_cur)/(1+clouds_tom)),end=',')
