import zipfile

archive = "voyna-i-mir.zip"  # Путь к архиву.
directory_to_extract_to = "vim"  # Путь, куда будет распакован архив.
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(directory_to_extract_to)

str_open = open("vim/voyna-i-mir.txt", 'r', encoding='utf-8')
list_file = str_open.read()
count_dict = {}
count_letter = 0
for letter in list_file:
    if (letter.isalpha()):
        x = count_dict.get(letter, 0)
        count_dict[letter] = x + 1
        count_letter += 1
count_letter_dict = [(k, "{:8.6f}".format(count_dict[k] / count_letter)) for k in count_dict.keys()]
str_open.close()
count_letter_dict.sort(key=lambda x: x[1], reverse=True)
print()
for i in count_letter_dict:
    print(i[0] + " " + i[1])


"""
import collections
import zipfile

def unzip(archive):
    zfile = zipfile.ZipFile(archive, "r")
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()

def collect_stats(file_name):
    result = {}
    if file_name.endswith(".zip"):
        unzip(file_name)
        file_name = "".join((file_name[:-3], "txt"))
    text_file = open(file_name, "r", encoding="utf-8")
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def print_stats(stats):
    print("+{:-^19}+".format("+"))
    print("|{: ^9}|{: ^9}|".format("буква", "частота"))
    print("+{:-^19}+".format("+"))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format("+"))

def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values()) # reverse=True) по убыванию
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict

file_name = "voyna-i-mir.zip"
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)
"""