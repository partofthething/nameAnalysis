"""
Scans text for first names and prints out most common ones as document goes on

Useful for analyzing journals or whatever.
"""

FEMALE = 0
MALE = 1
EITHER = 2

def read_names(filename):
    """
    read potential first names from data library
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
    look through file for names
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
    Mangles a word and gets rid of contractions so "John's" shows up as "john"
    """
    word = word.lower()
    if "'" in word and word not in ["don't", "haven't"]:
        word = word.split("'")[0]
    return word

def rank(name_results):
    divisions = 25
    show = 8

    for names in grouper(name_results, divisions):
        names_here, _word_num_here = zip(*names)
        counts = []
        for name in uniquify(names_here):
            counts.append((names_here.count(name), name))
        counts.sort()
        counts.reverse()
        print ''.join(['{0:10s}'.format(name) for _count, name in counts[:show]])


def uniquify(seq):
    # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

def grouper(iterable, n, fillvalue=(None, None)):
    """break list into n chunks

    """
    num = float(len(iterable)) / n
    l = [ iterable [i:i + int(num)] for i in range(0, (n - 1) * int(num), int(num))]
    l.append(iterable[(n - 1) * int(num):])
    return l

def make_name_data(chicks, dudes):
    """
    makes convenient data structure about names
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

