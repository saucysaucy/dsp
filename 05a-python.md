# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are objects separated by a variable and indexed by position. Lists are containers that can altered, but tuples are immutable thus cannot changed change. Keys in dictionaries can be any object, but each key must be unique. Since two or more lists can hold the same information though look unique, they contain the same hash value and the computer interprets them as the same. So, lists will always produce an error if they are used as keys.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both are object containers that can be iterated/altered, but lists are indexed, ordered, and can contain unique values, while sets can only contain unique, unordered values. Elements in sets are stored by their hash values and when searching for an item in a set, it looks directly for its hash value. In lists, searching is done by comparing every element with the value that is being searched. This makes sets much faster at finding values.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a tool to create one time use functions that aren't stored and that work in line with your code without a return command.It is a great tool in list comprehensions. To find the square of each element in 2 lists and add the 2 lists, we could write :
a = [1,2,3,4,5]
b = [6,7,8,9,10]
map(lambda x,y: x**2 + y**2, a,b)
------------------------------

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used to take a nested for statements into one flat statement. It is really useful to quickly assign a new variables and also to reduce lists of lists. Map and filter statements can do simliar tasks, but are better for utilizing more complex functions and be inplace or setting to a new function.

Map vs list comprehension:
```
alist = [1,2,3,4,5]
LC_list = [i**2 for i in alist]
mapped_list = map(lambda x : x**2, alist)
```
Filter vs list comprehension:
```
alist = [1,2,3,4,5]
LC_list = [i for i in alist if i > 2]
filter_list = list(filter(lambda x : x > 2, alist))
```

Dictionaries and sets: 
```
alist = [('a', 1),('b', 2),('c', 3)]
adict = {k:v for k,v in alist}

alist = [[1,1,1,1,1,2],[2,2,2,2,3,4,3,2,3,2],[6,5,4,5,6,5,4,5,6,4,3,2]]
aset = [set(i) for i in alist]    # returns a list of a set
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days



b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)