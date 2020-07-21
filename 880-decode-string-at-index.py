class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = 0
        for i, c in enumerate(S):
            if c.isdigit():
                n *= int(c)
            else:
                n += 1
            if n >= K:
                break

        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                n /= int(c)
                K %= n

            else:
                if K == 0 or K == n:
                    return c

                n -= 1
