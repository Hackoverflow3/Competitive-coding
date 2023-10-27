from collections import defaultdict
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        compressed = []
        count = 1
        prevchar = chars[0]

        for i in range(1, len(chars)):
            if chars[i] == prevchar:
                count += 1
            else:
                compressed.append(prevchar)
                if count > 1:
                    compressed += list(str(count))
                prevchar = chars[i]
                count = 1

        compressed.append(prevchar)
        if count > 1:
            compressed += list(str(count))

        chars[:] = compressed
        return len(compressed)