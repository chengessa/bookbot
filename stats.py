def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(item):
    return item[1]  # item is a (key, value) tuple