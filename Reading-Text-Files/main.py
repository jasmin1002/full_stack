# Read text from a file, and count the occurence of words in that text

def read_file_content(filename): 
    f = open(filename)
    text = f.read()
    f.close()
    return text


def count_words():
    text = read_file_content("./story.txt")

    # new list
    new_text = []
    occurrence = {}
    punctuation = '''.,!:"^`-_'\n()\[]{}@;?/'''
    
    # Remove punctuation marks
    for mark in punctuation:
        text = text.replace(mark, "")

    # Remove empty space from beginning and ending
    # And separate string into words   
    text = text.strip().split(' ')

    # Remove any empty string
    new_text =[word.lower() for word in text if word != '']

    # Count number of occurrence of each word
    for show in new_text:
        occurrence[show] = new_text.count(show)
        
    return occurrence

print(count_words())
