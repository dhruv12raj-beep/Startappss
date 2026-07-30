from collections import *

# text = "banana"
# c= Counter(text)
# print(list(c.elements()))

# dd = defaultdict(list)

# dd["A"].append(40)
# dd["A"].append(40)
# print(dd)

# dd  = defaultdict(int)
# dd["A"] = 2
# dd["A"] += 1
# print(dd)

# dd = defaultdict(float)
# dd["B"]=0.1
# print(dd)

# dd = defaultdict(str)
# dd["C"] = "hello bhai kya haal chal"
# dd["B"] = "welcome"
# dd.pop("C")
# print(dd)

# d = deque()

# d.append(10)
# d.append(10)
# d.append(10)

# d.appendleft(5)

# d.pop()

# d.popleft()
# d.popleft()
# print(d)


# t = (10,20)
# print(t[0])


# from collections import ChainMap 

# defaults = {"theme": "light", "language": "English"} 

# user = {"theme": "dark"} 

# settings = ChainMap(user, defaults) 
# print(settings)
# print(settings["theme"])
# print(settings["language"])

# print(settings["theme"]) 

# print(settings["language"])



# nt = namedtuple("mytuple","a b c")

# obj = nt(1,2,3)
# print(obj.a)
# print(obj.b)
# print(obj.c)

# # from collections import *
# class UpperString(UserString): 
#     def __init__(self, text): 
#         super().__init__(text.upper())

#     def reverse(self):
#         return self.data[::-1]

# s = UpperString("heelo dhruv")
# print(s.reverse())
# print(s)

# class LowerCaseDict(UserDict):
#     def __setitem__(self,key,value):
#         self.data[key.lower()] = value

# lower = LowerCaseDict()
# lower["DHRUV"] = 23
# print(lower)


# class AllowOnlyInt(UserDict):

#     def __setitem__(self,key,value):
#         if not isinstance(value , int):
#             raise ValueError("key must be integer")
#         self.data[key] = value

# allow = AllowOnlyInt()
# allow["dhruv"] = 100
# print(allow)


# class OnlyPositive(UserList):
    
#     def append(self,item):
#         if item <0:
#             raise ValueError("values must be positive")

#         self.data.append(item)

# o = OnlyPositive()
# o.append(10)
# o.append(10)
# o.append(10)
# o.append(-7)
# print(o)

# class DoubleNumber(UserList):

#     def append(self,value):
#         super().append(value*2)

# d = DoubleNumber()
# d.append(10)
# d.append(10)
# d.append(10)
# print(d)



# sentence = "python java python c java python"

# words = sentence.split()

# count = Counter(words)
# print(count)

# for key , value in count.items():
#     if value >1:
#         print(key)

# students = [ ("IT","Rahul"), ("HR","Aman"), ("IT","Priya"), ("Finance","Riya"), ("HR","Karan") ]

# dd = defaultdict(list)

# for key , value in students:
#     dd[key].append(value) 

# print(dd)


# employees = [
# ("IT","Rahul"),
# ("IT","Aman"),
# ("HR","Priya"),
# ("HR","Rohit"),
# ("IT","Raj")
# ]

# dd = defaultdict(int)

# for key , value in employees:
#     dd[key] += 1

# print(dd)


# '''Remove Last 5 Browsing History Items

# Implement browser history.

# Operations

# Visit
# Back

# Use: deque'''


# class History:

#     def __init__(self):
#         self.history = deque(maxlen=5)

#     def visit(self,url):
#         self.history.append(url)
#         print(f"VIsited : {url}")

#     def back(self):
#         if self.history:
#             print(f"removed {self.history.pop()}")
#         else:
#             print("not history")

#     def show(self):
#         print(self.history)


# history = History()

# history.visit("Google.com")
# history.visit("Amazon.com")
# history.visit("Myntra.com")
# history.visit("YOutube.com")
# history.visit("Flipkart.com")
# history.visit("myntra.com")
# history.visit("myntra.com")
# history.show()


# '''Reverse Queue

# Given a deque

# deque([1,2,3,4,5])

# Reverse it using only deque methods.'''

# dd= deque([1,2,3,4,5])

