"""
Scans text for first names and prints out most common ones as document goes on

Useful for analyzing journals or whatever.

"""

# controls
NUM_FILE_SEGMENTS = 25
NUM_TOP_NAMES = 8

# consts
FEMALE = 0
MALE = 1
EITHER = 2

def read_names(filename):
    """
    read potential first names from data library

    Get names from, for example, http://www.outpost9.com/files/WordLists.html
    See http://stackoverflow.com/questions/1803628/raw-list-of-person-names for other options.
    """
    names = []
    with open(filename) as f:
        for name in f:
            name = name.strip().lower()
            if len(name) > 2:
                names.append(name)
    return names


def scan_for_names(data_file_name, names):
    """
    look through text file for names
    """
    with open(data_file_name) as f:
        num_words = 0
        names_found = []
        for line in f:
            for word in line.split():
                num_words += 1
                word = process(word)
                if word in names:
                    names_found.append((word, num_words))
                    # print word
                # hack to prevent ann from "ann arbor" from showing up
                if word == 'arbor' and names_found[-1][0] == 'ann':
                    names_found.pop()
    return names_found

def process(word):
    """
    Mangle a word and gets rid of contractions so "John's" shows up as "john"
    """
    word = word.lower()
    if "'" in word and word not in ["don't", "haven't"]:
        word = word.split("'")[0]
    return word

def rank(name_results):
    """
    process the names found and print out the top few.
    """
    for names in chunk(name_results, NUM_FILE_SEGMENTS):
        names_here, _word_num_here = zip(*names)
        counts = []
        for name in uniquify(names_here):
            counts.append((names_here.count(name), name))
        counts.sort()
        counts.reverse()
        print ''.join(['{0:10s}'.format(name) for _count, name in counts[:NUM_TOP_NAMES]])


def uniquify(iterable):
    """
    Make unique list while preserving order.
    """
    unique = []
    for entry in iterable:
        if entry not in unique:
            unique.append(entry)
    return unique

def chunk(iterable, num_chunks, fillvalue=(None, None)):
    """break list into num_chunks chunks. Ugly.

    Stolen from the web somewhere.
    """
    num = float(len(iterable)) / num_chunks
    chunks = [iterable[i:i + int(num)] for i in range(0, (num_chunks - 1) * int(num), int(num))]
    chunks.append(iterable[(num_chunks - 1) * int(num):])
    return chunks

def make_name_data(chicks, dudes):
    """
    make convenient data structure about names.

    It separates out men and women in case future development wants to plot them in
    different colors or something.
    """
    names = {}
    for name in chicks:
        names[name] = FEMALE

    for name in dudes:
        if name in names:
            names[name] = EITHER
        else:
            names[name] = MALE

    return names

if __name__ == '__main__':
    chicks = read_names('female-names')
    dudes = read_names('male-names')
    name_lib = make_name_data(chicks, dudes)
    results = scan_for_names('data.txt', name_lib)
    rank(results)

