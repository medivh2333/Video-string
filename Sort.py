from random import *


class SortAlogorithm:
    def display(self):
        pass
    def _sort_alogorithm(self):
        pass

class BubbleSort(SortAlogorithm):
    def __init__(self,list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        for i in range(len(self.l) - 1):
            for j in range(len(self.l) - 1 - i):
                if self.l[j] > self.l[j + 1]:
                    self.l[j], self.l[j + 1] = self.l[j + 1], self.l[j]
        return self.l

class SimpleselectSort(SortAlogorithm):
    def __init__(self,list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        for i in range(0, len(self.l)):
            min = i
            for j in range(i + 1, len(self.l)):
                if self.l[min] > self.l[j]:
                    min = j
            temp = self.l[min]
            self.l[min] = self.l[i]
            self.l[i] = temp
        return self.l

class SimpleInsertSort(SortAlogorithm):
    def __init__(self,list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        for i in range(1,len(self.l)):
            j = i - 1
            key = self.l[i]
            while j >= 0:
                if key < self.l[j]:
                    self.l[j+1] = self.l[j]
                    self.l[j] = key
                j -= 1
        return self.l

class ShellSort(SortAlogorithm):
    def __init__(self,list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        step = len(self.l) // 2
        while step > 0:
            for i in range(len(self.l)):
                if i + step < len(self.l):
                    index = self.l[i]
                    if index > self.l[i + step]:
                       self.l[i], self.l[i + step] = self.l[i + step], self.l[i]
            step //= 2
        else:
            for j in range(1, len(self.l)):
                k = j - 1
                key = self.l[j]
                while k >= 0:
                    if key < self.l[k]:
                        self.l[k + 1] = self.l[k]
                        self.l[k] = key
                    k -= 1
        return self.l

class BinarySort(SortAlogorithm):
    def __init__(self, list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        for i in range(1, len(self.l)):
            index = self.l[i]
            left = 0
            right = i - 1
            while left <= right:
                mid = (left + right) // 2
                if index > self.l[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            for j in range(i, left, -1):
                self.l[j] = self.l[j - 1]
            self.l[left] = index
        return self.l

class QuitSort(SortAlogorithm):
    def __init__(self, list):
        self.l = list

    def display(self):
        return self._sort_alogorithm()

    def _sort_alogorithm(self):
        if len(self.l) < 2:
            return self.l
        mid = self.l[len(self.l) // 2]
        left, right = [], []
        self.l.remove(mid)
        for item in self.l:
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        return QuitSort(left)._sort_alogorithm() + [mid] + QuitSort(right)._sort_alogorithm()

class MergeSort(SortAlogorithm):
    def __init__(self, list):
        self.l = list
        self.newl = []

    def display(self):
        return self._sort_alogorithm()


    def merge(self,left,right):
        i = j = 0
        while j < len(left) and i < len(right):
            if left[j] < right[i]:
                self.newl.append(left[j])
                j += 1
            else:
                self.newl.append(right[i])
                i += 1
        if j == len(left):
            for x in right[i:]:
                self.newl.append(x)
        else:
            for y in left[j:]:
                self.newl.append(y)
        self.newl = self.l
        return self.l

    def _sort_alogorithm(self):
        if len(self.l) <= 1:
            return self.l
        middle = len(self.l) // 2
        left = MergeSort._sort_alogorithm(self.l[:middle])
        right = MergeSort._sort_alogorithm(self.l[middle:])
        return MergeSort.merge(left, right)

selfl=[8, 6, 4, 2, 748, 132, 1]
a=MergeSort(selfl)
print(a.display())