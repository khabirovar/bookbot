from stats import count_words, count_char, reorder_dict
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    content = get_book_text(file_path)

    print("----------- Word Count ----------")
    num_words = count_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars = count_char(content)
    sorted_list = reorder_dict(chars)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")


main()
