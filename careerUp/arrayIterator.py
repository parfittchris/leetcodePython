# Given K sorted(ascending) arrays with N elements in each array, implement an iterator for iterating over the elements of the arrays in ascending order.

# The constructor receives all of the input as array of arrays.

# You need to implement the MyIterator class with a constructor and the following methods:


# class MyIterator < T > {
# 	T next()
# 	boolean hasNext()
# }


# You are allowed to use only O(K) extra space with this class.



class MyIterator:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr) * len(arr[0])
        self.current_length = 0
        self.current_val = float("inf")

    def nextItem(self):
        if self.has_next() == False:
            return False

        next_val = self.current_val
        idx = 0

        for i in range(len(arr)):
            if self.current_val == float("inf") or self.arr[i][0] > self.current_val:
                if next_val > self.arr[i][0]:
                    next_val = self.arr[i][0]
                    idx = i

            i += 1

        self.current_length += 1
        self.arr[idx].pop(0)

        if len(self.arr[idx]) == 0:
            self.arr.pop(idx)

        return next_val

    def has_next(self):
        return self.current_length < self.length


arr = [[1, 5, 7], [2, 4, 6], [7, 9, 10]]
test = MyIterator(arr)
print(test.nextItem())
