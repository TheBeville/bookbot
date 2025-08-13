def get_num_words(booktext):
    return len(booktext.split())

def character_frequency(booktext):
    freq = {}
    for char in booktext:
        if char.lower().isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq

def sort_by(count):
    return count["num"]

def sorted_char_frequency(booktext):
    dict_list = []
    freq = character_frequency(booktext)
    for char, count in freq.items():
        dict_list.append({"char": char, "num": count})
    return sorted(dict_list, key=sort_by, reverse=True)