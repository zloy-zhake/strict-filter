from os import listdir
from os.path import join


def join_filters(path: str) -> set:
    """
  Функция, перебирающая все фильтры (файлы с расширением .fltr) находящиеся в папке path
  и возвращающая set со всеми символами из этих файлов.
  """
    result_set = set()
    for item in listdir(path):
        if item.endswith(".fltr"):
            with open(join(path, item)) as filter_file:
                chars = filter_file.read()
                result_set.update(chars)
    return result_set


