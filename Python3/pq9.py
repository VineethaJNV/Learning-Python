#given a list print all elements that appear more than once in a set

def print_elements_appearing_morethan_once(nums):
    unique =set()
    duplicate = set()
    for n in nums:
        if len(unique) > 0 and n in unique:
            duplicate.add(n)
        unique.add(n)
    print(duplicate)

nums = [1, 10, 30, 23, 45, 1, 2, 2, 4,4, 4, 4, 5, 6, 10]
print_elements_appearing_morethan_once(nums)
