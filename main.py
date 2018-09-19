class Pali:
    def isPalindrome(string):
        left_pos = 0
        right_pos = len(string) - 1
        while right_pos >= left_pos:
            if string[left_pos].lower() != string[right_pos].lower():
                return False
            left_pos += 1
            right_pos -= 1
        return True
print(Pali.isPalindrome("daxad"))
