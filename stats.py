def count_words(file_content):
    words = file_content.split()
    return len(words)


def count_char(file_content):
    text = file_content.lower()
    chars = dict()
    for char in text:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars


def reorder_dict(chars):
    reordered = list()
    for key in chars:
        val = chars[key]
        reordered.append({"char": key, "num": val})
    reordered.sort(reverse=True, key=lambda x: x["num"])
    return reordered
