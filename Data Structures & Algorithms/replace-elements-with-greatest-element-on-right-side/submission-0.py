class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]

        for i in range(len(arr)-2, -1,-1):
            if arr[i] > greatest:
                arr[i], greatest = greatest, arr[i]
            else:
                arr[i] = greatest

        arr[-1] = -1

        return arr
