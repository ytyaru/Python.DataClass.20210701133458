#!/usr/bin/env python3
# coding: utf8
# https://docs.python.org/ja/3.7/library/dataclasses.html
# https://docs.python.org/ja/3/library/stdtypes.html
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Tuple, Optional
from decimal import Decimal

@dataclass
class MyData:
    '''Class for keeping track of an item in inventory.'''
    any: Any = None
    name: str = ''
    group: chr = 'A'
    fix_data: bytes = b''
    data: bytearray = b''
    mem: memoryview = b''
    age: int = 0
    rate: float = 0.0
    img: complex = 0.0
    dec: Decimal = 0.0
    is_dead: bool = False
    r: range = range(0,9,1)
    oi: Optional[int] = None
#    d: dict = {}
#    l: list = []
#    t: tuple = (,)
#    s: set = set([1,2,3,4,5])
#    fs: frozenset = frozenset([1,2,3,4,5])
#    gl: list[int] = []
#    gd: dict[str, int] = {}
    def intro(self) -> str: return f'My name is {self.name}.'
    def wrap(self, func: Callable[[],None]) -> None:
        print('start')
        print('end')

d = MyData()
d.name = 'Yamada'
d.img = 3+1j
print(f"{d.name}, {d.age}, {d.img}")
print(d.intro())
