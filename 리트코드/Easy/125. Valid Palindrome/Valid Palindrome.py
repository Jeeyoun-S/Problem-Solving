class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss_list = []
        for ss in s:
            sss = ss.lower()
            if sss.isalnum():
                ss_list.append(sss)
        for i in range(len(ss_list)//2):
            if ss_list[i] != ss_list[-i-1]:
                return False
        return True
