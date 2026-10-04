class Solution:

    def __init__(self):
        self.delimiter_end = "|"
        self.sep = "/"
    
    def encode_word(self, s: str) -> str:
        arr = ["/|" if c == self.delimiter_end
                else "//" if c == self.sep
                else c
                for c in s]
        return "".join(arr)


    def encode(self, strs: List[str]) -> str:
        arr = [self.encode_word(s) + self.delimiter_end for s in strs]
        return "".join(arr)


    def decode(self, s: str) -> List[str]:
        result = list()
        i = 0
        word = list()
        while i < len(s):
            if s[i] == self.sep:
                i += 1
                word.append(s[i])
            elif s[i] == self.delimiter_end:
                result.append("".join(word))
                word.clear()
            else:
                word.append(s[i])
            i += 1
        return result
