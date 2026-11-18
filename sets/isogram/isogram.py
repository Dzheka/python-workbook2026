def is_isogram(text: str):
    letters = [char for char in text.lower() if char.isalpha()]
    return len(list(letters)) == len(set(letters))
    
  


if __name__ == "__main__":
    print(is_isogram("lumberjacks"))  # True
    print(is_isogram("isograms"))  # False
    print(is_isogram("Alphabet"))  # False
    print(is_isogram("thumbscrew-japingly"))  # True
    print(is_isogram("Emily Jung Schwartzkopf"))  # True
    print(is_isogram(""))  # True
