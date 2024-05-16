import os

def load_input(file_path: str):
    """Return input content from input file for a given exercise

    :param file_path: __file__ from exercise file
    :return: content of input file for this exercise
    """

    data_path = os.path.join(
        os.path.dirname(file_path),
        'inputs',
        os.path.basename(file_path).replace('.py', '.txt')
    )

    return open(data_path, 'r').read()
