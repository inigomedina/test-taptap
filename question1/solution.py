"""
Assumptions.

I assumme that string (S) contains is not empty.
I assume that S contains only lowercase a-z.
I assume that we are not dealing with specific language such as
English, Spanish, etc.
"""

from random import shuffle


def is_anagram_of_palindrome(s):
    letter_counts = {}
    for c in s:
        letter_counts[c] = letter_counts.get(c, 0) + 1
    num_odds = 0
    for v in letter_counts.values():
        if v % 2 == 1:
            num_odds += 1
    return num_odds <= 1

def scramble(s):
    lis = [ c for c in s ]
    shuffle(lis)
    return ''.join(lis)

def main():
    # Test a list of strings which are anagrams of palindromes.
    aops = ['kayak', 'ana', 'civic', 'radar']
    for s in aops:
        s_test = scramble(s)
        print "{} is an anagram of palindrome {}: {}".format(s_test, \
            s, is_anagram_of_palindrome(s_test))
    print
    # Test a list of strings which are not anagrams of palindromes.
    not_aops = ['inigo', 'python', 'luis']
    for s in not_aops:
        s_test = scramble(s)
        print "{} is an anagram of a palindrome: {}".format(s_test, \
            is_anagram_of_palindrome(s_test))

main()
