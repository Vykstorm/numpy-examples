
'''
Example that shows how to create a structured numpy ndarray
To know more about structure arrays check the official docs:
https://docs.scipy.org/doc/numpy-1.15.1/user/basics.rec.html#structured-arrays
'''


import numpy as np


if __name__ == '__main__':
    '''
    You can define a strctured array with the regular method array(). A structured array can have entries where each of
    them could have the next values: name, age, gender
    '''
    data = np.array([
        ('victor', 'male', 24),
        ('isabel', 'female',30),
        ('javier', 'male', 22),
        ('lucas', 'male', 20),
        ('penny', 'female', 30)],
        dtype=[('name', 'U10'), ('gender', 'U10'), ('age', 'i4')])
    '''
    Fields of the structured array are defined using the dtype parameter.
    It can be specified as a list of tuple items, one per each attribute of the structure.
    On each tuple, the name and data type of the attribute is specified.
    This is not the only structured array format specification avaliable, check the docs to see more ways to define
    a structured array: https://docs.scipy.org/doc/numpy-1.15.1/user/basics.rec.html#structured-arrays
    '''

    # Once we defined our structured array, we can access its entries as normally.
    data[:2], data[0:4:2], data[0]

    # Also its possible to access the entry attributes via indexation
    a = data[0]
    a['name'], a['gender'], a['age']

    a = data[0:3]
    a['name'], a['gender'], a['age']

    # The next statement returns the names of people with more than 25 years.
    data['name'][data['age'] >= 25]

    # And this returns the mean of age of man
    data[data['gender'] == 'male']['age'].mean()