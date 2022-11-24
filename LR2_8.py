'''
- [2418. Sort the People](https://leetcode.com/problems/sort-the-people/)
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mydict=dict(zip(heights,names))
        l=[]
        heights.sort(reverse=True)
        for i in heights:
            l.append(mydict[i])
        return l