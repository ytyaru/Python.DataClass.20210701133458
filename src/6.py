#!/usr/bin/env python3
# coding: utf8
# 疑似フィールド：クラス変数
from dataclasses import dataclass, field, InitVar
from typing import ClassVar
@dataclass
class MyData:
    Name: ClassVar[str] = 'ClassVar-Name'


if __name__ == "__main__":
    print(MyData.Name)
    d = MyData()
    print(d.Name)

