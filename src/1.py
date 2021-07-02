#!/usr/bin/env python3
# coding: utf8
# https://docs.python.org/ja/3.7/library/dataclasses.html
# https://docs.python.org/ja/3/library/stdtypes.html
# https://www.python.org/dev/peps/pep-0484/
from dataclasses import dataclass, field
import typing 
from typing import Any, Callable, Iterable, Tuple, Optional, List, Tuple, Dict, ClassVar, Union, TypeVar, NewType, Sequence
from decimal import Decimal
from pathlib import Path 
#import re

T = TypeVar('T', int, str)
Id = NewType('Id', int)
@dataclass
class MyData:
    any: Any = None
    name: str = ''
    group: chr = 'A'
    fix_data: bytes = b''
    data: bytearray = b''
    mem: memoryview = b''
    age: int = 0
    rate: float = 0.0
    img: complex = 0j
    dec: Decimal = Decimal(0.00)
    is_dead: bool = False
    r: range = range(0,9,1)
    oi: Optional[int] = None
    pattern: typing.re.Pattern = None
    match: typing.re.Match = None
    path: Path = None
    l: List[str] = field(default_factory=list)
    d: Dict[str, str] = field(default_factory=dict)
    t: Tuple[int, float, str] = field(default_factory=tuple)
    c: ClassVar[str] = 'クラス変数'
    u: Union[int, str] = 'int | str どちらでもよい'
    t: type = None
    tv: T = None
    id: Id = 0
    s: Sequence[int] = field(default_factory=list)
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
        func()
        print('end')

d = MyData()
d.name = 'Yamada'
d.img = 3+1j
print(f"{d.name}, {d.age}, {d.img}")
print(d.intro())