# newdd = deque()

# newdd.append(dd.pop())
# newdd.append(dd.pop())
# newdd.append(dd.pop())
# newdd.append(dd.pop())
# newdd.append(dd.pop())

# print(newdd)

# '''Given

# nums = [1,2,3,4,5,6]
# k = 3

# Print every window.

# Output

# [1,2,3]

# [2,3,4]

# [3,4,5]

# [4,5,6]'''

# dd = deque()
# nums = [1,2,3,4,5,6]
# k = 3 

# for i in range(len(nums)-k+1):
#     print(nums[i:i+k])

# '''Word Frequency in File

# Read a text file and print

# Top 10 words
# Total unique words'''


# with open("text.txt","r") as file:
#     text = file.read()
    
# words = text.split()
# counts = Counter(words)

# for word , count in counts.most_common(10):
#     print(f"{word}: {count}")
# print(len(counts))


# '''Q10. Group Orders Customer-wise

# Input

# orders = [
# ("Rahul","Laptop"),
# ("Rahul","Mouse"),
# ("Aman","Keyboard"),
# ("Rahul","Monitor"),
# ("Aman","Mouse")
# ]

# Output
# Rahul
# Laptop
# Mouse
# Monitor
# Aman
# Keyboard
# Mouse
# Use: defaultdict(list)'''

# orders = [
# ("Rahul","Laptop"),
# ("Rahul","Mouse"),
# ("Aman","Keyboard"),
# ("Rahul","Monitor"),
# ("Aman","Mouse")
# ]


# dd = defaultdict(list)

# for key , value in orders:
#     dd[key].append(value)

# # print(dd)

# '''Log Analyzer

# Read a log file.

# Print

# ERROR count
# INFO count
# WARNING count'''

# c= Counter() 

# with open("log.txt", "r") as file:
#     for line in file:
#         level = line.split()[0]
#         c[level] +=1

# print(c)
    

# '''Recent 20 Logs

# Store only the latest 20 logs.

# Older logs should automatically be removed.

# Use: deque(maxlen=20)'''


# class Logs:

#     def __init__(self):
#         self.logs = deque(maxlen=10)

#     def add_log(self,log):
#         self.logs.append(log)

#     def show(self):
#         return self.logs
    
# log = Logs()

# log.add_log("info")
# log.add_log("info")
# log.add_log("info")
# log.add_log("warning")
# log.add_log("warning")
# log.add_log("Critical")
# log.add_log("Critical")
# log.add_log("warning")
# log.add_log("warning")
# log.add_log("error")
# log.add_log("error")
# log.add_log("INFO")

# # print(log.show())

# '''Q14. Group Logs Date-wise
# Input
# 2026-07-21 ERROR
# 2026-07-21 INFO
# 2026-07-22 WARNING
# 2026-07-22 ERROR
# Output
# 2026-07-21
# ERROR
# INFO
# 2026-07-22
# WARNING
# ERROR
# Use: defaultdict(list)'''


# logs = [
#     "2026-07-21 ERROR",
#     "2026-07-21 INFO",
#     "2026-07-22 WARNING",
#     "2026-07-22 ERROR"
# ]

# grouped_logs = defaultdict(list)

# for log in logs:
#     date , info = log.split()
#     grouped_logs[date].append(info)

# print(grouped_logs)

# '''Playlist

# Implement

# Next Song
# Previous Song

# using deque.'''


# class Playlist:

#     def __init__(self):
#         self.dd = deque()

#     def play(self,song):
#         self.dd.append(song)

#     def current(self):
#         return self.dd[0]

#     def next(self):
#         self.dd.rotate(-1)
#         return self.dd[0]
    
#     def previous(self):
#         self.dd.rotate(1)
#         return self.dd[0]
    

# p = Playlist()
# p.play("beliver")
# p.play("shape of you ")
# p.play("perfect")
# p.play("faded")

# print(p.current())
# print(p.next())
# print(p.previous())


# ''' Implement LRU Cache

# Capacity = 3

# Operations

# put()

# get()

# When full,

# remove least recently used item.

# Use: OrderedDict'''

# class LRU:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.od = OrderedDict()

