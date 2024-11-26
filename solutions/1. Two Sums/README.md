# Two Sums
Difficulty: Easy
Topics: Array, Hash Table

### Problem Definition
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers* such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
```
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
```
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
### Constraints
- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- Only one valid answer exists.

---

## Brute-Force!
Let's start with something very intuitive. 

As we are given a set of numbers in an array, we can set a number as our constant, and add it to every other element and check if they match the `target` value. We will do it for every element, which will take some time, but will get the job done!

As the problem guarantees that there is a solution, as soon as we find a pair that matches the description, we can return the indices of the pair of values.

#### Time Complexity: O(n^2)
The brute-force method makes use of a nested loop, wherein we will set a certain value as our main value, and compare it to the rest of the values. The outer loop takes `n` times, and it then runs an inner for-loop that also takes `n` times.

Runtime was `4137 ms`, which beats 5.00% of all submissions.

#### Space Complexity: O(1)
We only need to declare looping variables such as `i` and `j` to iterate through the array. Both variable's space allocations are constant regardless of the size of the input, thus, its space complexity is constant.

Memory required was `17.05 MB`, which beats 8.94% of all submissions.

--- 

## Two-Pointers
As the previous method's runtime was okay at best, we need to optimize it!

If we think about it, if the array was sorted from lowest to highest values, we will find out about the following:
- If their sum is bigger than `target`, then we need to replace the highest value by the value lower than it.
- If their sum is smaller than `target`, then we need to replace the lowest value by the value higher than it.

We will do this process repeatedly until we reach the solution! But a new problem arises from our method -- the problem asks us to return the original indices of the two solution. To amend this, we need to create a temporary copy of the original array `nums`, and if we find the solution, we can just ask for the original index of the solutions using the method `.index()`. 

#### Time Complexity: O(nlogn)
The two-pointers approach will only loop the array once, as both pointers from the start and end point approaches the middle. In addition to that, we also used a sorting algorithm for our temporary array, which we can assume to have a time complexity of `O(nlogn)` if its *merge sort* or *quick sort*. If it was *counting sort*, then maybe just `O(n)`, but it might struggle with longer arrays. Adding these two complexities, we can simplify them and arrive at a general runtime of `O(nlogn)`.

Runtime was `3 ms`, which beats 54.01% of all submissions.

#### Space Complexity: O(n)
As we need a temporary array to sort the values, we need to create a similar-sized array to the given. That will consume `n` amounts of space.

Memory required was also `18.05 MB`, which beats 8.94% of all submissions.

--- 

## Hash Table
The two-pointer approach was already good, but what if we don't need to sort the elements to reduce the runtime?

A *hash table* allows us to store values in it and access those *values* in constant time using *keys*. What this allows us to do is we can subtract a given number to the `target` value, and check if the result exists in our hash table that contains all the array's original value. If it does exists, and it has a different index than the current number, then we have our solution!

#### Time Complexity: O(n)
The hash table approach allows us to run two separate *n-loops*, one for storing the values of the array to the hash table along with the index, and one that iterates through it, finding the solution. Adding both runtimes, we will arrive at a general runtime of `O(n)`.

Runtime was `0 ms`, which beats 100.00% of all submissions.

#### Space Complexity: O(n)
As we need a hash table to store the values, we need to allot a similar-sized space for it, which is around *n* number of spaces.

Memory required was also `18.34 MB`, which beats 5.23% of all submissions.