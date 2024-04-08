class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        i=n-1
        j=0
        
        while j<m and i>-1 and arr1[i]>arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i=i-1
            j=j+1
        arr1.sort()
        arr2.sort()