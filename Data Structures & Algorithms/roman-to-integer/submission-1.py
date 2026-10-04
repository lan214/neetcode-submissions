class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s):
            ch = s[i]

            if i + 1 < len(s):
                ch2 = s[i+1]
            
            if ch == 'I' and ch2 == 'V':
                total += 4
                i += 2
            elif ch == 'I' and ch2 == 'X':
                total += 9
                i += 2
            elif ch == 'X' and ch2 == 'L':
                total += 40
                i += 2
            elif ch == 'X' and ch2 == 'C':
                total += 90
                i += 2
            elif ch == 'C' and ch2 == 'D':
                total += 400
                i += 2
            elif ch == 'C' and ch2 == 'M':
                total += 900
                i += 2
            elif ch == 'I':
                total += 1
                i += 1
            elif ch == 'V':
                total += 5
                i += 1
            elif ch == 'X':
                total += 10
                i += 1
            elif ch == 'L':
                total += 50
                i += 1
            elif ch == 'C':
                total += 100
                i += 1
            elif ch == 'D':
                total += 500
                i += 1
            elif ch == 'M':
                total += 1000
                i += 1
                
            
        return total