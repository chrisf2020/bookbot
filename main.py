import sys
from stats import get_num_words, get characters_num, print_sorted dict, sorted dict


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path to books")
    sys.exit(1)

print("============= BOOKBOT =============")
print("Analyzing book found at", sys.argv[1])

print("----------- Word Count ----------")
print(f"Found {len(get_num_words(sys.argv[1]))} total words")
print("-------- Character Count --------")

print_sorted_dict(get_characters_num(sys.argv[1]))
print("============= END ===============")