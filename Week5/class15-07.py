# #performance profile: performance proile is the process
# # of measurung where a program spends its execution time and memory.

# # optimization: it is the process of improving the speed and efficiency of the code.

# import cProfile

# def square():
#     total = 0 
#     for i in range(100000):
#         total+= i*i

# cProfile.run("square()")

# def factorial(n):
#     if n ==1:
#         return 1 
    
#     return n*factorial(n-1)

# cProfile.run("factorial(20)")


#2 line profile: it measures executioin time line by line inside a funtion 

# from line_profiler import profile

# @profile
# def square():
#     total = 0
#     for i in range(1000000):
#         total += i*i
#     return total

# n = square()
# print(n)



#hits: total number of time that line hit
#time: total execution time spednt on that line
#per hit:  average time spent per execution of the line
#time: tie persentage of the total function's line
#line contents: code of particular line

#3 py-spy: it is an external profiler that can inspect a running 
# python program witthout modifying its source code

# why use py-spy:
# doesn't require adding profiling code
# can profile a running python process 
# shows CPU bottleneck Problems
# very low performance


# import time

# def fast_fun():
#     time.sleep(0.01)


# def slow_bottleneck_function():
#     total = 0 
#     for i in range(1000000):
#         total+=i
#     return total

# def main():
#     print("start progran")
#     while True:
#         fast_fun()
#         slow_bottleneck_function()
