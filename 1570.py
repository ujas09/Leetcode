class SparseVector:
    def __init__(self, nums: List[int]):
        self.tracnum = {}

        for i in range(0, len(nums)):
            if nums[i] != 0:
                self.tracnum[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        dot_product = 0

        for key in self.tracnum.keys():
            if key in vec.tracnum:
                dot_product += self.tracnum[key] * vec.tracnum[key]

        return dot_product


        # Your SparseVector object will be instantiated and called as such:
        # v1 = SparseVector(nums1)
        # v2 = SparseVector(nums2)
        # ans = v1.dotProduct(v2)