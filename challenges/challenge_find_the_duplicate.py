def find_duplicate(nums):
    unique = []
    for number in nums:
        if isinstance(number, str) or number < 0:
            return False
        if number not in unique:
            unique.append(number)
        else:
            return number
    if len(unique) == len(nums):
        return False
