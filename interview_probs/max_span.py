'''
Consider the leftmost and righmost appearances of some value in an array.
We'll say that the "span" is the number of elements between the two inclusive.
A single value has a span of 1.
Returns the largest span found in the given array.
(Efficiency is not a priority.)

max_span([1, 2, 1, 1, 3]) → 4
max_span([1, 4, 2, 1, 4, 1, 4]) → 6
max_span([1, 4, 2, 1, 4, 4, 4]) → 6
'''

def max_span(nums):
    if len(nums) == 1 or nums[0] == nums[-1]:
        return len(nums)
    num_dict = dict()
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    spans = 0
    for num in num_dict:
        if num_dict[num] > 1:
            i = nums.index(num)
            j = nums[::-1].index(num)
            j = len(nums) - j - 1
            if len(nums[i:j]) > spans:
                spans = len(nums[i:j+1])
    print(spans)


if __name__ == '__main__':
    max_span([1, 4, 2, 1, 4, 4, 4])
