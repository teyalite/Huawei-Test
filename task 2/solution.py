# Binary Search to find the index of the minimum knapsack size
# Time complexity is O(log(m)) and m = len(array)
def binary_search(array: list[int], left: int, right: int, x: int):
    while left <= right:
        middle = left + (right - left) // 2

        if array[middle] == x:
            return middle
        elif array[middle] < x:
            left = middle + 1
        else:
            right = middle - 1

    return left


# Solution that finds the minimum knapsack C such that all wi items fits in it
# Time complexity is O(n + log(m)) where:
# m is the number of knapsacks
# n is the number of items
def solution(w: list[int], c: list[int]):
    x = sum(w)

    return c[binary_search(c, 0, len(c) - 1, x)]


# Test cases defined as follows (items, knapsacks, minimal knapsack)
test_cases = [([2, 6], [2, 4, 8, 16], 8)]

if __name__ == "__main__":
    for test in test_cases:
        print("\n----------------------------------------------------------------\n")

        print("Items are: ", test[0]),
        print("Knapsacks are: ", test[1]),

        minimal = solution(test[0], test[1])

        if minimal != test[2]:
            print(f"Test case failed:\nExpected: {test[2]}\nGot: {minimal}")
        else:
            print("The minimal capacity knapsack is: ", minimal)

        print("\n----------------------------------------------------------------\n")
