{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This material is inspired from different source:\n",
    "\n",
    "* https://github.com/SciTools/courses\n",
    "* https://github.com/paris-saclay-cds/python-workshop/blob/master/Day_1_Scientific_Python/01-numpy-introduction.ipynb"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Difference between python list and numpy array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python offers some data containers to store data. Lists are generally used since they allow for flexibility."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = [i for i in range(10)]\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "At a first glance, numpy array seems to offer the same capabilities."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.arange(10)\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To find the difference, we need to focus on the low-level implementation of these two containers.\n",
    "\n",
    "A python list is a contiguous array in memory containing the references to the stored object. It allows for instance to store different data type object within the same list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2.0, 'three']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = [1, 2.0, 'three']\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The type of x is: [1, 2.0, 'three']\n",
      "The type of the 0-ith element is\" <class 'int'>\n",
      "The type of the 1-ith element is\" <class 'float'>\n",
      "The type of the 2-ith element is\" <class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print('The type of x is: {}'.format(x))\n",
    "for idx, elt in enumerate(x):\n",
    "    print('The type of the {}-ith element is\" {}'.format(idx, type(elt)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy arrays, however, are directly storing the typed-data. Therefore, they are not meant to be used with mix type."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The type of x is: <class 'numpy.ndarray'>\n",
      "The data type of x is: int64\n"
     ]
    }
   ],
   "source": [
    "x = np.arange(3)\n",
    "print('The type of x is: {}'.format(type(x)))\n",
    "print('The data type of x is: {}'.format(x.dtype))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create numpy array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Try out some of these ways of creating NumPy arrays. See if you can produce:\n",
    "\n",
    "* a NumPy array from a list of numbers,\n",
    "* a 3-dimensional NumPy array filled with a constant value -- either 0 or 1,\n",
    "* a NumPy array filled with a constant value -- not 0 or 1. (Hint: this can be achieved using the last array you created, or you could use np.empty and find a way of filling the array with a constant value),\n",
    "* a NumPy array of 8 elements with a range of values starting from 0 and a spacing of 3 between each element, and\n",
    "* a NumPy array of 10 elements that are logarithmically spaced.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.array([1, 2, 3])\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1., 1.],\n",
       "        [1., 1.]],\n",
       "\n",
       "       [[1., 1.],\n",
       "        [1., 1.]]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.ones((2, 2, 2))\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[5., 5.],\n",
       "        [5., 5.]],\n",
       "\n",
       "       [[5., 5.],\n",
       "        [5., 5.]]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x *= 5\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[5., 5.],\n",
       "        [5., 5.]],\n",
       "\n",
       "       [[5., 5.],\n",
       "        [5., 5.]]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.ones((2, 2, 2)) * 5\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[5. 5.]\n",
      "  [5. 5.]]\n",
      "\n",
      " [[5. 5.]\n",
      "  [5. 5.]]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[[9., 9.],\n",
       "        [9., 9.]],\n",
       "\n",
       "       [[9., 9.],\n",
       "        [9., 9.]]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.empty((2, 2, 2))\n",
    "print(x)\n",
    "x[...] = 9\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[10., 10.],\n",
       "        [10., 10.]],\n",
       "\n",
       "       [[10., 10.],\n",
       "        [10., 10.]]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[:, :, :] = 10\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  3,  6,  9, 12, 15, 18, 21])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.arange(0, 3 * 8, 3)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1.        ,  1.29154967,  1.66810054,  2.15443469,  2.7825594 ,\n",
       "        3.59381366,  4.64158883,  5.9948425 ,  7.74263683, 10.        ])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.logspace(0, 1, num=10)\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How could you change the shape of the 8-element array you created previously to have shape (2, 2, 2)? Hint: this can be done without creating a new array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.arange(8)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0, 1],\n",
       "        [2, 3]],\n",
       "\n",
       "       [[4, 5],\n",
       "        [6, 7]]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.reshape((2, 2, 2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Indexing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that the NumPy arrays are zero-indexed:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = np.random.randn(10000, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.08132702268232626"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It means that that the third element in the first row has an index of [0, 2]:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.2724298595412566"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, 2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also assign the element with a new value:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100.0\n"
     ]
    }
   ],
   "source": [
    "data[0, 2] = 100.\n",
    "print(data[0, 2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NumPy (and Python in general) checks the bounds of the array:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10000, 5)\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "index 10 is out of bounds for axis 1 with size 5",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-21-32129d83259c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m60\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m10\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m: index 10 is out of bounds for axis 1 with size 5"
     ]
    }
   ],
   "source": [
    "print(data.shape)\n",
    "data[60, 10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, we can ask for several elements at once:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.08132702, -1.09055622])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, [0, 3]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can even pass a negative index. It will go from the end of the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.454906523922135"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[-1, -1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.454906523922135"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.shape[0] - 1, data.shape[1] - 1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Slices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can select ranges of elements using slices. To select first two columns from the first row, you can use:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.08132702, -1.98069255])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, 0:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that the returned array does not include third column (with index 2).\n",
    "\n",
    "You can skip the first or last index (which means, take the values from the beginning or to the end):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.08132702, -1.98069255])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, :2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you omit both indices in the slice leaving out only the colon (:), you will get all columns of this row:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-8.13270227e-02, -1.98069255e+00,  1.00000000e+02, -1.09055622e+00,\n",
       "        1.93917583e+00])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, :]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Filtering data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-8.13270227e-02, -1.98069255e+00,  1.00000000e+02,\n",
       "        -1.09055622e+00,  1.93917583e+00],\n",
       "       [ 2.83983502e-01, -5.88899180e-01, -1.08568283e+00,\n",
       "         9.84910443e-01, -1.01478765e-01],\n",
       "       [ 6.56546514e-02,  1.92029377e-01, -5.66876543e-01,\n",
       "         7.17270032e-01, -1.57349865e+00],\n",
       "       ...,\n",
       "       [-1.48875317e+00,  1.36000612e+00, -5.24095340e-02,\n",
       "        -2.01434344e-01, -7.79935175e-02],\n",
       "       [ 9.84720335e-01, -1.32389381e+00, -5.70135316e-01,\n",
       "         1.99504546e-01, -6.89925502e-01],\n",
       "       [-7.62318898e-02,  1.60750123e+00,  3.27054878e-01,\n",
       "         4.51632811e-01, -4.54906524e-01]])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can produce a boolean array when using comparison operators."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[False, False,  True, False,  True],\n",
       "       [ True, False, False,  True, False],\n",
       "       [ True,  True, False,  True, False],\n",
       "       ...,\n",
       "       [False,  True, False, False, False],\n",
       "       [ True, False, False,  True, False],\n",
       "       [False,  True,  True,  True, False]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data > 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This mask can be used to select some specific data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([100.        ,   1.93917583,   0.2839835 , ...,   1.60750123,\n",
       "         0.32705488,   0.45163281])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data > 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It can also be used to affect some new values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.08132702, -1.98069255,         inf, -1.09055622,         inf],\n",
       "       [        inf, -0.58889918, -1.08568283,         inf, -0.10147876],\n",
       "       [        inf,         inf, -0.56687654,         inf, -1.57349865],\n",
       "       ...,\n",
       "       [-1.48875317,         inf, -0.05240953, -0.20143434, -0.07799352],\n",
       "       [        inf, -1.32389381, -0.57013532,         inf, -0.6899255 ],\n",
       "       [-0.07623189,         inf,         inf,         inf, -0.45490652]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data > 0] = np.inf\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Answer the following quizz:\n",
    "\n",
    "* Print the element in the $1^{st}$ row and $10^{th}$ cloumn of the data.\n",
    "* Print the elements in the $3^{rd}$ row and columns of $3^{rd}$ and $15^{th}$.\n",
    "* Print the elements in the $4^{th}$ row and columns from $3^{rd}$ t0 $15^{th}$.\n",
    "* Print all the elements in column $15$ which their value is above 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = np.random.randn(20, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6529138803447789"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[0, 9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.66515239, 0.14031021])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[2, [2, 14]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-2.11294964, -0.57307469,  0.46439587, -0.26358502,  0.84391946,\n",
       "       -1.98356733, -3.08046592,  1.13553818, -1.23978368, -1.49197707,\n",
       "       -2.12300313,  1.43175373, -0.91972511])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[3, 2:15]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.41960809, 1.27840098, 0.36925738, 0.095759  , 0.87680405,\n",
       "       0.40121943, 0.11250155, 0.70322598, 0.50978188, 0.62297046,\n",
       "       1.37656749])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[:, 15] > 0, 15]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Broadcasting"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Broadcasting applies these three rules:\n",
    "\n",
    "* If the two arrays differ in their number of dimensions, the shape of the array with fewer dimensions is padded with ones on its leading (left) side.\n",
    "\n",
    "* If the shape of the two arrays does not match in any dimension, either array with shape equal to 1 in a given dimension is stretched to match the other shape.\n",
    "\n",
    "* If in any dimension the sizes disagree and neither has shape equal to 1, an error is raised.\n",
    "\n",
    "Note that all of this happens without ever actually creating the expanded arrays in memory! This broadcasting behavior is in practice enormously powerful, especially given that when NumPy broadcasts to create new dimensions or to 'stretch' existing ones, it doesn't actually duplicate the data. In the example above the operation is carried out as if the scalar 1.5 was a 1D array with 1.5 in all of its entries, but no actual array is ever created. This can save lots of memory in cases when the arrays in question are large. As such this can have significant performance implications."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"broadcasting.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Replicate the above exercises. In addition, how would you make the matrix multiplication between 2 matrices."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = np.random.random((1, 3))\n",
    "Y = np.random.random((3, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "operands could not be broadcast together with shapes (1,3) (3,5) ",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-38-c6c375f45737>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mX\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0mY\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m: operands could not be broadcast together with shapes (1,3) (3,5) "
     ]
    }
   ],
   "source": [
    "X * Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.61185004, 0.41006318, 0.53700563, 0.48526757, 0.58896413]])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xx = np.dot(X, Y)\n",
    "xx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xx.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.61185004, 0.41006318, 0.53700563, 0.48526757, 0.58896413]])"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xx = X @ Y\n",
    "xx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xx.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Views on Arrays\n",
    "\n",
    "NumPy attempts to not make copies of arrays. Many NumPy operations will produce a reference to an existing array, known as a \"view\", instead of making a whole new array. For example, indexing and reshaping provide a view of the same memory wherever possible.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before\n",
      " [[0 1 2 3]\n",
      " [4 5 6 7]]\n",
      "After\n",
      " [[1000    1    2    3]\n",
      " [   4    5    6    7]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(8)\n",
    "arr_view = arr.reshape(2, 4)\n",
    "\n",
    "# Print the \"view\" array from reshape.\n",
    "print('Before\\n', arr_view)\n",
    "\n",
    "# Update the first element of the original array.\n",
    "arr[0] = 1000\n",
    "\n",
    "# Print the \"view\" array from reshape again,\n",
    "# noticing the first value has changed.\n",
    "print('After\\n', arr_view)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What this means is that if one array (`arr`) is modified, the other (`arr_view`) will also be updated : the same memory is being shared. This is a valuable tool which enables the system memory overhead to be managed, which is particularly useful when handling lots of large arrays. The lack of copying allows for very efficient vectorized operations.\n",
    "\n",
    "Remember, this behaviour is automatic in most of NumPy, so it requires some consideration in your code, it can lead to some bugs that are hard to track down. For example, if you are changing some elements of an array that you are using elsewhere, you may want to explicitly copy that array before making changes. If in doubt, you can always copy the data to a different block of memory with the copy() method.\n",
    "\n",
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before\n",
      " [[0 1 2 3]\n",
      " [4 5 6 7]]\n",
      "After\n",
      " [[0 1 2 3]\n",
      " [4 5 6 7]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(8)\n",
    "arr_view = arr.reshape(2, 4).copy()\n",
    "\n",
    "# Print the \"view\" array from reshape.\n",
    "print('Before\\n', arr_view)\n",
    "\n",
    "# Update the first element of the original array.\n",
    "arr[0] = 1000\n",
    "\n",
    "# Print the \"view\" array from reshape again,\n",
    "# noticing the first value has changed.\n",
    "print('After\\n', arr_view)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Final exercise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "def trapz_slow(x, y):\n",
    "    area = 0.\n",
    "    for i in range(1, len(x)):\n",
    "        area += (x[i] - x[i-1]) * (y[i] + y[i-1])\n",
    "    return area / 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Part 1\n",
    "\n",
    "Create two arrays $x$\n",
    "and $y$, where $x$ is a linearly spaced array in the interval $[0,3]$ of length 3000, and y represents the function $f(x)=x^2$ sampled at $x$\n",
    "\n",
    "#### Part 2\n",
    "\n",
    "Use indexing (not a for loop) to find the 10 values representing $y_i+y_{i−1}$\n",
    "for i between 1 and 11.\n",
    "\n",
    "Hint: What indexing would be needed to get all but the last element of the 1d array `y`. Similarly what indexing would be needed to get all but the first element of a 1d array.\n",
    "\n",
    "#### Part 3\n",
    "\n",
    "Write a function `trapz(x, y)`, that applies the trapezoid formula to pre-computed values, where x and y are 1-d arrays. The function should not use a for loop.\n",
    "\n",
    "#### Part 4\n",
    "\n",
    "Verify that your function is correct by using the arrays created in #1 as input to trapz. Your answer should be a close approximation of $\\sum 30 x^2$ which is 9\n",
    "\n",
    "#### Part 5 (extension)\n",
    "\n",
    "`numpy` and `scipy.integrate` provide many common integration schemes. Find the documentation for NumPy's own version of the trapezoidal integration scheme and check its result with your own."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.00000000e+00, 1.00033344e-03, 2.00066689e-03, ...,\n",
       "       2.99799933e+00, 2.99899967e+00, 3.00000000e+00])"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.linspace(0, 3, 3000)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.000000e+00, 1.000667e-06, 4.002668e-06, ..., 8.988000e+00,\n",
       "       8.993999e+00, 9.000000e+00])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = x ** 2\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f0e241f1fd0>]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAW4AAAD8CAYAAABXe05zAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAHoJJREFUeJzt3Xl4VOWhx/HvS1ZCIOwJJoSwI/sS2ey1ihsudUWlCiKiuGtta21tb6v1ttcuV8Vqa5FFVjekdWnVKuIjatnCvgcICQFCErLvmZn3/pFoFYEMIZMzZ/L7PE8eJ+Yk+b2c5Jcz75xzXmOtRURE3KOV0wFEROT0qLhFRFxGxS0i4jIqbhERl1Fxi4i4jIpbRMRlVNwiIi6j4hYRcRkVt4iIy4QH4ot27tzZpqSkBOJLi4iEpLS0tHxrbRd/tg1IcaekpLB+/fpAfGkRkZBkjMn0d1tNlYiIuIyKW0TEZVTcIiIuo+IWEXEZFbeIiMuouEVEXEbFLSLiMipuEZEmsDajgDmr9tMcy0GquEVEzlBuaRX3Ld3AkjVZVNR4A/79AnLlpIhIS+Hx+rh/6UZKq2pZNGM0baICX6sqbhGRM/D7D3azNqOAZ28azoCEds3yPTVVIiLSSO9vO8LsT/czdWwPrhmR2GzfV8UtItII+/PK+PEbWxjevT2/uPLsZv3eKm4RkdNUXu3hrkVpRIa34s+3jCQqPKxZv7+KW0TkNFhreWTZZvbllfH890dwVvvWzZ5BxS0ichr++ul+/rk1h59eNoDxfTo7kkHFLSLip1Xpefz+/V1cObQbd/5XL8dyqLhFRPxwsKCCB17ZSN+ubfn9pKEYYxzLouIWEWlAVa2Xuxen4fVZ/jp1FDGRzl4CowtwREROwVrLY8u3suNICXOnpZLSuY3TkXTELSJyKgv/ncnyjYf4wYX9mDAg3uk4gIpbROSk1mYU8OS7O7jo7K48MKGP03G+ouIWETmBnOIq7l2yge4dY3j6puG0auXci5HH0xy3iMhxqj1e7lmSRkWNh6V3jqFddITTkb5BxS0icpwn3tnBxqwi/nzLSPrFt3U6zrdoqkRE5GsWrc5k6Zos7v5uby4f0s3pOCek4hYRqbd6/zGeeHs7EwZ05ZFL+zsd56T8Km5jzMPGmO3GmG3GmFeMMdGBDiYi0pwOFlRwz+I0enSK4dnJwwkLohcjj9dgcRtjEoEHgVRr7WAgDJgc6GAiIs2lvNrDnQvX4/VZ5kw7J+hejDyev1Ml4UBrY0w4EAMcDlwkEZHm4/NZfvT6ZvYcLeX5m0fSMwiujGxIg8VtrT0E/BHIAo4Axdbafx2/nTFmpjFmvTFmfV5eXtMnFREJgOc+Tuf97Tk8dvnZnNevi9Nx/OLPVEkH4GqgJ3AW0MYYM+X47ay1s621qdba1C5d3DF4EWnZ3t92hGc/Sue6kYnM+E5Pp+P4zZ+pkouADGttnrW2FlgOjA9sLBGRwNp5pIQfvr6Z4d3b89trhzh6m9bT5U9xZwFjjTExpm5kFwI7AxtLRCRwCspruHPhetpGhzN76iiiI5p3zcgz5c8c9xpgGbAB2Fr/ObMDnEtEJCBqvT7uXZJGbmk1s6em0rWd+85u9uuSd2vtr4BfBTiLiEhAWWt54p3trN5fwDM3DWNY9/ZOR2oUXTkpIi3Ggi8OsHh1Fned14trRyQ5HafRVNwi0iKs3J3Lr9/dwcUD4/nJxAFOxzkjKm4RCXm7c0p5YOlGBiS049mbgvtydn+ouEUkpOWXVXP7y+uIiQxj7m2ptIly/92s3T8CEZGTqKr1MnPheo6VV/P6XePoFtfa6UhNQsUtIiHJWsujb25hQ/2CCEOT3HkGyYloqkREQtKfPt7LW5sO88il/YN2QYTGUnGLSMh5Z/Nhnv5wD9eNSOTe83s7HafJqbhFJKRszCrkx29sJrVHB/73enfdg8RfKm4RCRmHiiq5c2EaXdtF8depo4gKd9c9SPylFydFJCSUVNUy4+V1VNd6eeXOMXSKjXI6UsCouEXE9Wq9Pu5dvIG9uWW8PH00fePbOh0poFTcIuJq1lp+tnwrn+3N5w+ThvKdvp2djhRwmuMWEVd7bsVelqVl8+CFfbkhtbvTcZqFiltEXOvNtGye+WgP141M5OGL+jodp9mouEXElb7Ym8+jb25hfO9OPHXd0JA87e9kVNwi4jp7jpZy1+I0enVpw1+mjCIyvGVVWcsarYi4Xm5JFdPnr6N1RBjzp48mrnWE05Ganc4qERHXKK/2cPuCdRRW1PD6XeNIbB8ad/s7XSpuEXEFj9fH/Us3sPNIKXNuTWVwYpzTkRyjqRIRCXrWWv77re2s3J3Hk1cP5oIBXZ2O5CgVt4gEvWc/SueVtVncd0Fvbh6T7HQcx6m4RSSoLV6dyawV6dyYmsSPL+nvdJygoOIWkaD1/rYcfvnWNiYM6Mpvrw3NW7Q2hopbRILS2owCHnx1I8O6t+eFm0cSHqa6+pL+JUQk6OzOKeWOBetI6tCaudPOoXVkaN5Xu7FU3CISVA4VVTJt3lpaR4ax8PbRdGwT6XSkoKPzuEUkaBRV1DBt3lrKazy8cfc4kjrEOB0pKKm4RSQoVNZ4uf3ldWQVVLDw9tEMSGjndKSgpakSEXGcx+vjgVc2sPFgEbNuGs7YXp2cjhTUVNwi4iifz/LT5Vv5aGcuv75qEJcN6eZ0pKCn4hYRx1hr+Z9/7GRZWjY/uKgvU8elOB3JFVTcIuKY51bsZd7nGUw/N4WHLmw5K9icKRW3iDji5c8zeOajPVw/Mon/vmKgroo8DX4VtzGmvTFmmTFmlzFmpzFmXKCDiUjoWr4hm8ff2cElA+P53fVDaNVKpX06/D0dcBbwvrV2kjEmEtDJlSLSKP/ansMjy+rWinzu+yN0KXsjNFjcxph2wHnAbQDW2hqgJrCxRCQUfbEvn/tf2cjgxDhm35pKdIQuZW8Mf/7U9QLygPnGmI3GmDnGmDYBziUiIWbzwSLuXLCelE4xLJh+DrFRuv6vsfwp7nBgJPAXa+0IoBz46fEbGWNmGmPWG2PW5+XlNXFMEXGz9KOlTJu/lo6xkSyaMYb2Mbr/yJnwp7izgWxr7Zr695dRV+TfYK2dba1NtdamdunSpSkzioiLZR2rYMrcNUSEtWLxjDHEt4t2OpLrNVjc1toc4KAx5sulJy4EdgQ0lYiEhENFlXz/pdXUeHwsnjGGHp00y9oU/J1kegBYUn9GyX5geuAiiUgoOFpSxc0vraakqpZX7hxL/4S2TkcKGX4Vt7V2E5Aa4CwiEiLyy6q5+aXV5JdWs+iOMQxOjHM6UkjRy7oi0qSKKmqYMmcNh4uqWHD7aEYmd3A6UshRcYtIkympqmXq3LXszy9n/m3nMLpnR6cjhSRdsiQiTaKs2sNt89ayK6eEv04Zxbl9OjsdKWTpiFtEzlhljZcZL69jc3YxL9w8kgsGdHU6UkjTEbeInJGqWi8zF61n3YECnrlpOBMHJzgdKeTpiFtEGq3a4+XeJRtYlZ7PH28YxlXDznI6UougI24RaZRqj5d7Fm/g4125/PbaIUwaleR0pBZDxS0ip+340r55TLLTkVoUFbeInBaVtvM0xy0ifqv2eLl7URord+eptB2kI24R8UtVrUo7WOiIW0QaVFXr5Z7FdaX9v9cN4fujVdpO0hG3iJySSjv4qLhF5KRU2sFJUyUickIVNR5mLkzjs735Ku0go+IWkW8pq/Zw+/x1rM8s4I83DNPFNUFGxS0i31BcUcu0+WvZeqiYWZNH8D1dxh50VNwi8pVjZdVMnbuWvbll/OWWkVwySDeMCkYqbhEBILekilvmrCGroILZt47i/P66NWuwUnGLCIeLKrllzhqOllQxf/o5jO+tRRCCmYpbpIXLOlbBzXNWU1xRy6IZoxnVQ8uNBTsVt0gLti+vjFteWkNlrZcld45haFJ7pyOJH1TcIi3UtkPFTJu3FoBXZ47l7G7tHE4k/tKVkyIt0Or9x5g8ezXREWG8cfc4lbbL6IhbpIX5cMdR7lu6ge4dWrP4jjF0i2vtdCQ5TSpukRZk+YZsHlm2hcFntWP+9NF0bBPpdCRpBBW3SAsx77MMfv3uDsb37sTsW1OJjdKvv1tpz4mEOGstz3yUznMr0rl0UDyzJo8gOiLM6VhyBlTcIiHM57M8/s52Fv47kxtTk/jttUMID9M5CW6n4hYJUTUeH48s28xbmw4z87xe/OyyARhjnI4lTUDFLRKCSqtquWfxBj7bm89PJvbn3vP7OB1JmpCKWyTE5JZUcdv8dew+WsofJg3lhtTuTkeSJqbiFgkh+/LKmDZvLQXlNcydlqo7/IUoFbdIiEjLLGTGgnWEtzK8OnOs7jsSwlTcIiHgwx1HuX/pBrrFRbPw9jEkd4pxOpIEkN/nBRljwowxG40x7wYykIicniVrMrlr0XoGdGvHm/eMV2m3AKdzxP0QsBPQ3WhEgoC1lmc+3MNzH+9lwoCuPH/zCGIi9SS6JfDriNsYkwRcAcwJbBwR8Ue1x8uPXt/Mcx/vZfI53Zk9dZRKuwXxd08/C/wEaBvALCLih8LyGu5anMbajAJ+eHE/HpjQRxfWtDANFrcx5kog11qbZow5/xTbzQRmAiQnJzdZQBH5j4z8cm5/eR2HiiqZNXk4Vw9PdDqSOMCfqZJzgauMMQeAV4EJxpjFx29krZ1trU211qZ26dKliWOKyNqMAq798+cUV9ay9I4xKu0WrMHittb+zFqbZK1NASYDH1trpwQ8mYh85W8bs5kyZw0d20Tyt3vHk5qiBX1bMr2aIRLErLU8+1E6s1akM65XJ16cMoq4mAinY4nDTqu4rbWfAJ8EJImIfEO1x8ujy7bw902HuWFUEr+5dgiR4bolq+iIWyQo5ZZWcc/iDaRlFvLIpf259/zeOnNEvqLiFgky2w4Vc+fC9RRW1PDCzSO5Ymg3pyNJkFFxiwSRdzYf5pFlm+kYE8myu8czODHO6UgShFTcIkHA57M8/eEenl+5l9QeHXhx6ig6x0Y5HUuClIpbxGFl1R4efm0TH+44yk2p3XnymsF6EVJOScUt4qCsYxXcsXAd+/LKefx7A5k2PkUvQkqDVNwiDvliXz73LdmAz8KC6aP5Tt/OTkcSl1BxizQzay1zVmXw1Pu76Nm5DXNuTSWlcxunY4mLqLhFmlF5tYefvLmFf2w5wmWDE/jDDcOIjdKvoZwe/cSINJN9eWXcvSiNfXll/PSyAdx1Xi/NZ0ujqLhFmsEH23P40eubiQxvxaIZYzi3j+azpfFU3CIB5PVZ/u9fu/nzJ/sYmhTHX6aMIrF9a6djicupuEUCpKC8hode3ciq9Hwmn9Odx68aRHREmNOxJASouEUCYGNWIfcv3UheaTVPXTeEyaO1KpQ0HRW3SBOy1jL3swyeem8XCXHRvHH3OIZ1b+90LAkxKm6RJlJcUcuPl23mwx1HuWRgPH+YNEyLHkhAqLhFmsCmg0Xct2QDuaVV/PLKgUw/V5euS+CouEXOgLWWeZ8f4Kn3dtK1bTRv3D2e4ZoakQBTcYs0UnFFLY8s28y/dhzlorPj+eMNQ2kfE+l0LGkBVNwijZCWWcBDr24ip7iKX1xxNjO+01NTI9JsVNwip8Hj9fH8yr08tyKdxA6tef3ucYxM7uB0LGlhVNwifjpYUMHDr21ifWYh141I5ImrB9E2WmeNSPNTcYv44e3Nh/n58q1Y4NmbhnPNiESnI0kLpuIWOYWyag+/fGsbyzccYmRye2ZNHkH3jjFOx5IWTsUtchKbDhbx0KsbOVhQwYMX9uXBCX0ID9NakOI8FbfIcWq9Pv60Ip0XPtlHQrtoXrtrHOekdHQ6lshXVNwiX7M7p5Qfvr6J7YdLuG5EIr+6ahBxrfUCpAQXFbcIdffNnrNqP//3rz20jQ7nxSmjmDg4welYIiek4pYWL/NYOT9+YzPrDhRy6aB4fnPtEDrHRjkdS+SkVNzSYllrWbImi9/+cydhrQxP3ziMa0ck6gpICXoqbmmRsgsr+NnyraxKz+e/+nbm95OG0i1OS4qJO6i4pUXx+SyLVmfyu/d3YYAnrxnMlDHJOsoWV1FxS4uxL6+MR5dtYX1mId/t14XfXDuYpA66mEbcR8UtIa/W62P2p/uZtSKdmMgwzWWL66m4JaRtO1TMo29uYfvhEq4Y0o3HrxpEl7Y6Y0TcrcHiNsZ0BxYCCYAPmG2tnRXoYCJnorLGy6wV6by0aj8d20TqvGwJKf4ccXuAH1lrNxhj2gJpxpgPrbU7ApxNpFFW7DzKL9/azqGiSm5MTeLnlw/Uor0SUhosbmvtEeBI/eNSY8xOIBFQcUtQOVxUyRPvbOeD7UfpFx/L63eNY3RP3WNEQs9pzXEbY1KAEcCaQIQRaYxar4+XPz/AMx/twWctj04cwIzv9CQyXHfyk9Dkd3EbY2KBN4EfWGtLTvDxmcBMgOTk5CYLKHIqaZmF/PxvW9mVU8qFA7ry+FWDdL9sCXl+FbcxJoK60l5irV1+om2stbOB2QCpqam2yRKKnEBeaTV/+GAXr6/PpltcNH+dOopLBsbrFD9pEfw5q8QAc4Gd1tqnAx9J5ORqPD4WfHGA51akU+XxMvO8Xjx0YV/aROnMVmk5/PlpPxeYCmw1xmyq/3+PWWv/GbhYIt+2cncuT767g/155VzQvwv/feVAenWJdTqWSLPz56ySzwA9/xTHZOSX8z/v7mDFrlx6dm7DvNtSmTAg3ulYIo7R80sJWiVVtbywci/zPssgMqwVP7tsANPP1dkiIipuCTo1Hh9L12Ty3Md7KSiv4fqRSTw6sT9d20U7HU0kKKi4JWhYa3l/Ww6/e38XB45VMK5XJx67/GyGJMU5HU0kqKi4JSikZRbwm3/sZENWEX27xjLvtlQu6N9Vp/eJnICKWxyVkV/O797bxfvbc+jaNoqnrhvCpFFJhIdpHlvkZFTc4ohDRZX8aUU6b6RlExXeiocv6sed5/UkJlI/kiIN0W+JNKvc0ir+vHIfS9dkATB1bA/uvaA3XdvqhUcRf6m4pVkUltfw4qf7WPDFAWq9lhtTk7h/Ql8S22uBXpHTpeKWgCqpqmXuqgzmfpZBeY2Ha4Yn8tCFfUnp3MbpaCKupeKWgCgsr2H+5xnM/+IApVUeLhucwMMX96NffFuno4m4nopbmlRuaRVzV2WwaHUmFTVeLhucwH0X9GFwos7FFmkqKm5pEoeLKpn96X5eWZtFrdfHVcPO4t4L+ugIWyQAVNxyRvbnlfHSqv0sS8vGWrh+ZBL3nN9bc9giAaTiltNmrWV9ZiGzP93PRzuPEhHWisnnJHPXd3uR1EGrz4gEmopb/Ob1WT7YnsPsT/ez6WARHWIieGBCX24d14POsVFOxxNpMVTc0qDyag/L0rKZ89l+DhZUktIphievGcykkUm0jgxzOp5Ii6PilpPan1fGotWZLEvLprTKw6geHfj55QO5eGA8Ya108ycRp6i45Ru8PsvKXbks+PcBVqXnExFmuGxwN6aNT2FUjw5OxxMRVNxSr7C8htfWH2Tx6kyyCytJaBfNDy/ux+TR3XUfEZEgo+JuwXw+y+qMY7y27iDvbcuhxuNjbK+OPHb52Vw8MJ4I3VpVJCipuFugoyVVLEvL5rV1B8kqqKBtdDg3pXZnytge9E/QBTMiwU7F3ULUen2s3JXLa+sOsnJ3Lj4LY3t15IcX92Pi4ASiI3R2iIhbqLhDmLWWjQeL+PvGQ7y75QgF5TV0bRvF3d/tzY2p3XV1o4hLqbhD0L68Mt7aeIi3Nh8m81gFUeGtuGhgPNcOT+T8/l20LJiIy6m4Q8Shokre23qEtzcfZkt2McbA+N6duP+CPkwcnEDb6AinI4pIE1Fxu1jmsXLe25bDe9ty2HywCIBBZ7XjF1eczfeGnUV8O53GJxKKVNwusze3jPe2HuG9bTnsOFICwJDEOH4ysT+XDe5GT81bi4Q8FXeQq/H4WJtRwMe7clm5O5eM/HIARia35xdXnM2lgxLo3lF35BNpSVTcQSi3tIpPduWxYtdRPkvPp7zGS2R4K8b16sT0c1O4ZGACCXGaBhFpqVTcQaCixsPajAK+2HeMz/fms/1w3RRIQrtorh6RyIT+XRnfpxMxkdpdIqLidkSt18eW7CI+Sz/G5/vy2ZhVSK3XEhnWipE92vPIpf25oH9Xzu7WFmN0Fz4R+SYVdzMoq/awMauQdQcKScssYGNWERU1XoypOwvk9nN7cm6fzpyT0lH3txaRBqm4m5i1lqyCCjZnF5N2oIB1BwrZlVOCz0IrAwMS2jFpVBJje3ViXK9OdGgT6XRkEXEZFfcZsNZysKCSLYeK2HqomG2HitmaXUxJlQeAmMgwRiS35/4JfUnt0YERye11IYyInDEVt5+KKmrYc7SM3UdLST9ayp6jpew8UkpxZS0AEWGGAQntuHLYWQxJjGNIYhwDEtrq8nIRaXJ+FbcxZiIwCwgD5lhrnwpoKodUe7xkF1aSeayczGMVZB6rYG9uXVnnlVZ/tV1sVDh942O5fEgCQxLbMyQxjn4JsUSFa35aRAKvweI2xoQBLwAXA9nAOmPM29baHYEO15SstZRUecgpriKnpIqc4kqOFFeRU1xFVkFdSR8ursTa/3xOm8gweneN5bv9utAvPpa+8W3pH9+WbnHROttDRBzjzxH3aGCvtXY/gDHmVeBqwJHirvX6qKjxUlHjobz6P/8traqlqKKWgooaCitqKCyvoaC8lqKKGo6V15BTXEVlrfdbX69zbCTdO8YwumdHkjvGkNI5huSObejRKYZObSJV0CISdPwp7kTg4NfezwbGBCLMlX9aRUWNF6/P4vFaPD5f3WOfxeu1VHt81Hh9DX6dyLBWdGgTQYeYSDrERDKwWzsmDOhKQrtoEuKi6RYXTXy7urfIcM1Bi4i7+FPcJzrktN/ayJiZwEyA5OTkRoXp0yUWj88S3soQ1qpV3X/DTP37hsjwVsRGhhMTFU5MZBgxkWG0iQwnJiqM2KhwOsRE0rFNJDGRYTpSFpGQ5U9xZwPdv/Z+EnD4+I2stbOB2QCpqanfKnZ/PDt5RGM+TUSkRfFnnmAd0NcY09MYEwlMBt4ObCwRETmZBo+4rbUeY8z9wAfUnQ44z1q7PeDJRETkhPw6j9ta+0/gnwHOIiIiftApFSIiLqPiFhFxGRW3iIjLqLhFRFxGxS0i4jLG2kZdK3PqL2pMHpDZyE/vDOQ3YRwnhcpYQmUcoLEEo1AZB5zZWHpYa7v4s2FAivtMGGPWW2tTnc7RFEJlLKEyDtBYglGojAOabyyaKhERcRkVt4iIywRjcc92OkATCpWxhMo4QGMJRqEyDmimsQTdHLeIiJxaMB5xi4jIKThW3MaYicaY3caYvcaYn57g41HGmNfqP77GGJPS/Ckb5sc4bjPG5BljNtW/3eFEzoYYY+YZY3KNMdtO8nFjjHmufpxbjDEjmzujv/wYy/nGmOKv7ZNfNndGfxljuhtjVhpjdhpjthtjHjrBNkG/b/wchyv2izEm2hiz1hizuX4sT5xgm8D2l7W22d+ouz3sPqAXEAlsBgYet829wIv1jycDrzmRtQnGcRvwvNNZ/RjLecBIYNtJPn458B51KyKNBdY4nfkMxnI+8K7TOf0cSzdgZP3jtsCeE/yMBf2+8XMcrtgv9f/OsfWPI4A1wNjjtglofzl1xP3VAsTW2hrgywWIv+5qYEH942XAhSb41iPzZxyuYK39FCg4xSZXAwttndVAe2NMt+ZJd3r8GItrWGuPWGs31D8uBXZStw7s1wX9vvFzHK5Q/+9cVv9uRP3b8S8WBrS/nCruEy1AfPxO/Goba60HKAY6NUs6//kzDoDr65/CLjPGdD/Bx93A37G6xbj6p7rvGWMGOR3GH/VPt0dQd4T3da7aN6cYB7hkvxhjwowxm4Bc4ENr7Un3SSD6y6ni9mcBYr8WKXaYPxnfAVKstUOBj/jPX2G3ccP+8NcG6i4vHgb8Cfi7w3kaZIyJBd4EfmCtLTn+wyf4lKDcNw2MwzX7xVrrtdYOp24N3tHGmMHHbRLQfeJUcfuzAPFX2xhjwoE4gu/pb4PjsNYes9ZW17/7EjCqmbI1Nb8WjXYDa23Jl091bd3qThHGmM4OxzopY0wEdWW3xFq7/ASbuGLfNDQOt+0XAGttEfAJMPG4DwW0v5wqbn8WIH4bmFb/eBLwsa2f6Q8iDY7juLnGq6ib23Ojt4Fb689gGAsUW2uPOB2qMYwxCV/ONxpjRlP3e3DM2VQnVp9zLrDTWvv0STYL+n3jzzjcsl+MMV2MMe3rH7cGLgJ2HbdZQPvLrzUnm5o9yQLExphfA+uttW9Tt5MXGWP2UveXarITWU/Fz3E8aIy5CvBQN47bHAt8CsaYV6h7Vb+zMSYb+BV1L7pgrX2RujVHLwf2AhXAdGeSNsyPsUwC7jHGeIBKYHIQHhR86VxgKrC1fk4V4DEgGVy1b/wZh1v2SzdggTEmjLo/Lq9ba99tzv7SlZMiIi6jKydFRFxGxS0i4jIqbhERl1Fxi4i4jIpbRMRlVNwiIi6j4hYRcRkVt4iIy/w/MBzp/trYZ1IAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f0e32b22eb8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.48 ms ± 39.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%%timeit\n",
    "trapz_slow(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.000000500333512"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trapz_slow(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "def trapz(x, y):\n",
    "    return np.sum((x[1:] - x[:-1]) * (y[1:] + y[:-1])) / 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.7 µs ± 58.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%%timeit\n",
    "trapz(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.0000005003335"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trapz(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.integrate import trapz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.0000005003335"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trapz(y, x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16.8 µs ± 93 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%%timeit\n",
    "trapz(y, x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
