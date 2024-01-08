class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)<2:
            return arr[0]
        f = len(arr)//4
        if len(arr) % 2 == 0:
            f+=0.5
        l = 1
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    l+=1
            if l>f:
                return arr[i]
            else:
                l = 1
                