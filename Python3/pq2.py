#compute average of all number in a list

def calc_avg(nums):
    sum = 0
    for n in nums:
        sum += n
    return (sum/len(nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"The average of given list of numbers is : {calc_avg(nums)}")