# ✅ Manual Heap Implementation (No heapq)
# 📚 Core educational heap structure with min/max toggle

class Heap:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def compare(self, a, b):
        return a < b if self.is_min_heap else a > b

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.compare(self.heap[i], self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return top

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            best = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.compare(self.heap[left], self.heap[best]):
                best = left
            if right < n and self.compare(self.heap[right], self.heap[best]):
                best = right
            if best == i:
                break
            self.heap[i], self.heap[best] = self.heap[best], self.heap[i]
            i = best

    def peek(self):
        return self.heap[0] if self.heap else None

    def build_heap(self, arr):
        self.heap = arr[:]
        for i in range((len(self.heap) - 1) // 2, -1, -1):
            self._sift_down(i)


# 🔁 Usage Examples:
if __name__ == "__main__":
    print("-- MinHeap --")
    h = Heap(is_min_heap=True)
    h.build_heap([5, 3, 8])
    h.push(2)
    print(h.pop())  # 2

    print("-- MaxHeap --")
    h = Heap(is_min_heap=False)
    for val in [5, 3, 8]:
        h.push(val)
    print(h.peek())  # 8
