class Vector2D:
    def __init__(self, v: List[List[int]]):

        self.arr = []
        for i in range(0, len(v)):
            for j in range(0, len(v[i])):
                self.arr.append(v[i][j])
        self.start = 0

    def next(self) -> int:
        self.start += 1
        return self.arr[self.start - 1]

    def hasNext(self) -> bool:
        if self.start < len(self.arr):
            return True
        return False



        # Your Vector2D object will be instantiated and called as such:
        # obj = Vector2D(v)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()