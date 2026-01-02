def get_num_words(file_path):
    with open(file_path) as f:
        return f.read().split() 

def get_characters_num(file_path):
    with open(file_path) as f:
        amount = {}
        text = f.read()
        for char in text.lower():
            if char in amount:
                amount[char] += 1
            else:
                amount[char] = 1
        return amount

def sort_on(item):
    return item[1]

def sorted_dict(unsorted_dict):
    return unsorted_dict.sort(reverse=True, key=sort_on)

def print_sorted_dict(dict):
    sorted_items = sorted(dict.items(), key=sort_on, reverse=True)
    for item in sorted_items:
        print(f"{item[0]}: {item[1]}")
        