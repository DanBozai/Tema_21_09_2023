### Homework

1) For a given list get:
   * the maximum
   * minimum
   * average
2) Get the sum of all odd numbers of the previously generated list (ex of odd numbers 1,3,5,9) 
3) Get the sum of all even numbers of the previously generated list (ex of even numbers 2,4,6)
4) Get the factorial for l=[1,2,3,4,5] factorial = 1 * 2 * 3 * 4 * 5.

There is a skeleton script shared within this homeworks. Provide the answer in each function.  
Share the answer on each individual Github account.  

### Additional Explanation

Python random.randint generates a random number.  
For the example below it generates a random number between 1, 100.  

```
import random
print(random.randint(1, 100))
75
```

List Comprehension.  
List comprehension is an elegant way to define and create lists.  
It's a shortened version.  

```
l = [ random.randint(1, 100)for i in range(20)]
l
Out[5]: [18, 22, 73, 50, 2, 69, 52, 44, 83, 64, 19, 49, 46, 15, 52, 96, 59, 87, 57, 22]
```

The above list comprehension is equal to this block of code:

```
l = []
for i in range(20):
    l.append(random.randint(1, 100))
```
