### 1) Python Code
```
def rle_encode(s: str) -> str:
    """Run-length encode without extra modules."""
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += (str(count) if count > 1 else "") + s[i - 1]
            count = 1
    result += (str(count) if count > 1 else "") + s[-1]
    return result

def rle_decode(encoded: str) -> str:
    """Decode run-length encoded string without extra modules."""
    result = ""
    count = ""
    for ch in encoded:
        if ch.isdigit():
            count += ch
        else:
            num = int(count) if count else 1
            result += ch * num
            count = ""
    return result

// Test
original = "AAAAYYPAAA"
encoded = rle_encode(original)
decoded = rle_decode(encoded)

print("Original:", original)
print("Encoded :", encoded)
print("Decoded :", decoded)
```

### 2) Decorators in python 
```
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # run the original function
        except Exception as e:
            print(f"Error in function '{func.__name__}': {e}")
            return None   # return safe value instead of crashing
    return wrapper


@error_handler
def divide(a, b):
    return a / b


print(divide(10, 2))  # ✅ 5.0
print(divide(10, 0))  # ❌ handled by decorator → prints error
```

### 3) List vs Array

	In Python, a list is a built-in data structure that can hold elements of different data types, like integers, strings, or even other lists. It’s very flexible but not memory-efficient when handling large amounts of numeric data.

    An array, on the other hand, comes from the array module. It’s more restricted because it can only hold elements of the same type, but it’s more memory-efficient for large numerical data.

```
  // Python list can hold mixed types
	my_list = [1, "hello", 3.14]
	print(my_list)  # [1, 'hello', 3.14]
	
	//Array requires same type
	import array
	my_array = array.array('i', [1, 2, 3, 4])
	print(my_array)  # array('i', [1, 2, 3, 4])
```
### 4) Class and object:**
```
	class Dog:
	    // Class variable to count the number of dogs
	    number_of_dogs = 0
	    
	    def __init__(self, name, age):
	        self.name = name
	        self.age = age
	        Dog.number_of_dogs += 1
	
	    def description(self):
	        return f"{self.name} is {self.age} years old"
	    
	    // @classmethod
	    // def get_number_of_dogs(cls):
	    def get_number_of_dogs(self):
	        # return cls.number_of_dogs
	        return self.number_of_dogs

	// Create instances
	dog1 = Dog("Buddy", 3)
	dog2 = Dog("Bella", 5)
	
	dog2 = Dog("Bella", 5)
	
	data = dog2
	
	// Access class variable
	print(data.get_number_of_dogs())  # Output: 2
```


### 5) Fibonic**
```
	k=4
	end =7

	second_final=[]
	
	index = 0
	for i in range(end):
	    if i > k-1:
	        sum= 0
	
	        for t in second_final[index : len(second_final)]:
	            print("fatat : ",index)
	            sum+=t
	        index+=1
	
	        second_final.append(sum)
	
	    else:
	        second_final.append(1)
```



 ### 6) Booble sort
```
	data =[33,2,33,1,2,45,2,4,-1,4,23]

	data =[1,2,3,4,4]
	
	for i in range(len(data)-1):
	    tr_fal = False
	    
	    for j in range(len(data)-1-i):
	        
	        if data[j]>data[j+1]:
	            tr_fal = True
	            
	            data[j],data[j+1] = data[j+1],data[j]
	    
	    if tr_fal == False:
	        print(tr_fal)
	        break
	    
	    
	print(data)
```

### 7) Selection sort
```
	for i in range(len(data)-1):
    
	    tr_fal = False
	    for j in range(i+1,len(data)):
	        
	        if data[i]>data[j]:
	            tr_fal = True
	            
	            data[i],data[j] = data[j],data[i]
	        
	    
	    if tr_fal == False:
	        print(tr_fal)
	        break
	
	print(data)
```
### 8)  insertion sort
```
	data =[10,15,9,-1,0]
	for i in range(1,len(data)):
	    
	    j = i-1
	    mid = data[i]
	    
	    while j>=0 and  data[j]  > mid:
	        
	        data[j+1] = data[j]
	        j-=1
	    
	    data[j+1] = mid
	    
	
	print(data)
```

### 9) Anagrom:
```
	def anagrom(first,second):
	    true_or_false = True
	    if first!=second:
	        true_or_false= False
	    return true_or_false
	        
	print(anagrom(["a",2,"df"],["a",2,"df"]))
```

