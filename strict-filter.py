"""
strict-filter.py - строгий фильтр, который пропускает только разрешённые символы, перечисленные в фильтрах.
Фильтры - файлы с расширением .fltr

Usage:
  strict-filter.py (-h | --help)
  strict-filter.py [-i INPUT_FILE | --input-file INPUT_FILE] [-o OUTPUT_FILE | --output-file OUTPUT_FILE] [--filters-path PATH] [--filters-pick FILTER ...] [--interactive] [--interactive-new-filter]

Options:
  -h --help                 вывести справку
  -i --input-file           по умолчанию - stdin
  -o --output-file          по умолчанию - stdout
  --filters-path            путь до папки, в которой находятся файлы с фильтрами (по умолчанию - ./filters)
  --filters-pick            (TODO) список применяемых фильтров (если не указан, применяются все фильтры из --filters-path)
  --interactive             (TODO) интерактивный режим, в котором для каждого символа, который не проходит фильтры, задаётся вопрос пользователю. (Для создания и проверки фильтров)
  --interactive-new-filter  (TODO) интерактивный режим для создания нового фильтра

"""

from docopt import docopt
from sys import stdin, stdout
from os import getcwd

# преобразование параметров командной строки в dict
arguments = docopt(__doc__)
# print(arguments)

# разбираем параметры командной строки
if arguments["--input-file"]:
  input_file = arguments["INPUT_FILE"]
else:
  input_file = stdin

if arguments["--output-file"]:
  output_file = arguments["OUTPUT_FILE"]
else:
  output_file = stdout

if arguments["--filters-path"]:
  filter_path = arguments["PATH"]
else:
  filter_path = getcwd() + "/filters"



# прочитать строку из файла
# если режим не -ia
# пропустить строку через функцию filter
# вывести результат

# если режим -ia
# каждый символ строки пропустить через функцию filter
# если символ не прошёл фильтр
# задать вопрос пользователю: сохранить ли символ в фильтре
# если ответ - y
# сохранить символ во временный фильтр
# в конце сохранить временный фильтр в новый файл или добавить временный фильтр в существующий файл

