class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            length = 0

            while s[i] != "#":
                length = length * 10 + ord(s[i]) - ord("0")
                i += 1

            i += 1

            res.append(s[i:i + length])

            i += length

        return res