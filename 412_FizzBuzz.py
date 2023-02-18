from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_of_value = []
        for number in range(1, n + 1):
            if number % 15 == 0:
                number = "FizzBuzz"
                list_of_value.append(number)
                continue
            if number % 3 == 0:
                number = "Fizz"
                list_of_value.append(number)
                continue
            if number % 5 == 0:
                number = "Buzz"
                list_of_value.append(number)
                continue
            number = str(number)
            list_of_value.append(number)
        return list_of_value


print(Solution().fizzBuzz(20))
