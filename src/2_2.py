#!/usr/bin/env python3
# coding: utf8
class MyData: pass


d = MyData()
d.__x = 'x'
print(d.__x)
print(d._MyData__x) # AttributeError: 'MyData' object has no attribute '_MyData__x'
