def merge_sort(list1: list[int], list2: list[int]) -> list[int]:
    ans = list1
    for i in list2:
        ans.append(i)
    return sorted(ans)
if __name__ == "__main__":
    # Test your function
    print(merge_sort([2, 5, 11], [3, 7, 13]))  # [2, 3, 5, 7, 11, 13]
    print(merge_sort([2, 3], [5, 7]))          # [2, 3, 5, 7]
