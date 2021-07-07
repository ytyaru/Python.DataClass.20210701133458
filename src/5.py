#!/usr/bin/env python3
# coding: utf8
# 疑似フィールド：初期化限定変数
from dataclasses import dataclass, field, InitVar
@dataclass
class MyData:
    name: InitVar[str] = ''
    def __post_init__(self, name):
        self.name = str(1+2+3)


if __name__ == "__main__":
    d = MyData()
    print(d.name)

