# word counter
def word_counter(text):
    
    word_list = text.split()

    return len(word_list)



def letter_counter(text):

    letter_counts = {}

    for letter in text:
        if letter.lower() in letter_counts:
            letter_counts[letter.lower()] = letter_counts[letter.lower()] + 1
        
        else:
            letter_counts[letter.lower()] = 1

    return letter_counts



def sort_dic(dic):
    
    sorted = []

    for k, v in dic.items():
        sorted.append({"char": k, "num": v})
    
    def sort_on(items):
        return items["num"]
    
    sorted.sort(reverse=True, key=sort_on)

    return sorted
