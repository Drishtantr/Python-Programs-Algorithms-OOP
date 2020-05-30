
def selection_sort(nums):
    
	for i in range(len(nums)-1):
		
		index = i
		
		for j in range(i+1,len(nums),1):
			if nums[j] < nums[index]:
				index = j
			
		if index != i:
			swap(nums,index,i)
			
	
	return nums
	
def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
 
if __name__ == "__main__":
   
   nums = [8,2,5,9,6,3,4,7,1]
   print(selection_sort(nums))
  