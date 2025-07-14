def word_count(book_text):
    word_count = len(book_text.split())
    return word_count

def unique_chars(book_text):
    book_text_lower = book_text.lower()
    unique_chars_count = {}

    for char in book_text_lower:
        if char not in unique_chars_count:
            unique_chars_count[char] = 1
        else:
            unique_chars_count[char] += 1 
    return(unique_chars_count)

def dict_sort(dictonary):
    dict_list = []
    for dict in dictonary:
        if dict.isalpha():
            dict_list.append({"char":dict, "num": dictonary[dict] })
    def sort_on(items):
        return items["num"]
    dict_list.sort(reverse=True, key=sort_on)
    for dict in dict_list:
        print(f"{dict["char"]}: {dict["num"]}")