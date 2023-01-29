# Quiz

1. Consider the following function:
   ```python
   def op(m: int, n: int) -> int:
     if n != 0:
       return m + op(m, n - 1)
     else:
       return 0
   ```
    1. What does it do?
    2. Is it tail-recursive? Why?
    3. Re-write it using a `while` loop. (If you answered "no" to the previous question, make the necessary changes to
       make it tail-recursive first.)

The following questions use the following recursive definition for a linked list:

    <linked list> = () | (<value> , <linked list>) 

That is, a linked list is either an empty tuple or an ordered pair (2-tuple) where the second component is itself a
linked list.

2. Write a function named `len` that returns the length of the given linked list:
   ```python
   def len(xs: tuple) -> int:
     # TODO: Implement this function.
     pass
   ```
    1. Using non-tail recursion.
    2. Using tail recursion (add a second parameter as appropriate).
    3. Using a `while` loop.

3. Write a function named `sum` that returns the sum of a linked list of `floats`:
   ```python
   def sum(xs: tuple) -> float:
     # TODO: Implement this function.
     pass
   ```
    1. Using non-tail recursion.
    2. Using tail recursion (add a second parameter as appropriate).
    3. Using a `while` loop.

4. Write a wrapper class named `LinkedList` that stores a linked list of values as defined above and supports iteration
   over these values using a `for` loop, list comprehension, or the built-in function `list`. Test your class using the
   following program that finds all the prime numbers smaller than 1000:
   ```python
   from LinkedList import LinkedList

   small_primes = LinkedList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
   k = 1
   for n in range(2, 1000):
       qs = [p for p in small_primes if p * p <= n]
       for q in qs:
           if n % q == 0:
               break
       else:
           print(f'[{k}] {n}')
           k += 1
   ```