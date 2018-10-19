'''
Given a string S and a set of words D, find the longest word in D that is a
subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can
be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple",
"bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter
than "apple".
The word "bale" is not a subsequence of S because even though S has all the
right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
'''

def is_substring(s, w):
    if len(w) > len(s):
        return False
    if s == w:
        return True
    j = -1
    for i in range(len(w)):
        if w[i] not in s[j+1:]:
            return False
        if w[i] in s:
            j = s.index(w[i]) + 1
            if j + 1 == len(w):
                return False
    return True

def find_largest_subsequence(S, D):
    D = sorted(D, key=lambda w: len(w), reverse=True)
    for w in D:
        if is_substring(S, w):
            return w

if __name__ == '__main__':
    S = "abppplee"
    D = ["able", "ale", "apple", "bale", "kangaroo"]
    print(find_largest_subsequence(S, D))
