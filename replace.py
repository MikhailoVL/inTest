import os
import sys


def replace(path, old_string, new_string, line_number=None):
    """

    :param path: path to the file
    :param old_string: string to replace
    :param new_string:  the new string to replace with
    :param line_number:  in which line in the file to replace (if empty, then replace all)
    """
    if not os.path.isfile(path):
        print(f"File path {path} does not exist. Exiting...")
        sys.exit()

    if not line_number:
        # line number not passed
        data = new_string
    else:
        with open(path, "r") as f:
            data = f.readlines()

        data[line_number-1] = data[line_number-1].replace(old_string, new_string)

    with open(path, "w") as f:
        f.writelines(data)


replace("wer.txt", "sderr", "wer", 2)
