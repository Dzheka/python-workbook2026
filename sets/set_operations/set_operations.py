def uniques(values: list) -> set:
  result = set()
  for v in values:
    result.add(v)
  return result


def union(set1: set, set2: set) -> set:
  result = set()
  for x in set1:
    result.add(x)
  for x in set2:
    result.add(x)
  return result


def intersection(set1: set, set2: set) -> set:
  result = set()
  for x in set1:
    if x in set2:
      result.add(x)
  return result


def is_subset(subset: set, superset: set) -> bool:
  for x in subset:
    if x not in superset:
      return False
  return True


def symmetric_diff(set1: set, set2: set) -> set:
  result = set()
  for x in set1:
    if x not in set2:
      result.add(x)
  for x in set2:
    if x not in set1:
      result.add(x)
  return result


if __name__ == "__main__":
  print(uniques([2, 3, 3, 5, 5, 5]))  # {2, 3, 5}
  print(union({2, 3, 5}, {5, 7, 11}))  # {2, 3, 5, 7, 11}
  print(intersection({2, 3, 5, 7}, {5, 7, 11, 13}))  # {5, 7}
  print(is_subset({2, 3}, {2, 3, 5, 7}))  # True
  print(is_subset({2, 11}, {2, 3, 5, 7}))  # False
  print(symmetric_diff({2, 3, 5}, {3, 5, 7}))  # {2, 7}