def sortedArrayToBST(self,nums: List[int]) -> Treenode:
    if not nums:
        return None

    mid = len(nums) //2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid+1:])