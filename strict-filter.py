"""
strict-filter.py - строгий фильтр, который пропускает только разрешённые символы, перечисленные в фильтрах.
Фильтры - файлы с расширением .fltr

Usage:
  strict-filter.py (-h | --help)
  strict-filter.py [-i INPUT_FILE | --input-file INPUT_FILE] [-o OUTPUT_FILE | --output-file OUTPUT_FILE] [--filters-path PATH] [--filters-pick FILTER ...] [--interactive] [--interactive-new-filter]

Options:
  -h --help                 вывести справку
  -i --input-file           (TODO) по умолчанию - stdin
  -o --output-file          (TODO) по умолчанию - stdout
  --filters-path            (TODO) путь до папки, в которой находятся файлы с фильтрами (по умолчанию - ./filters)
  --filters-pick            (TODO) список применяемых фильтров (если не указан, применяются все фильтры из --filters-path)
  --interactive             (TODO) интерактивный режим, в котором для каждого символа, который не проходит фильтры, задаётся вопрос пользователю. (Для создания и проверки фильтров)
  --interactive-new-filter  (TODO) интерактивный режим для создания нового фильтра

"""

from docopt import docopt

arguments = docopt(__doc__)
print(arguments)


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

