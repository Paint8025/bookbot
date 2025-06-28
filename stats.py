def get_num_words(book_text):
    wordlist = book_text.split()
    word_count = len(wordlist)
    return word_count

def count_characters(book_text):
    char_count = dict()
    lowercase_text = book_text.lower()
    for character in lowercase_text:
        if character in char_count.keys():
            char_count[character] += 1
        else:
            char_count[character] = 1
    
    return char_count

def dict_to_sorted_list(unsorted_dict):
    unsorted_list = []

    for key in unsorted_dict:
        unsorted_list.append({"char" : key, "num" : unsorted_dict[key]})
    
    unsorted_list.sort(reverse=True, key=sort_dictlist_by_num)

    return unsorted_list
    

def sort_dictlist_by_num(item):
    return item["num"]
    