### 10) Substring present:
```
    	def how_may_substrings(main,sub):
	    number =0 
	    if len(main) > len(sub):
	        main,sub=main,sub
	    else:
	        main,sub = sub,main
	    main_len =len(main)
	    sub_len = len(sub)
	    print(main_len,sub_len)
	    for i in range(0,main_len-sub_len+1):
	        print(main[i:i+sub_len])
	        if (main[i:i+sub_len]==sub):
	            number+=1
	    return number
	
	print(how_may_substrings("abababa","aaaba"))
```

### 11)  interview questions 
```
	 class Amar:
	    amar ="amar"
	    
	    def __init__(self,a,b):
	        self.a = a
	        self.b = b
	    
	    @staticmethod
	    def Amar_call():
	        return amar
	    
	    @classmethod
	    def Amar_call1(cls):
	        return cls.amar
	
	
	amar = Amar(1,2)
	print(amar.amar)
	print(amar.a)
	
	# classs level
	print(amar.Amar_call1())
	print(Amar.Amar_call1())
	
	# Static level
	print(amar.Amar_call().amar) # it's returning Amar_class as a object
	print(Amar.Amar_call().amar) # it's returning Amar_class as a object
```

### 12) Python List Functions & Methods

🔹 List Methods

| Method | Description | Example | Output |
|--------|-------------|---------|--------|
| `append(x)` | Adds an element at the end | `lst = [1,2]; lst.append(3)` | `[1, 2, 3]` |
| `extend(iterable)` | Adds all elements from another iterable | `lst = [1]; lst.extend([2,3])` | `[1, 2, 3]` |
| `insert(i, x)` | Inserts element at given index | `lst = [1,3]; lst.insert(1,2)` | `[1, 2, 3]` |
| `remove(x)` | Removes first occurrence of element | `lst = [1,2,2]; lst.remove(2)` | `[1, 2]` |
| `pop([i])` | Removes and returns element at index (default last) | `lst = [1,2,3]; lst.pop()` | `[1, 2]` |
| `clear()` | Removes all elements | `lst = [1,2]; lst.clear()` | `[]` |
| `index(x)` | Returns index of first occurrence | `lst = [10,20,30]; lst.index(20)` | `1` |
| `count(x)` | Returns number of times element appears | `lst = [1,1,2]; lst.count(1)` | `2` |
| `sort()` | Sorts the list (in place) | `lst = [3,1,2]; lst.sort()` | `[1, 2, 3]` |
| `reverse()` | Reverses the list (in place) | `lst = [1,2,3]; lst.reverse()` | `[3, 2, 1]` |
| `copy()` | Returns a shallow copy | `lst = [1,2]; new = lst.copy()` | `[1, 2]` |

---

🔹 Built-in Functions for Lists

| Function | Description | Example | Output |
|----------|-------------|---------|--------|
| `len(lst)` | Returns number of elements | `len([1,2,3])` | `3` |
| `max(lst)` | Largest element | `max([1,5,3])` | `5` |
| `min(lst)` | Smallest element | `min([1,5,3])` | `1` |
| `sum(lst)` | Sum of elements | `sum([1,2,3])` | `6` |
| `sorted(lst)` | Returns new sorted list | `sorted([3,1,2])` | `[1, 2, 3]` |
| `any(lst)` | True if any element is truthy | `any([0, "", 5])` | `True` |
| `all(lst)` | True if all elements are truthy | `all([1,2,3])` | `True` |

### 13) Palindrom
```
data = 123432

def palindrome_data(data):    
    data_str = str(data)
    
    i = 0
    j = len(data_str) - 1   
    
    while i < j:
        if data_str[i] != data_str[j]:
            return False
        i += 1
        j -= 1
    
    return True

print(palindrome_data(data))  // False
print(palindrome_data(12321)) // True
```

### 14) Multi inheretence

```
from abc import ABC,abstractmethod
class Narayan(ABC):
    @abstractmethod
    def my_function(self):
        pass
    
class KondaReddy(Narayan):
    
    def my_function(self):
        print("My function in KondaReddy")
    
    @abstractmethod
    def my_child(self):
        pass
class AmarReddy(KondaReddy):
    def my_child(self):
        print("My child function in AmarReddy")
    def my_child1(self):
        print("My child function in AmarReddy")
        
Reddy = AmarReddy()
 
Reddy.my_function()
```

