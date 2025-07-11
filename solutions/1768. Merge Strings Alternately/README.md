# Merge Strings Alternatively
Difficulty: Easy

Topics: Two Pointers, String 

### Problem Definition
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string

Return the merged string.

Example 1:

```
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```
### Constraints
- 1 <= `word1.length`, `word2.length` <= 100
- `word1` and `word2` consist of lowercase English letters.

---

## Linear Approach!
Let's start with something very intuitive. 

If we are familiar with `Merge Sort`, the exhaustion of the characters of each word will look familiar. We will instantiate two pointers/indices for the two words, and parse them until one is exhausted. Once one is exhausted, we will append the remaining unparsed characters to the concatenated string.

#### Time Complexity: O(n+m)
This linear approach goes through each character of both words, which takes `n+m` times where `n` is the length of `word1` and `m` is the length of `word2`. The last condition for appending the remaining characters also take as much time as the linear approach.

Runtime was `37 ms`, which beats 64.36% of all submissions.

#### Space Complexity: O(n+m)
We declared three variables: two pointer/index variables and a string of n + m size, similar to the representations of n and m earlier. The additional two variables can be neglected as they don't grow in terms of the input size.

Memory required was `17.66 MB`, which beats 73.78% of all submissions.

--- 

## Cleaner Linear Approach
As the previous method's runtime was okay at best, we need to optimize it!

If we think about it, we can use a single while loop to parse both words until both are exhausted
- Instead of having an `and` condition, an `or` one would allow us to parse both of them until both are finished.
- Use the `if` conditions outside and implement them inside to avoid `index out of range`.


#### Time Complexity: O(n+m)
Same with earlier, this linear approach goes through each character of both words, which takes `n+m` times where `n` is the length of `word1` and `m` is the length of `word2`. This time, there is no last condition which helps the runtime be better.

Runtime was `30 ms`, which beats 93.89% of all submissions.

#### Space Complexity: O(n+m)
Same as earlier, we declared three variables: two pointer/index variables and a string of n + m size, similar to the representations of n and m earlier. The additional two variables can be neglected as they don't grow in terms of the input size.

Memory required was also `17.68 MB`, which beats 73.78% of all submissions.