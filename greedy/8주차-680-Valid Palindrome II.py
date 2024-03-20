class Solution:
  def validPalindrome(self, s: str) -> bool:
    start, end = 0, len(s) - 1
    while start <= end:
      if s[start] != s[end]:
        case1 = s[start: end] # end 제거
        case2 = s[start + 1: end + 1]# start 제거
        return case1 == case1[::-1] or case2 == case2[::-1]
      start += 1
      end -= 1
    return True