### 15) Multi inheretence
```
class Narayan(ABC):
    def init(self):
        print("Narayan constructor")
 
    @abstractmethod
    def my_function(self):
        pass
 
class KondaReddy(Narayan):
    def init(self):
        super().init()  # Call Narayan's constructor
        print("KondaReddy constructor")
 
    def my_function(self):
        print("My function in KondaReddy")
 
    @abstractmethod
    def my_child(self):
        pass
 
class AmarReddy(KondaReddy):
    def init(self):
        super().init()  # Call KondaReddy's constructor
        print("AmarReddy constructor")
 
    def my_child(self):
        print("My child function in AmarReddy")
 
Reddy = AmarReddy()
```


### 16) Second largest number.

```                                  data = [99, 4, 5, 6, 4, 33]
# data = [5, 1, 1]
final_array = []

if len(data) == 0:
    print("No data")
elif len(data) == 1:
    print("Only one element")
else:
    big = second = float('-inf')
    for d in data:
        if d > big:
            second = big
            big = d
        elif big > d > second:
            second = d

    print("Largest:", big)
    print("Second largest:", second if second != float('-inf') else "No second largest")
```

### 17) find the maximum profit you could make by buying and selling once
```
prices = [1, 25, 34, 65, 78]

min_price = prices[0]
max_profit = 0

for price in prices:
    profit = price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price)

print("Maximum Profit:", max_profit)
```

### 18) What is docker

	- Docker is an open-source platform that enables developers to build, deploy, and run applications in isolated environments called containers. It provides a standardized way to package an application and all its dependencies (libraries, system tools, code, and runtime) into a single, portable unit.

### 19) Custom train and split data set

	- case1) 
	```
	import pandas as pd
	import numpy as np
	
	df = pd.DataFrame({
	    "A": range(10),
	    "B": np.random.randn(10),
	    "label": np.arange(10)
	})
	
	test_size = 0.2
	
	# Shuffle the rows
	df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
	
	test_count = int(len(df) * test_size)
	
	test_df = df_shuffled[:test_count]
	train_df = df_shuffled[test_count:]
	
	print(len(test_df))
	X_train = train_df.drop("label", axis=1)
	y_train = train_df["label"]
	
	X_test = test_df.drop("label", axis=1)
	y_test = test_df["label"]
	
	```

	- case2)
	```
	import pandas as pd
	import numpy as np
	
	# sample DataFrame
	df = pd.DataFrame({
	    'age': [10, 20, 30, 40, 50],
	    'salary': [1000, 2000, 3000, 4000, 5000],
	    'label': [0, 1, 0, 1, 0]
	})
	
	test_ratio = 0.2
	n_rows = len(df)
	n_test = int(n_rows * test_ratio)
	
	# fix random seed for reproducibility
	np.random.seed(42)
	
	# shuffle row indices
	indices = np.arange(n_rows)
	np.random.shuffle(indices)
	
	test_idx = indices[:n_test]
	train_idx = indices[n_test:]
	
	train_df = df.iloc[train_idx]
	test_df  = df.iloc[test_idx]
	
	print("---- TRAIN ----")
	print(train_df)
	
	print("\n---- TEST ----")
	print(test_df)
	```

### 20) Sum == user input
```
data = [i for i in range(10)]
user_input = 5
seen_numbers = {} # Dictionary to store numbers we have encountered

print(f"Finding pairs in {data} that sum to {user_input}:")

for num in data:
    complement = user_input - num
    # Check if the 'complement' needed to reach the target is already in our dictionary
   
    if complement in seen_numbers:
        # If it is, we found a pair!
        print(complement, num)
    
    # Add the current number to the dictionary for future checks
    # The value stored (e.g., 'True') doesn't matter much here, just the key presence.
    seen_numbers[num] = True
```

### 21) Monkey patching in Python
```
is a technique for dynamically modifying or extending a module, class, or object at runtime without changing its original source code. This is possible due to Python's dynamic nature, where attributes and methods can be reassigned as easily as variables.

- Example: Patching a class method 

# original_module.py
class MyClass:
    def say_hello(self):
        return "Hello, Welcome to TutorialsPoint!"

# patch_script.py
from original_module import MyClass

# Define a new function with the desired behavior
def new_say_hello(self):
    return "Greetings from a patch!"

# Monkey patch MyClass with the new function
MyClass.say_hello = new_say_hello

# Test the patched method
obj = MyClass()
print(obj.say_hello())
# Output: Greetings from a patch!

-  Example: Patching a module-level function

# my_module.py
def original_function():
    return "Original behavior"

# main_script.py
import my_module

# Define a new function
def new_function():
    return "Patched behavior"

# Monkey patch the function in the module
my_module.original_function = new_function

# Test the patched function
print(my_module.original_function())
# Output: Patched behavior

```
