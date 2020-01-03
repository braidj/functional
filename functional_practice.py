import os
import sys
from functools import reduce
import operator


def add_space(func):
    print (f"\nRunning {func.__name__}")
    func()
    print('')
    return add_space

def map_example():
    # ---------------------------------------------------------------------------------------
    # Created: 20200103 by Jason Braid
    # Straight forward examples
    # Map applies a function to all the items in an input_list.
    # ---------------------------------------------------------------------------------------

    nos_list = range(1, 26)
    print(f'using numbers: {list(nos_list)}')
    product = reduce((lambda x, y: x * y), nos_list)
    print(product)
    print(list(map(lambda x: x**2, nos_list)))


def filter_example():
    # ---------------------------------------------------------------------------------------
    # Created: 20200103 by Jason Braid
    # Straight forward examples
    # filter creates a list of elements for which a function returns true
    # ---------------------------------------------------------------------------------------
    
    nos_list = range(-5, 10)
    print(f'using numbers: {list(nos_list)}')
    product = reduce((lambda x, y: x * y), nos_list)
    print(product)
    less_than_zero = list(filter(lambda x: x < 0, nos_list))
    more_than_five = list(filter(lambda x: x > 5, nos_list))

    print(less_than_zero)
    print(more_than_five)

def reduce_example():
    # ---------------------------------------------------------------------------------------
    # Created: 20200103 by Jason Braid
    # Straight forward examples
    # Reduce is a really useful function for performing some computation on a list and 
    # returning the result. It applies a rolling computation to sequential pairs of values in
    #  a list.
    # ---------------------------------------------------------------------------------------   
    nos_list = range(1,5)
    print(f'using numbers: {list(nos_list)}')
    product = reduce((lambda x, y: x * y), nos_list)
    print(product)

    print (reduce(operator.mul,nos_list))
    print (reduce(operator.add,nos_list))

if __name__ == "__main__":

    add_space(filter_example)
    add_space(map_example)
    add_space(reduce_example)
