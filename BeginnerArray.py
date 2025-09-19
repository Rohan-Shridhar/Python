#import the numpy and give it a nickname
import numpy as np
x=200# length of separator lines I
y=50# length of separator lines II
# Check the version of numpy 
print("Numpy version Available: ",np.__version__)
#       Array Library 
print("-"*92,"Array Library","-"*92)
#    my_list=[1,2]
#   print(my_list*2) prints [1,2,1,2]
my_list=np.array([1,2])
print("My array",my_list)
print("My array doubled",my_list*2)# Array elements are doubled instead of repeating
print("-"*x)
print("-"*84,"Dimensions and Shape of Arrays","-"*85)

# Multidimensional arrays
# ndim returns an integer equal to the dimension of the array
# shape returns a tuple of depth rows and columns in the array
# 0 Dimensional
arr=np.array(1)
print("My Array: ",arr)
print("Dimension of the array: ",arr.ndim)
print("Shape of the array: ",arr.shape)
print("-"*y)
# 1 Dimensional
arr=np.array([1,2])
print("My Array: \n",arr)
print("Dimension of the array: ",arr.ndim)
print("Shape of the array: ",arr.shape)
print("-"*y)
# 2 Dimensional
arr=np.array([[1,2],[3,4]])# you cannot have arr=[[1,2],[3]]
print("My Array: \n",arr)
print("Dimension of the array: ",arr.ndim)
print("Shape of the array: ",arr.shape)
print("-"*y)
# 3 Dimensional
arr=np.array([[[1,2],[3,4]],[[1,2],[3,4]],[[1,2],[3,4]]])
print("My Array: \n",arr)
print("Dimension of the array: ",arr.ndim)
print("Shape of the array: ",arr.shape)
print("-"*x)
print("-"*84,"Indexing and Slicing of Arrays","-"*85)
#       Slicing the array
#[starting index:ending index:step]
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Print the array")
print(arr)
print("Reverse order")
print(arr[::-1])
print("Alternate rows")
print(arr[::2])
print("Alternate columns")
print(arr[:,::2])
print("Even row even column")
print(arr[:2:,1::2])
print("-"*x)
print("-"*88,"Arithematics on Arrays","-"*87)
#       Arithematics
print("-"*88,"Scalar Arithematic","-"*91)
#   Scalar arithematic
#Scalar arithmetic on a NumPy array is the element-wise operation of a 
#single number (a scalar) with every element in the array.
arr=np.array([1,2,3])
print("Original array",arr)
print(1,"Addition",arr+1)
print(2,"Subtraction",arr-2)
print(3,"Multiplication",arr*3)
print(4,"Division",arr/4)
print(5,"Exponent",arr**5)
print(6,"Modulus",arr%6)
print(7,"Add two arrays",arr+arr)
print(8,"Minus two arrays",arr-arr)
print(9,"Multiply two arrays",arr*arr)
print(10,"Divide two arrays",arr/arr)
print("-"*x)

#     Vector arithematic
#Vector arithmetic is the element-wise operation of two arrays of the same
#shape.
arr=np.array([1.5,2.7,3.3])
print("Square of each element")
print(np.sqrt(arr)) #square root
print("Round")
print(np.round(arr))
print("Floor")
print(np.round(arr))
print("Ceil")
print(np.ceil(arr))
print("Sum of all elements")
print(np.sum(arr)) #sum of all elements
print("Axis attribute in sum function")
print(np.sum([[1,2,3],[4,5,6]],axis=1)) #sum of each column
print("Minimum of all elements")
print(np.min(arr)) #minimum element 
print("Index of minimum element in the array")
print(np.argmin(arr)) #index of minimum element in the array
print("Index of maximum element in the array")      
print(np.argmax(arr)) #index of maximum element in the array
print("Maximum of all elements")
print(np.max(arr)) #maximum element
print("Mean of all elements")
print(np.mean(arr)) #mean of all elements   
print("Median of all elements")
print(np.median(arr)) #median of all elements
print("Standard deviation of all elements")
print(np.std(arr)) #standard deviation of all elements
print("Variance of all elements")
print(np.var(arr)) #variance of all elements
print("pi")
print(np.pi)
print("-"*x)
# Comparision Operators
print("-"*89,"Comparision operators","-"*89)
scores=np.array([100,90,80,70,60,50])
print("Scores are ",scores)
# when comparision operators ae operated on arrays, it retruns a array of boolean values
print("Marks greater than or equal to 70 ",scores>=70)
# array[array condition] retruns the elemnts that are true in following conditions
print("Scores more than or eaqual to 70 ",scores[scores>=70])
print("Equal to",scores==100)
print("Equal to",scores[scores==100])
print("Not equal to",scores!=100)
print("Not equal to",scores[scores!=100])
print("Greater than",scores>70)
print("Greater than",scores[scores>70])
print("Greater than or equal to",scores>=70)
print("Greater than or equal to",scores[scores>=70])
print("Smaller than",scores<80)
print("Smaller than",scores[scores<80])
print("Smaller than or equal to",scores<=80)
print("Smaller than or equal to",scores[scores<=80])
students=np.array([[12,50,78,45,19,34],
                   [67,89,90,56,45,78],
                   [45,23,67,89,90,100]])
Adults=np.where((students>=18) & (students<=65),students,"Need an Adult here")
print("Adults in the class\n",Adults)
print("-"*x)
#       broadcasting
print("-"*89,"Broadcasting","-"*89)
# Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
# The smaller array is "broadcast" across the larger array so that they have compatible shapes.     
arr1=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
arr2=np.array([[1,2,3,4,5,6,7,8,9,10]])  
print("Array 1\n",arr1)
print("Array 2\n",arr2)
print(arr1.shape,"\n",arr2.shape)
print("Add two arrays\n",arr1+arr2)
print("Subtract two arrays\n",arr1-arr2)    
print("Multiply two arrays\n",arr1*arr2)
print("-"*x)

#       Random Numbers
print("-"*89,"Random Numbers","-"*89)
# NumPy includes a random module that can be used to generate random numbers.
# The random module includes functions for generating random numbers,   
# creating random samples, and performing random permutations.
# Generate a random number between 0 and 1
print("Random number between 0 and 1",np.random.rand())
# Generate an array of 5 random numbers between 0 and 1
print("Array of 5 random numbers between 0 and 1",np.random.rand(5))
# Generate a 2x3 array of random numbers between 0 and 1
print("2x3 array of random numbers between 0 and 1\n",np.random.rand(2,3))
# Generate a random integer between 0 and 10
print("Random integer between 0 and 10",np.random.randint(0,10))
# Generate an array of 5 random integers between 0 and 10
print("Array of 5 random integers between 0 and 10",np.random.randint(0,10,5))
# Generate a 2x3 array of random integers between 0 and 10
print("2x3 array of random integers between 0 and 10\n",np.random.randint(0,10,(2,3)))
print("-"*x)
# Thank you

