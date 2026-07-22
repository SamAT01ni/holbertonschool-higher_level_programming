# Everything is Object - A quick dive into mutable and immutable objects in Python

---

## Introduction - What is an object?

Put simply, an object in Python is any piece of data that gets saved. These include strings, integers, functions and even modules.

These objects have 3 main characteristics:
. id - objects memory address
. Type - what the object represents (int, str, etc)
. Value - The data stored in the object which can be mutable or immutable

An instance is similar to an object but where an object relates to an entity in the memory, and instance the relationship between an object and its class

### Mutable and immutable

A **mutable object** is one which can be altered after creation. These include lists, dictionaries and sets. The memory address stays the same when altered and they are unhashable.

**Immutable objects** cannot be altered after they are created. They can only be changed by essentially creating a new object. These include integers, floats, strings, tuples and booleans. The memory address changes when the onject is reassigned which makes it immutable, and they can be hashed.

---

## Type and ID

To return the type of an object, you can use something like:
```python
>>> a = 8
>>> type(a)
<class 'int'>
```

and to return the memory address (id) you can do:
```python
>>> id(a)
4521921040
```

---

## Immutable objects
### Int
say we have 2 integers, a and b. Let `a = 89` and `b = 89`.

a and b both **point** to the same object. If we said `b = a` then they still point to the same object. However, if we then said `b = a + 1`, they no longer do as integers are **immutable**. The value of `b` has been altered so it no longer points to the same object.

### Str

The same will happen with strings, another immutabale object. If we say:
```python
>>> s1 = "banana"
>>> s2 = "banana"
>>> print(s2 is s1)
True
```
The 2 strings both point to the same object of `banana` to save memory. 2 strings with identical values will point to the same object.

![Image of 2 strings pointing to same object](banana.png)