#     def put(self,key,value):
#         self.od[key] = value
        
#         if len(self.od) > self.capacity:
#             self.od.popitem(last=False)

#     def get(self,key):
#         self.od.move_to_end(key)
#         print(self.od[key])

#     def show(self):
#         print(self.od)

        
# cache = LRU(3)
# cache.put("sad",90)
# cache.put("aizen",20)
# cache.put("megh",30)
# cache.put("dhruv",10)
# cache.get('aizen')
# cache.get("dhruv")
# cache.put("open",100)
# cache.show()



# Given

# defaults = {
# "theme":"light",
# "font":"Arial"
# }

# user = {
# "theme":"dark"
# }

# If the key exists in user, use it; otherwise use defaults.

# Use: ChainMap

# defaults = {
#  "theme":"light",
#  "font":"Arial"
#  }

# user= {"theme": "dark"}

# cn = ChainMap(defaults,user)
# print(cn.user["theme"])

# '''Create
# Student
# name
# age
# course
# using namedtuple.
# Print
# student.name
# student.course'''


# # nt = namedtuple("student","name age course")
# # student = nt("dhruv",23,"python")
# # print(student.age)
# # print(student.course)

# Validate Dictionary

# Create a class using UserDict.

# Conditions

# Keys must be strings.
# Values must be integers.

# Raise ValueError otherwise.

# class MYdict(UserDict):
#     def __setitem__(self, key, item):
#         if not isinstance(key,str): 
#             raise ValueError("Key must be string")
#         if not isinstance(item, int):
#             raise ValueError("Values must be integer")
        

#         super().__setitem__(key,item)
    

# my = MYdict()
# my["dhruv"] = 23
# my["helo"] ="asd"
# print(my)


# '''Positive Number List

# Create a custom list using UserList.

# Rules

# No negative numbers.
# No duplicate values.'''


# class Mylist(UserList):

#     def append(self,value):
#         if value < 0:
#             raise ValueError("value must be positive")
        
#         if value in self.data:
#             raise ValueError("value can not be duplicate")
        
#         super().append(value)

# my = Mylist()

# my.append(-10)
# my.append(20)
# print(my)

# class Upper(UserString):

#     def __init__(self, seq):
#         super().__init__(seq.upper())

# upper = Upper("hello")
# print(upper)

from dataclasses import dataclass , field , asdict, replace


# Create a Book dataclass with title, author, and price.
# Validate that price > 0 using __post_init__().

# @dataclass(frozen=  True)
# class Book:
#     title : str
#     author : str
#     price : int

#     def __post_init__(self):
#         if self.price < 2000:
#             raise ValueError("Price must be greater than 2000")

# b= Book("marvel", "stan lee", 2012)
# print(b.author)
# b.price = 9873
# print(b.price)
# print(b)

# @dataclass()
# class Student:
#     subjects: list = field(default_factory=list)


# obj1 = Student()
# obj1.subjects.append("django")
# obj1.subjects.append("fastapi")
# obj1.subjects.append("fastapi")
# print(obj1)

# obj2 = Student()
# obj2.subjects.append("sql")
# obj2.subjects.append("mongodb")
# print(obj2)

# print(asdict(obj1))


# @dataclass
# class ABC:

#     x : int
#     y : int 


# abc = ABC(3,5)
# asd = replace(abc, y=99)
# print(asd)
# print(abc)


# Use slots=True and demonstrate that adding a new attribute raises an AttributeError.

# @dataclass(slots=True)
# class Student:
#     name : str
#     age : int 
#     marks : int


# std = Student("dhruv",23, 99)
# std.language = "python"
# print(std)


# Create a nested dataclass (Department containing a list of Employee objects).

# @dataclass
# class Employee:
#     name : str
#     salary : int

# @dataclass
# class Department:
#     employee : list[Employee] = field(default_factory=list)


# emp1= Employee("dhruv", 90000)
# emp2= Employee("aizen", 70000)

# d = Department()
# d.employee.append(emp1)
# d.employee.append(emp2)
# print(d)



import asyncio 

# async def main():
#     print("starting....")
#     await asyncio.sleep(2)
#     print("done!") 

