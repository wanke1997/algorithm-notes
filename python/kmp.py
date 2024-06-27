from typing import List


class KMP:
    def __init__(self) -> None:
        pass

    def preprocess(self, p: str) -> List[int]:
        "build a list to memorize the longest prefix which is also the suffix of the substring ending with current index"
        idxs = [0] * (len(p) + 1)
        k = 0
        # 1-indexed list, be careful!
        for idx, ch in enumerate(p):
            idx += 1
            if idx == 1:
                idxs[idx] = 0
                continue
            else:
                # 0-indexed while access string, be careful
                # do not need to modify the value of k here
                while k > 0 and p[k] != ch:
                    k = idxs[k]
                if p[k] == ch:
                    k += 1
                idxs[idx] = k
        return idxs

    def kmp_matching(self, idxs: List[int], p: str, t: str) -> List[int]:
        ans = []
        k = 0
        # 1-indexed list, be careful!
        for idx, ch in enumerate(t):
            idx += 1
            # find the longest valid pattern's prefix to match the text ending at idx
            while k > 0 and p[k] != ch:
                # shrink the window
                k = idxs[k]
            # extend the window if there is a match
            if p[k] == ch:
                # expand the window
                k += 1
            if k == len(p):
                # found an answer, add it to the list
                ans.append(idx - 1)
                k = idxs[k]
        return ans


if __name__ == "__main__":
    instance = KMP()
    p = "ababaca"
    t = "abababacababaca"
    idxs = instance.preprocess(p)
    print(idxs)
    res = instance.kmp_matching(idxs, p, t)
    print(res)
