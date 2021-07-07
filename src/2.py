#!/usr/bin/env python3
# coding: utf8
# dataclassはマングリングされない。
from dataclasses import dataclass

@dataclass
class MyData:
    __private_prop: str = ''


if __name__ == "__main__":
    d = MyData()
    d.__private_prop = 'Yamada'
    print(d._MyData__private_prop)
    print(d.__private_prop)

