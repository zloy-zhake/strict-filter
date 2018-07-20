"""
==========
strict-filter.py - строгий фильтр, который пропускает только разрешённые символы, перечисленные в фильтрах.
Фильтры - файлы с расширением .fltr

Usage:
    strict-filter.py [-i INPUT_FILE | --input-file INPUT_FILE] [-o OUTPUT_FILE | --output-file OUTPUT_FILE] [--filters-path PATH] [--filters-pick FILTER ...] [--interactive] [--interactive-new-filter]
    strict-filter.py (-h | --help)

Options:
    -h --help                   вывести справку
    -i --input-file             по умолчанию - stdin
    -o --output-file            по умолчанию - stdout
    --filters-path              путь до папки, в которой находятся файлы с фильтрами (по умолчанию - ./filters)
    --filters-pick              (TODO) список применяемых фильтров (если не указан, применяются все фильтры из --filters-path)
    --interactive               (TODO) интерактивный режим, в котором для каждого символа, который не проходит фильтры, задаётся вопрос пользователю. (Для создания и проверки фильтров)
    --interactive-new-filter    ?? (TODO) интерактивный режим для создания нового фильтра

"""

from os import getcwd
from sys import stdin, stdout

from docopt import docopt

from utils import join_filters

# преобразование параметров командной строки в dict
arguments = docopt(__doc__)
# print(arguments)

# разбираем параметры командной строки
# входные данные либо из указанного файла, либо с stdin
if arguments["--input-file"]:
    with open(arguments["INPUT_FILE"], mode="r") as input_f:
        input_data = input_f.readlines()
else:
    input_data = stdin

# строка для результатов фильтрации
output_data = ""

# путь до папки с фильтрами
if arguments["--filters-path"]:
    filter_path = arguments["PATH"]
else:
    filter_path = getcwd() + "/filters"

# собираем все доступные/требуемые фильтры в один set
all_filters = join_filters(path=filter_path)

# прочитать строку из файла
# TODO если режим не --interactive
# пропустить строку через функцию filter
# записать результат в output_data
for line in input_data:
    for item in filter(lambda char: char in all_filters, line):
        output_data += item

# вывести результат либо в указанный файл, либо в stdout
if arguments["--output-file"]:
    with open(arguments["OUTPUT_FILE"], mode="w") as output_file:
        print(output_data, file=output_file)
else:
    print(output_data)

# TODO
# если режим --interactive
# каждый символ строки пропустить через функцию filter
# если символ не прошёл фильтр
# задать вопрос пользователю: сохранить ли символ в фильтре
# если ответ - y
# сохранить символ во временный фильтр
# в конце сохранить временный фильтр в новый файл или добавить временный фильтр в существующий файл
