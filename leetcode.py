class Solution:
    def removeDuplicates(self, nums):
        self.ans=[]
        self.k=0
        for i in  range(len(nums)):
            if nums[i]!=nums[i-1]:
                self.ans.append(nums[i])
                self.k+=1
        print(f"{self.k}, nums={self.ans}")
prueba=Solution()
prueba.removeDuplicates([1,1,2])
prueba.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
