#!/usr/bin/env python3
# test.py

import timeit


class BenchMark:
  def __init__(self) -> None:
      pass


  def measureTime(functionName):
    return timeit.Timer(functionName).timeit(number=2)


