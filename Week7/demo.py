#unit test it is a process  of testing the smallest unit of code (usually a function or method)
# independently  to ensure it work correctly 
# integration testing: Test multiple modules /files together
#  System Testing: whole appliction 
# End to End Testing ; form start to end test

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(add(5,2))


# Common Assertions:
# 1 AssertEqual : compare two values are equal
#2 assertNotEqual()
#3 assertTrue
#4 assertFalse
#5 assertIs 6. assertIsNot() 7. assertIn() 8.assertNOtIn()
# 9. assertRaises()
# 10. assertGreater(), assertLess(), assertGreaterEqual , assertLessEqual

# assertRegex()

#pytest: pytest is a powerful framework used to perform testing efficiently.