class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapper = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        if len(digits) == 1:
            return mapper[int(digits)]
        if len(digits) == 2:
            w = int(digits[0])
            x = int(digits[1])
            o = []
            for i in range(len(mapper[w])):
                for j in range(len(mapper[x])):
                    a = mapper[w][i]
                    b = mapper[x][j]
                    o.append(a + b)
            return o
        if len(digits) == 3:
            w = int(digits[0])
            x = int(digits[1])
            y = int(digits[2])
            o = []
            for i in range(len(mapper[w])):
                for j in range(len(mapper[x])):
                    for k in range(len(mapper[y])):
                        a = mapper[w][i]
                        b = mapper[x][j]
                        c = mapper[y][k]
                        o.append(a + b + c)
            return o
        if len(digits) == 4:
            w = int(digits[0])
            x = int(digits[1])
            y = int(digits[2])
            z = int(digits[3])
            o = []
            for i in range(len(mapper[w])):
                for j in range(len(mapper[x])):
                    for k in range(len(mapper[y])):
                        for l in range(len(mapper[z])):
                            a = mapper[w][i]
                            b = mapper[x][j]
                            c = mapper[y][k]
                            d = mapper[z][l]
                            o.append(a + b + c + d)
            return o
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("5234"))
