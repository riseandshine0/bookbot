def count_words(text):
    word_counter = 0
    for word in text.split():
        word_counter += 1
    return word_counter

def count_chars(text):
    counted_chars = {}
    for char in text:
        if char.lower() not in counted_chars:
            counted_chars[char.lower()] = 1
        else:
            counted_chars[char.lower()] += 1 
    return counted_chars # returns {'char': int}

def sort_on(items):
    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    return items["num"]

def sorted_dict(dict_in):
    new_list = []
    for char_c, count in dict_in.items():
        new_list.append({"char": char_c, "num": count})
    new_list.sort(reverse=True, key=sort_on)    
    return new_list