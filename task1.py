import string


def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    f = open(path, "r")
    lines = f.readlines()
    lst = []
    for l in lines:
        lst.append(l[:-1])
    f.close()
    return lst



def row_extend(row):
    """
    list -> list

    Returns the extended row with sorted vowels by their frequency in the row.
    """
    dct = {}
    lst = []
    for line in row:
        for el in line:
            el1 = el.lower()
            if el1 in "oiaeu":
                if el1 not in dct.keys():
                    dct[el1] = 1
                else:
                    dct[el1] += 1
    lst1 = []
    dict1 = {}
    for i in dct.keys():
        dict1[dct.get(i)] = i
    for i in dict1.keys():
        lst.append(i)
    lst_sorted = sorted(lst, reverse=True)
    for i in lst_sorted:
        lst1.append(dict1.get(i))
    return lst1

def column_extend1(column):
    """
    list -> list

    Returns the extended column with sorted consonants without duplication.
    """
    result = []
    max_len = max([len(column[i]) for i in range(len(column))])
    for line in column:
        while len(line) <= max_len:
            line += " "
    for el in range(len(column[0])):
        temp_line = ""
        for line in column:
            temp_line += line[el]
        unsorted = ""
        for letter in temp_line:
            if letter not in "oiaeuOIAEU.() ":
                unsorted += letter
        unsorted_lst = sorted(list(unsorted))
        result.append(unsorted_lst)
    return result

def column_extend(column):
    """
    list -> list

    Returns the extended column with sorted consonants without duplication.
    """
    result = []
    for el in column:
        if el not in result:
            result.append(el)
    return result
# column_extend(input_data("text_1.txt"))


def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and
    outputs to the other file.
    """
    file2 = open(out_path, "a")
    lines = input_data(in_path)
    for line in lines:
        lst = row_extend(line)
        result = column_extend(lst)
        col = " "
        for i in result:
            col += i
        line2print = line+col+"\n"
        file2.write(line2print)
    col = column_extend1(input_data("text_1.txt"))
    max_len = max([len(col[i]) for i in range(len(col))])
    for spysok in col:
        while len(spysok) <= max_len:
            spysok.append(" ")
    for i in range(len(col[0])):
        for spysok in col:
            file2.write(spysok[i])
        file2.write("\n")
    file2.close()


characters_info("text_1.txt", "koko4.txt")