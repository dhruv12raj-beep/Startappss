'''Create a list of 10 numbers and count how many numbers are even and odd.'''

nums = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in nums:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(f"even's: {even} , odd's: {odd}")