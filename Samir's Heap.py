import copy

class Heap:
    def __init__(self, array: list[int]):
        self.array = array
        self.heap_size = len(array)

    def sort(self):
        for i in range(len(self.array)):
            self.array[0], self.array[self.heap_size - 1] = self.array[self.heap_size - 1], self.array[0]
            self.heap_size -= 1
            self.sift_down(0)

    def max(self):
        return self.array[0]

    def sift_up(self, start: int):
        current = start - 1
        while current > 0:
            parent = (current - 1) >> 1
            if self.array[current] > self.array[parent]:
                self.array[current], self.array[parent] = self.array[parent], self.array[current]
                current = parent
            else:
                break

    def sift_down(self, start):
        while 2 * start + 1 < self.heap_size:
            left_pos = 2 * start + 1
            right_pos = 2 * start + 2
            j = left_pos
            if right_pos < self.heap_size and self.array[right_pos] > self.array[left_pos]:
                j = right_pos
            if self.array[start] >= self.array[j]:
                break
            self.array[start], self.array[j] = self.array[j], self.array[start]
            start = j


    def insert(self, item: int):
        self.array.append(item)
        self.heap_size = self.heap_size + 1
        self.sift_up(self.heap_size)


    @staticmethod
    def create(array: list[int]):
        array = copy.deepcopy(array)
        heap = Heap(array)
        for i in range(len(array) // 2 - 1, -1,  -1):
            heap.sift_down(i)
        return heap


    def __repr__(self):
        return f"Heap(array={self.array!r})"




def main():
    array = [int(item) for item in input().split()]
    heap = Heap.create(array)
    heap.insert(11)
    heap.insert(12)
    heap.insert(9)
    print(heap)
    heap.sort()
    print(heap)



if __name__ == '__main__':
    main()