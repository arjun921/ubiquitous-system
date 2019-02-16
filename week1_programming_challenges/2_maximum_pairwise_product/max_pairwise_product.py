# python3


# my solution
def max_pairwise_product(num_list):
    num_list.sort()
    largest = max(num_list)

    # find_second = True
    i = 2
    sec_large = num_list[-i]
    # check if second largest number is same or not, removed based on default logic. 
    # while find_second:
    #     sec_large = num_list[-i]
    #     if largest != sec_large:
    #         find_second = False
    #     else:
    #         if len(num_list)>i:
    #             i+=1
    #         else:
    #             find_second = False
    return largest*sec_large

# solution 2
def max_pairwise_product_two(num_list):
    num_list = list(set(num_list))
    largest = max(num_list)
    num_list.remove(largest)
    if len(num_list)>0:
        second_largest = max(num_list)
        return largest*second_largest
    else:
        return largest

# default solution
def max_pairwise_product_def(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            # print("First, Second",first,second)
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product

# my solution after reference


# internet solution
def largest(numbers):
    return max(numbers)

def second_largest(numbers):
    # fails when no second largest(on purpose)
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None


if __name__ == "__main__":
    # import random

    # Stress Test
    # while True:
    #     num_list = [random.randint(1,10000) for x in range(random.randint(2,10000))]
    #     print(num_list)
    #     my_solution = max_pairwise_product(num_list)
    #     my_solution2 = max_pairwise_product_def(num_list)

    #     # # stress test
    #     if my_solution2 == my_solution:
    #         print(my_solution,my_solution2)
    #         print('OK')
    #     else:
    #         print(my_solution,my_solution2)
    #         print('FAIL')
    #         break


    # Timer
    # Results:
    # My solution took:  0:00:00.000796
    # Default solution took:  0:00:05.298903
    # num_list = [random.randint(1,10000) for x in range(random.randint(2,10000))]
    # print(num_list)
    # import datetime
    # start = datetime.datetime.now()
    # my_solution = max_pairwise_product(num_list)
    # end = datetime.datetime.now()
    # print("My solution took: ",end-start)
    # start = datetime.datetime.now()
    # their_solution = max_pairwise_product_def(num_list)
    # end = datetime.datetime.now()
    # print("Default solution took: ",end-start)
    # # # stress test
    # if their_solution == my_solution:
    #     print(my_solution,their_solution)
    #     print('OK')
    # else:
    #     print(my_solution,their_solution)
    #     print('FAIL')
        

    # Submission
    # input()
    # num_list = [int(x) for x in input().split()]
    # my_solution = max_pairwise_product(num_list)
    # print(my_solution)
    
    # #Submission 2
    # input()
    # num_list = [int(x) for x in input().split()]
    # my_solution = max_pairwise_product_two(num_list)
    # print(my_solution)

    #  Submission 3
    input()
    num_list = [int(x) for x in input().split()]
    my_solution = max_pairwise_product(num_list)
    print(my_solution)

# Good job! (Max time used: 0.20/5.00, max memory used: 28344320/536870912.)