
def count_words(text):
    return len(text.split())
def count_characters(text):
    chars = dict()
    for char in text:
        c = char.lower()
        if not char.isalpha():
            continue
        if c in chars.keys():
            chars[c]+=1
        else:
            chars[c] = 1
    return chars
def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        print('--- Begin report of books/frankenstein.txt ---')
        print('{} words were found in the document\n'.format(count_words(content)))
        chars = count_characters(content)
        for char in chars.keys():
            print("The '{}' character was found {} times".format(char, chars[char]))

main()