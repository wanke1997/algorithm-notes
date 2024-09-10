class DigitDP:
    def __init__(self) -> None:
        self.cache = {}

    def dfs(self, number: str, cur: int, is_num: bool, is_limit: bool, state: int) -> int:
        if cur == len(number):
            return 1 if is_num else 0
        elif (cur, is_num, is_limit, state) in self.cache:
            return self.cache[(cur, is_num, is_limit, state)]
        else:

            total = 0
            if not is_num:
                # 1. if the current state doesn't have any leading digit
                # we can try to skip to the next
                total += self.dfs(number, cur + 1, False, False, state)

            # 2. decide the min digit, if the current digit is leading, set it as 1 to prevent leading 0
            # Otherwise, start from 0
            min_digit = 0 if is_num else 1
            # 3. decide the max digit, if there is a limit, the maximum value will be the number[cur]
            # Otherwise, we can try till 9.
            max_digit = int(number[cur]) if is_limit else 9

            for digit in range(min_digit, max_digit + 1):
                if (state & (1 << digit)) != 0:
                    continue
                next_state = state | (1 << digit)
                # if the previous one has a limit AND it reaches the limit currently, we need to set the next limit as True
                if digit == max_digit and is_limit:
                    total += self.dfs(number, cur + 1, True, True, next_state)
                # Otherwise, there will be no more limits
                else:
                    total += self.dfs(number, cur + 1, True, False, next_state)

            self.cache[(cur, is_num, is_limit, state)] = total
            return total

    def solution(self, n: int) -> int:
        n_str = str(n)
        res = self.dfs(n_str, 0, False, True, 0)
        return res


if __name__ == "__main__":
    n = 20
    instance = DigitDP()
    res = instance.solution(n)
    print("For n={}, the answer is {}".format(n, res))

    n = 5
    instance = DigitDP()
    res = instance.solution(n)
    print("For n={}, the answer is {}".format(n, res))

    n = 1005
    instance = DigitDP()
    res = instance.solution(n)
    print("For n={}, the answer is {}".format(n, res))

    n = 11111
    instance = DigitDP()
    res = instance.solution(n)
    print("For n={}, the answer is {}".format(n, res))
