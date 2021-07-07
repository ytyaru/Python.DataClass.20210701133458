#!/usr/bin/env python3
# coding: utf8
# 疑似フィールド：クラス変数
from dataclasses import dataclass, field, InitVar
@dataclass(frozen=True)
class MyData:
    name: InitVar[str] = ''
    age: int = 0
    def __post_init__(self, name):
#        self.name = name # dataclasses.FrozenInstanceError: cannot assign to field 'name'
        object.__setattr__(self, 'name', '初期値')


if __name__ == "__main__":
    a = MyData()
    print(a.name)
