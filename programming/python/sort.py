from benchmark import BenchMark
from collections import deque

listOfNums = [-2, 34, -5, 80, 20, 2, 5, 5, -10]

class sortNumbers:
  def __init__(self) -> None:
    pass


  def usingInBuilt(self) -> list:
    return sorted(listOfNums)

  
  def sortIt(self) -> list:
    sortedList = list()
    while listOfNums:
      firstNum = listOfNums[0]
      for num in listOfNums:
        if num < firstNum:
          firstNum = num
      sortedList.append(firstNum)
      listOfNums.remove(firstNum)
    return sortedList

  def queueSort(self) -> deque():
    q = deque()
    # while listOfNums:
    firstNum = listOfNums[0]
    for num in listOfNums:
      if num < firstNum:
        firstNum = num
        print('Appending left: {}. Reset number: {}'.format(num, firstNum))
        q.appendleft(num)
      else:
        q.append(num)
        print('Appending right: {}'.format(num))
      listOfNums.remove(num)
      print(q)
    # print(q)

  def getPert(self):
    print(BenchMark.measureTime(self.sortIt), BenchMark.measureTime(self.usingInBuilt))

# sortNumbers().getPert()
sortNumbers().queueSort()
