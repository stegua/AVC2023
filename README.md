# Python AdVent of Code - PyAVC 2023

This repository contains my solutions in Python for the puzzles of [Advent of Code 2023](https://adventofcode.com/).

Until day 19, I was on track. Then, the real family holydays started. Now, I am trying to close in missing puzzles during spare time.

Please, contact me if you have any comments or suggestions for the proposed solutions.

### Other solutions and/or programming languages

* [Dávid Németh](https://aoc.csokavar.hu/) publish nice C# solutions.
* [Daria Vasyukova](https://github.com/gereleth/aoc_python/tree/main) has pretty clean Python solutions with very beatiful animations, implemented using [PyGame](https://www.pygame.org/).
* [Pietroppeter](https://github.com/pietroppeter/adventofcode2023) is publishing solutions in [NIM](https://nim-lang.org/) and [Gleam](https://gleam.io/)
* [Hakank](http://hakank.org/advent-of-code-2023/) is publishing solutions in [Picat](http://www.picat-lang.org/) and [SWI-Prolog](https://www.swi-prolog.org/) (... old good Prolog!).
* [Peter Norvig](https://norvig.com/) has a complete collection of solutions for past editions, among other [PyTudes](https://github.com/norvig/pytudes).


### Personal commments

* **[Day 25](https://github.com/stegua/AVC2023/blob/main/python/day20/solution.py)** Still missing...
* **[Day 24](https://github.com/stegua/AVC2023/blob/main/python/day20/solution.py)** Still missing...
* **[Day 23](https://github.com/stegua/AVC2023/blob/main/python/day20/solution.py)** Still missing...
* **[Day 22](https://github.com/stegua/AVC2023/blob/main/python/day20/solution.py)** Still missing...

* **[Day 21](https://github.com/stegua/AVC2023/blob/main/python/day21/solution.py)** Part 1 is easy, while Part 2 was a real challenge. The intution of using polynomial fitting of degree 2 (a *parabola*) came straight, but filling in the details, was hard. Still, I have learned using [np.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) (for my first attempt, I made a manual *fitting* looking at my grid plots). 
    * **REMARK**: Strange enough, `wc -l input` was counting 130 rows instead of 131, and this made me crazy. Fixed after reading [this post](https://aoc.csokavar.hu/?day=21).
* **[Day 20](https://github.com/stegua/AVC2023/blob/main/python/day20/solution.py)** Still missing...
* **[Day 19.part 1](https://github.com/stegua/AVC2023/blob/main/python/day19/solution.py)** Working on solving part 2 (part 1 was easy).
* **[Day 18](https://github.com/stegua/AVC2023/blob/main/python/day18/solution.py)** Once you realize that the puzzle is about computing the area of a closed simple polygon, than you can implement the corresponding [closed formula](https://en.wikipedia.org/wiki/Polygon#Area), a particular type of [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula).
* **[Day 17](https://github.com/stegua/AVC2023/blob/main/python/day17/solution.py)** Best puzzle so far! Solved using [A* (a-star)](https://en.wikipedia.org/wiki/A*_search_algorithm) search algorithm with a [heap](https://docs.python.org/3.11/library/heapq.html#priority-queue-implementation-notes) priority queue.
* **[Day 16](https://github.com/stegua/AVC2023/blob/main/python/day16/solution.py)** Easy puzzle, but it was the occasion to play with [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple).
* **[Day 15](https://github.com/stegua/AVC2023/blob/main/python/day15/solution.py)** Finally, an easy puzzle.
* **[Day 14](https://github.com/stegua/AVC2023/blob/main/python/day14/solution.py)** This time I implemented my own **memoization** over a numpy matrix using the builtin [hash](https://docs.python.org/3/library/functions.html#hash) as suggested in a comment [here](https://stackoverflow.com/questions/16589791/most-efficient-property-to-hash-for-numpy-array).
* **[Day 13](https://github.com/stegua/AVC2023/blob/main/python/day13/solution.py)** The puzzle was hard not because of coding, but because it was hard to understand the assignment. Solved with numpy matrices, [not_equal](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html), and [zip](https://docs.python.org/3.3/library/functions.html#zip). 
* **[Day 12](https://github.com/stegua/AVC2023/blob/main/python/day12/solution.py)** This one was hard, until I realized that using tuples (read only) instead of lists (unhashable) as input arguments to function enables the decorator [@cache](https://docs.python.org/3.9/library/functools.html#functools.cache), which implements lightweight **[memoization](https://en.wikipedia.org/wiki/Memoization)**. For differences between @cache and @lru_cache, read [this post](https://stackoverflow.com/questions/70301475/difference-between-functools-cache-and-lru-cache).
* **[Day 11](https://github.com/stegua/AVC2023/blob/main/python/day11/solution.py)** Easy, with numpy [matrices](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html). Nothing to declare, but it nice to plot the galaxies with [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).
* **[Day 10](https://github.com/stegua/AVC2023/blob/main/python/day10/solution.py)** It's hard to work on Sunday, but Part 2 was completed on Monday.
    * **REMARK**: Plotting matrices with [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) helps in getting insights for [inside](https://github.com/stegua/AVC2023/blob/main/python/day10/dump1.png) and [outside](https://github.com/stegua/AVC2023/blob/main/python/day10/dump3.png) galaxies.
* **[Day 9](https://github.com/stegua/AVC2023/blob/main/python/day09/solution.py)** Nothing to declare. That's fine, since it is Saturday after all! 
* **[Day 8](https://github.com/stegua/AVC2023/blob/main/python/day08/solution.py)** Almost as hard as Day 5, but this time brute force didn't work at all. I need to draw a directed graph, detect cycles, and then to reason in term of period and *least commom multiple*.
    * **REMARK**: From Python 3.9+, there exists the builtin [lcm](https://docs.python.org/3/library/math.html#math.lcm), for computing [least common multiple](https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple).
* **[Day 7](https://github.com/stegua/AVC2023/blob/main/python/day07/solution.py)** A classic puzzle! A poker-like card game, with a custom order for handling jokers. Easy, no remarks.
* **[Day 5 BIS](https://github.com/stegua/AVC2023/blob/main/python/day05/fertilizer_v2.py)**: This time I used a disciplined approach: first, draw on a blackboard; second, code with intervals and recursioins. Going down from an hour of runtime to 0.001 seconds is quite rewarding. And I didn't need numpy at all. Here the second solution: [fertilizer_v2.py](https://github.com/stegua/AVC2023/tree/main/python/day05)
* **[Day 6](https://github.com/stegua/AVC2023/blob/main/python/day06/wait_for_it.py)** Nice application of [quadratic equations](https://en.wikipedia.org/wiki/Quadratic_equation). This time, speding some minutes with paper and pecil before coding was very productive... and I got the best rank of these first 6 days.
* **[Day 5](https://github.com/stegua/AVC2023/blob/main/python/day05/fertilizer.py)** Hard job this time. The puzzle logic was easy, but to find an efficient solution was the real challenge. Using numpy array with [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html) test, I was able to solve the puzzle in less than an hour, but it is defintely too long.
    * **Remark**: next time, think more befor coding. I should revisit this puzzle!
* **[Day 4](https://github.com/stegua/AVC2023/blob/main/python/day04/scratchcards.py)** Today, for parsing cards, I use [set](https://docs.python.org/3.11/library/stdtypes.html?highlight=set#set) which checks membership in O(1) average case. Second part was cute, but not very hard. 
    * **Remark**: for a review of the time complexity of Python builtin, see [wiki.python](https://wiki.python.org/moin/TimeComplexity).
* **[Day 3](https://github.com/stegua/AVC2023/blob/main/python/day03/gear_ratio.py)** I have admit that with a family is harder to work on AoC puzzles on Sunday. This is an ugly (unelegant) solution, but still, it works. Python dictionaries are always there the simplify the second part of the puzzle. **Remark**: 
    * **Remark**: Today, I learned about [numpy.char.array](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array), which are better than [numpy.matrix](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html) of [string](https://docs.python.org/3/library/string.html#module-string).
* **[Day 2](https://github.com/stegua/AVC2023/blob/main/python/day02/bag_of_cubes.py)** Easy with dictionaries, both first and second part. Implemented in functional syle (with `map`, `reduce`, and `sum`).
* **[Day 1](https://github.com/stegua/AVC2023/blob/main/python/day01/trebouchet.py)** The first part was easy, the second harder (I failed twice). It was unclear whether the string `'eightwo'` should be converted into 88 or 82 (and it was the second). 
    * **Remark**: I learned how to reverse a string with [slicing](https://www.digitalocean.com/community/tutorials/python-reverse-string).

