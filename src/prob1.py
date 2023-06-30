"""
Problem 1: Multiples of 3 or 5
If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$.
The sum of these multiples is $23$.</p>
Find the sum of all the multiples of $3$ or $5$ below $1000$.
"""

nums = []
nums_ = []
test_bound = 10
problem_bound = 1000


# Logic: use modulo of 3 and 5 == 0 to determine if a number is a multiple, add to list then sum
def compute_list_nums(bound, numbers):
    for i in range(bound):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)

    return sum(numbers)


print('Natural numbers below', test_bound, ':', nums, 'sum = ', compute_list_nums(test_bound, nums))
print('Natural numbers below', problem_bound, ':', nums_, 'sum = ', compute_list_nums(problem_bound, nums_))
