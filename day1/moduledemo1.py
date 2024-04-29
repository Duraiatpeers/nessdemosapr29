from calculator import add as addition
import platform
import math
import sys
import os

def demo(n1,n2):
    result = addition(n1,n2)
    print(result)

demo(20,30)

print(platform.uname())
print(platform.node())

print(platform.python_version())

print(math.sin(90))
print(math.tan(45))
print(math.cos(0))
print(math.pi)

print(sys.path)

print(os.getcwd())
print(type(os.listdir()))