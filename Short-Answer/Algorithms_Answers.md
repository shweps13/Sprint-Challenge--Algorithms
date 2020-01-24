#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) ==> we're checking a < n^3, while we're incrementing a by n^2 each time


b) O(n log n) ==> inner loop is running on less than what the outer loop is so total time will increase at a rate greater than the size of n


c) O(n) ==> it recursively call once each go around and the answer should be bunnies * 2 since 2 ears are added for each bunny

## Exercise II


we have n-story building with plenty of eggs

egg breaks n-story >= f
egg ! break n-story < f
value of f
number of dropped + broken eggs is minimized

Need to find which floor = f has the least broken eggs

```
1) min_floor = 0, max_floor =n
2) mid_floor = n//2
3) if add breaks, then max_floor = mid_floor, repeat [2] and [3]
   if egg doesn't break, then min_floor = mid_floor, repeat [2] and [3]
4) return current floor if floor above or below if egg breaks
```

Runtime complexity: Was applied binary search ==> O(Log n)