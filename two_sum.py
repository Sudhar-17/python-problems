def twoSum(nums, target):
    d = {}
    
    for i in range(0, len(nums)):
        value = nums[i]
        difference = target - value
        
        if value not in d:
            d[difference] = i
        else:
            current_value = i
            prev_value = d[value]
            return [current_value, prev_value]
