"""
Given an input string (s) and a pattern (p), implement wildcard pattern 
matching with support for '?' and '*' where:

  - ' ?' Matches any single character.
  - '*' Matches any sequence of characters (including the empty 
    sequence).

The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does 
not match 'b'.

 

Constraints:

  - 0 <= s.length, p.length <= 2000
  - s contains only lowercase English letters.
  - p contains only lowercase English letters, '?' or '*'.
"""
import re

class Solution:
    #Strategy: Regex comparision
        #1. Replace all instances of '*' in p with '.*'.
        #2. Replace all instances of '?' in p with '.'.
        #3. Use re.fullmatch() to check if the pattern evaluates to the
            #entire string.
        #4. If it does, return True.
        #5. Otherwise, return False.

    #Time complextiy: O(N * M) N = len(s) M = len(p)
    #Space complexity: O(1)
    def isMatch(self, s: str, p: str) -> bool:
        p = p.replace('*', '.*')
        p = p.replace('?', '.')
        if re.fullmatch(p, s, flags=re.DOTALL):
            print(f"{p} matches {s}")
            return True
        else:
            print(f"{p} doesn't match {s}")
            return False
            
    #Strategy: Brute force recursion
        #1. Convert s and p to lists.
        #2. Check if s and p are the same.
        #2. If they are, return True.
        #3. Otherwise, if only p is empty return False.
        #4. If only s is empty, it can only match a pattern filled with 
            #'*'. So, check if the first character of p is '*'.
        #5. If it is, return the result of isMatchRecursion('', p[1:])
        #6. Otherwise, return False
        #7. The only cases left will be where both s and p are not 
            #empty. So, we will compare the first character of each. If
            #p[0] is a '?' or the same as s[0], slice off the first
            #character of each and check if the remaining strings match.
        #8. If p[0] is a '*' then it could match as an empty string. So,
            #check isMatchRecursion(s, p[1:]).
        #9. A '*' could also match s[0]. So, check 
            #isMatchRecursion(s[1:], p)
        #10. Return True if any recursion evaluates to True and False
            #otherwise
        

    #Time complextiy: O(2 ^ (N + M)) N = len(s) M = len(p)
    #Space complexity: O(N + M)
    def isMatchRecursion(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(p)
        return self.solve(s, p)
        
    def solve(self, s, p):
        if s == p:
            return True
        elif not p:
            return False
        elif not s:
            if p[0] == '*':
                if self.solve([], p[1:]):
                    return True
        elif p[0] == '?' or p[0] == s[0]:
            if self.solve(s[1:], p[1:]):
                return True
        elif p[0] == '*':
            if self.solve(s[1:], p):
                return True
            if self.solve(s, p[1:]):
                return True
        return False
        
    #Strategy: Recursion with memoization
        #This strategy is exactly the same as the brute force recursion 
        #with the following additions:
        #1. Add an extra argument, memo, with a default value of an 
            #empty dictionary.
        #2. Create a key for each call by concatonating s a ',' and p.
        #3. Before any other checks are done, check to see if the key is
            #already in the memo.
        #4. If it is, return memo[key].
        #5. Otherwise, continue as in the original recursion algorithm.
        #6. Pass the memo to each recursive call.
        #7. Before returning any value, also add the value to the memo
            #using the unique key created.
        
    #Time complextiy: O(N ^ 2 + M ^ 2)) N = len(s) M = len(p)
    #Space complexity: O(N + M)
    def isMatchMemo(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(p)
        return self.solveMemo(s, p)
        
    def solveMemo(self, s, p, memo = {}):
        key = ''
        for x in s:
            key += x
        key += ','
        for y in p:
            key += y
        if key in memo:
            return memo[key]
        elif s == p:
            memo[key] = True
            return True
        elif not p:
            memo[key] = False
            return False
        elif not s:
            if p[0] == '*':
                if self.solveMemo([], p[1:], memo):
                    memo[key] = True
                    return True
        elif p[0] == '?' or p[0] == s[0]:
            if self.solveMemo(s[1:], p[1:], memo):
                memo[key] = True
                return True
        elif p[0] == '*':
            if self.solveMemo(s[1:], p, memo):
                memo[key] = True
                return True
            if self.solveMemo(s, p[1:], memo):
                memo[key] = True
                return True
        memo[key] = False
        return False
            
if __name__ == "__main__":
    test = Solution()
    print(test.isMatchMemo("aa", "a"))
    print(test.isMatchMemo("aa", "*"))
    print(test.isMatchMemo("cb", "?a"))
    print(test.isMatchMemo("abcdef", "a?c*f"))
    print(test.isMatchMemo(
          "bababbbbabababaabbaabbaababbbbbabaabbaaabababbaaabbbababbbbaaaaaabbbbbbabaaabbbbaababbbaaabaabaaababababaaabbbbbbababbabbbbabaabbabaabbabbbbaaabaabbbaaabaaaababbbbbabbbababbbaababaaaababaaaabbbbbbaaaabbb",
          "b*a*b*a****b**b*ab**ab*bb*abbb****babb**a*a*b*bb***aa*bb*b***bbba*bb*aa**b*a**b**b***a*bbbaa*bb***b*"))