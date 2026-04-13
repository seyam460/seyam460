import collections
#print(collections.__doc__)
from collections import defaultdict as dct
fruits = ['banana' ,'apple', 'orange' , 'pineapple']
#print(collections.Counter(fruits))
#print(collections.Counter(fruits).most_common(2))

word_dict = dct(list)
word_dict['python'].append('programming language')
print(word_dict)

# date-time module practice :
import datetime 
now = datetime.datetime.now()
today_time = datetime.date.today()
today_Time = datetime.datetime.now().time()
custom_datetime = datetime.datetime(2030,2,20, 10,30,0)
print(custom_datetime)
print(today_Time)
print(today_time)
print(now)

formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted_date)

#ate_str = "24-12-2030 10:34:00"
#parsed_date = datetime.datetime.strptime(date_str, "%")
#print(parsed_date)
#print(type(parsed_date))
#print(type(formatted_date))

from datetime import datetime , timedelta 

today =datetime.today().date()
tomorrow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)
#now = datetime.today()
#new_time = now + timedelta(hours = 5 , minitues = 30)
print(today , tomorrow , yesterday)
#print(now , new_time)

date1 = datetime(2025 ,12 ,4)
date2 = datetime(2025 , 12 ,3)
print(date1 - date2)

#import pytz,  datetime
#dhaka = pytz.timezone('Asia/Dhaka')
#utc = datetime.datetime.now(datetime.UTC)
#print(dhaka , utc)

#json practice: python to json
import json

data = {
    'name' : 'Rakib',
    'age': 30,
    'is_logged_in' : True,
    'test' : None
}
json_string = json.dumps(data , indent = 4)
print(json_string)

# json to python: deserialization 

data = '{"name" : "Rakib","age": 30,"is_logged_in" : true}'
python_dict = json.loads(data)
print(python_dict)

#CRUD operations:
# C --> create : post
# R --> read/retrieve : get
# U --> update : put/patch
# D --> delete : delete