# asyncio.run(main())


# implement two coroutines that run seqentally. 

# async def task1():
#     print("task 1 started")
#     await asyncio.sleep(3)
#     print("task 1 finished")

# async def task2():
#     print("task 2 started")
#     await asyncio.sleep(2)
#     print("task 2 finished")


# async def main():
#     await asyncio.gather(task1(), task2())


# asyncio.run(main())


# async def download_file():
#     print("downloading file")
#     await asyncio.sleep(3)
#     print("file downloaded")


# async def send_email():
#     print("sending email")
#     await asyncio.sleep(3)
#     print("email sent ")

# async def update_logs():
#     print("updating logs")
#     await asyncio.sleep(3)
#     print("logs updated ")


# async def main():
#     task1 = asyncio.create_task(download_file())
#     task2 = asyncio.create_task(send_email())
#     task3 = asyncio.create_task(update_logs())
#     print("main function running")

#     await task1
#     await task2
#     await task3

#     print("tasks finished")

# asyncio.run(main())


# async def download_image(image_name):
#     await asyncio.sleep(2)
#     print(f"downloaded image:{image_name}")

# async def main():

#     tasks = []

#     for i in range(1,6):
#         tasks.append(download_image(f"image_name{i}"))

#     await asyncio.gather(*tasks)

# asyncio.run(main())
    


# async def download_image(img_name):
#     await asyncio.sleep(2)
#     print(f"{img_name} image downloaded")

# async def main():

#     tasks = []

#     for i in range(1,6):
#         tasks.append(download_image(f"image {i}"))

#     await asyncio.gather(*tasks)
# asyncio.run(main())



# async def weatherapi():
#     await asyncio.sleep(1)
#     return "28'c , sunny"

# async def newsapi():
#     await asyncio.sleep(1)
#     return "todays headline"

# async def mapsapi():
#     await asyncio.sleep(1)
#     return "trafiic is normal"

# async def main():

#     weather , news , maps = await asyncio.gather(weatherapi(), newsapi(), mapsapi())

#     result = {"weather": weather,
#               "news": news,
#               "maps": maps}
    
#     print(result)

# asyncio.run(main())


# balance = 1000
# lock = asyncio.Lock()

# async def deposit(amount):
#     global balance

#     async with lock:
#         print(f"depositing: {amount}")
#         await asyncio.sleep(1)

#         balance += amount 
#         print(f"balance after depositing {amount} is {balance}")

# async def main():

#     await asyncio.gather(deposit(500),
#                           deposit(1000))

# asyncio.run(main())


# balance = 1000
# lock = asyncio.Lock()


# async def deposit(amount):
#     global balance
#     print(f" {amount} will be deposited ")

#     async with lock:
#         await asyncio.sleep(2)
#         balance +=amount

#         print(f"balance after depoit {amount} will be: {balance}")


# async def main():
#     await asyncio.gather(deposit(500), deposit(1000))
#     print(balance)

# asyncio.run(main())


# semaphore = asyncio.Semaphore(5)

# async def requests(user_id):
#     async with semaphore:
#         print(f"fetching : {user_id}")
#         await asyncio.sleep(4)
#         print(f"fetched : {user_id}")

# async def main():
#     tasks = []

#     for i in range(1,21):
#         tasks.append(requests(f"user_id:{i}"))

#     await asyncio.gather(*tasks)


# asyncio.run(main())


# from enum import Enum

# class TrafficLight(Enum):
#     Red  = "RED"
#     Yellow = "Yellow"
#     Green = "Green"

    
    
# def can_go(light):
#     if light == TrafficLight.Red:
#         return "Stop"
    
#     if light == TrafficLight.Yellow:
#         return "Wait"
    
#     if light == TrafficLight.Green:
#         return "GO"
    
# from enum import Enum

# class Animal(Enum):
#     DOG = 1
#     CAT = 2

# print(Animal(2))


# from enum import Enum

# class Animal(Enum):
#     DOG = 1

# print(Animal["DOG"])


# from enum import Enum

# class Animal(Enum):
#     DOG = 1

# print(Animal.DOG == 1)


# import time 

