#!/usr/bin/env python3
# coding: utf8
from dataclasses import dataclass, field, InitVar
@dataclass
class A:
    name: str = ''
@dataclass
class B(A):
    age: int = 0
@dataclass
class C(B):
    name: str = '山田'


if __name__ == "__main__":
    c = C()
    print(c.name)

