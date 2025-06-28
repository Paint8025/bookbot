from stats import get_num_words, count_characters, dict_to_sorted_list
import sys

def get_book_text(filepath):

    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def main(filepath):
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    character_dictlist = dict_to_sorted_list(count_characters(book_text))

    report = str('============ BOOKBOT ============\n')
    report += f'Analyzing book found at {filepath}...\n'
    report += '----------- Word Count ----------\n'
    report += f'Found {word_count} total words\n'
    report += '--------- Character Count -------\n'

    for item in character_dictlist:
        if item["char"].isalpha():
            report += f'{item["char"]}: {item["num"]}\n'

    report += '============= END ==============='

    print(report)

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    main(sys.argv[1])