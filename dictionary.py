def has_pair_with_sum(arr, target_sum):
    seen = set()
    
    for num in arr:
        if target_sum - num in seen:
            return True
        seen.add(num)
    
    return False
