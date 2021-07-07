#!/usr/bin/env python3
# coding: utf8
# 疑似フィールド：クラス変数
from dataclasses import dataclass, field, InitVar
from typing import ClassVar
@dataclass(frozen=True)
class MyData:
    name: str = ''
    age: int = 0


if __name__ == "__main__":
    a = MyData()
    del a.name
