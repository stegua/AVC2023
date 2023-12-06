# Python AdVent of Code - PyAVC 2023

This repository contains my solutions in Python for the puzzles of [Advent of Code 2023](https://adventofcode.com/).

Please, contact me if you have any comments or suggestions for the proposed solutions.

### Personal commments

* **Day 6**: Nice application of [quadratic equations](https://en.wikipedia.org/wiki/Quadratic_equation). This time, speding some minutes with paper and pecil before coding was very productive... and I got the best rank of these first 6 days.
* **Day 5**: Hard job this time. The puzzle logic was easy, but to find an efficient solution was the real challenge. Using numpy array with [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html) test, I was able to solve the puzzle in less than an hour, but it is defintely too long.
    * **Remark**: next time, think more befor coding. I should revisit this puzzle!
* **Day 4**: Today, for parsing cards, I use [set](https://docs.python.org/3.11/library/stdtypes.html?highlight=set#set) which checks membership in O(1) average case. Second part was cute, but not very hard. 
    * **Remark**: for a review of the time complexity of Python builtin, see [wiki.python](https://wiki.python.org/moin/TimeComplexity).
* **Day 3**: I have admit that with a family is harder to work on AoC puzzles on Sunday. This is an ugly (unelegant) solution, but still, it works. Python dictionaries are always there the simplify the second part of the puzzle. **Remark**: 
    * **Remark**: Today, I learned about [numpy.char.array](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array), which are better than [numpy.matrix](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html) of [string](https://docs.python.org/3/library/string.html#module-string).
* **Day 2**: Easy with dictionaries, both first and second part. Implemented in functional syle (with `map`, `reduce`, and `sum`).
* **Day 1**: The first part was easy, the second harder (I failed twice). It was unclear whether the string `'eightwo'` should be converted into 88 or 82 (and it was the second). 
    * **Remark**: I learned how to reverse a string with [slicing](https://www.digitalocean.com/community/tutorials/python-reverse-string).

### Other languages

* [Pietroppeter](https://github.com/pietroppeter/adventofcode2023) is publishing solutions in [NIM](https://nim-lang.org/) and [Gleam](https://gleam.io/)
