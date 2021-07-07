#!/usr/bin/env python3
# coding: utf8
# 複雑な初期化をしたいとき。
from dataclasses import dataclass, field
@dataclass
class MyData:
    name: str = field(init=False)
    def __post_init__(self):
        self.name = str(1+2+3)


if __name__ == "__main__":
    d = MyData()
    print(d.name)