# def work():
#     print("starting..")
#     time.sleep(5)
#     print("finished.")

# work()
# print("main program finished")

# from threading import Thread
# import time

# def work():
#     print("starting")
#     time.sleep(5)
#     print("finished")


# t = Thread(target= work)
# t.start()
# print("main program finished")

# from threading import Thread
# import time 

# def hello():
#     print("hello")

# t = Thread(target = hello)

# print("before start")

# t.start()

# print("after start ")

# from threading import Thread
# import time

# def work(number):
#     print(f"start {number}")
#     time.sleep(5)
#     print(f"ends {number}")


# for i in range(6):
#     thread = Thread(target=work,args=(i,))
#     thread.start()


# print("finished main program")

# from threading import Thread
# import time

# def task():
#     print("Task Started")
#     time.sleep(2)
#     print("Task Finished")

# t = Thread(target=task)

# print("A")

# t.start()

# print("B")

# print("C")


# from threading import Thread
# import time

# def work():
#     print("start")
#     time.sleep(5)
#     print("end")

# t = Thread(target=work)

# t.start()
# t.join()

# print("main function ends")

# from threading import Thread
# import time

# def task(name,delay):
#     print(f"{name} start")
#     time.sleep(delay)

# t1 = Thread(target= task,args=("A",3))
# t2 = Thread(target= task,args=("B",1))
# t3 = Thread(target= task,args=("C",2))

# t1.start()
# t2.start()
# t3.start()

# t3.join()
# print("Main After C")

# t1.join()
# print("Main After A")

# t2.join()
# print('Done')


# from threading import Thread
# import time


# def something():
#     print("start")
#     time.sleep(5)
#     print("end")

# t = Thread(target= something)
# t.daemon = True
# t.start()

# print("program ends")


# from threading import Thread , Lock 

# l = Lock()
# counter = 0


# def work(n):
#     global counter

#     for _ in range(n):
#         with l:
#             counter+=1

# t1 = Thread(target= work,args= (2000,))
# t2= Thread(target= work,args= (1000,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter)

# # print("program ends here......")

# from threading import Thread, Lock 
# import time

# l = Lock()

# def work(name):
#     print(f"{name} wants lock")

#     with l:
#         print(f"{name} aquires lock")
#         time.sleep(5)
#         print(f"{name} releases lock")


# t1 = Thread(target=work,args=("A"))
# t2 = Thread(target=work,args=("B"))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("main program ends")

# ##################################################################################################################

# from threading import Thread , Lock
# import time 

# lock = Lock()

# def work(name):
#     print(f"{name} waiting")

#     with lock:
#         print(f"{name}  entered")
#         time.sleep(3)
#         print(f"{name}  exits....")


#     print(f"{name} finished")


# t1 = Thread(target=work, args = ("A"))
# t2 = Thread(target=work, args = ("B"))

# t1.start()
# time.sleep(0.5)
# t2.start()

# t1.join()
# t2.join()

# #a waiting
# # A entered 
# # b waiting 
# # b entered
# # 


# from threading import RLock , Lock

# lock = RLock()

# def outer():
#     with lock:
#         print("A1")
#         inner()
#         print("A2")

# def inner():
#     with lock:
#         print("inner function")

# outer()


# from threading import Thread, Semaphore
# import time

# sem = Semaphore(2)

# def task(name):
#     print(f"{name} waiting")

#     with sem:
#         print(f"{name} entered")
#         time.sleep(10)
#         print(f"{name} leaving")

# for i in range(2):
#     Thread(target=task, args=(f"T{i}",)).start()


# from concurrent.futures import ThreadPoolExecutor
# import time 

# nums = [1,2,3,4,5,6]

# def square(n):
#     time.sleep(2)
#     return n*n


# with ThreadPoolExecutor(max_workers=4) as executor:

#     t1 = executor.map(square, nums)

# print(list(t1))


from concurrent.futures import ThreadPoolExecutor
import time 

def task(name, sec):
    print(f"{name} started")
    time.sleep(sec)
    print(f"{name} ends")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task,"A",3)
    executor.submit(task,"B",1)
    executor.submit(task,"C",2)
    