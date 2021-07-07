#!/usr/bin/env python3
# coding: utf8
# ValueErrorになる。コレクション型はfieldによる初期化をせねばならない。
from dataclasses import dataclass, field

@dataclass
class MyData:
    l: list = []
    d: dict = {}
    t: tuple = ()
    s: set = set()
#    l: list = field(default_factory=list)
#    d: dict = field(default_factory=dict)
#    t: tuple = field(default_factory=tuple)
#    s: set = field(default_factory=set)


if __name__ == "__main__":
    d = MyData()

