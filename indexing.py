
'''
Example that shows how to access a numpy ndarray using indexation and slicing
'''


import numpy as np

if __name__ == '__main__':
    # Indexing and slicing in 1D
    a = np.arange(0, 10)
    a[0] # Get a single element
    a[0:8], a[:8], a[:-1] # Get a slice of elements
    a[1:4:2], a[::2], a[1::2] # Get a slice of elements using a step value


    # Indexing and slicing in 2D
    a = np.arange(0, 25).reshape([5,5])
    a[2,2] # Get a single element
    a[:,0], a[0,:] # Fetch a row or a column
    a[:,0:3], a[0:3,:] # Fetch multiple rows or columns at one
    a[2:, 2:], a[:2, :2] # Get a submatrix

    # When only indicating less indexes than dimensions,
    # missing indices will be ":"
    a[1] # Its equivalent to a[1,:]
    assert (a[1] == a[1,:]).all()

    # Token "..." can be used when indexing. "..." is equivalent to all needed sequence of semicolons ":" to
    # complete array indexing...
    a = np.arange(0, 27).reshape([3,3,3])
    a[0,...], a[:,:,0] # is equivalent to a[0,:,:] and a[:,:,0]
    assert (a[0,...] == a[0,:,:]).all() and (a[...,0] == a[:,:,0]).all()
