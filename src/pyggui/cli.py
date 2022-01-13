"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m pyggui` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``pyggui.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``pyggui.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
import os

from pyggui.defaults import structures  # Import the structures package so we can fetch its path
from pyggui.helpers.file_handling import DirectoryReader


def find_environment_directory(path: str) -> str:
    """
    Function finds venv in passed path and returns path to its parent directory. If venv or env not found, returns
    None.

    Args:
        path (str): Path to find venv or env in.
    """
    path_list = path.split(os.sep)
    venv_dir = []
    for i, _dir in enumerate(path_list):
        if _dir in ["venv", "env"]:
            break
        elif i == len(path_list) - 1:
            return None
        else:
            venv_dir.append(_dir)

    return os.sep.join(venv_dir)


def copy_structure(from_dir: str, to_dir: str) -> None:
    """
    Function copies one structure to the next without copying already set directories / files.

    Args:
        from_dir ():
        to_dir ():
    """
    ignore = [".pyc"]
    dir_structure = DirectoryReader.get_structure(from_dir)
    pass


structures_path = structures.PATH  # Path of projects structures directory
base_structure_path = os.path.join(structures_path, "base")  # Path of base structure directory


def main(argv=sys.argv):
    """
    Creates a base directory structure for your project / game.

    Args:
        argv (list): List of arguments

    Returns:
        int: A return code
    """
    argument_dict = {
        "-t": None,
        "-p": None
    }
    call_path = argv[0]  # Get path of where call originated from, either some sort of venv or pythons path
    argv = argv[1:]  # Update arguments
    # Parse args into argument dictionary
    for arg in argv:
        split_arg = arg.split("=")
        argument_dict[split_arg[0]] = split_arg[1]

    # Check arguments are okay
    # Check path
    if not argument_dict["-p"]:  # If no path passed to create the structure in, try fetching venv position
        venv_parent_path = find_environment_directory(call_path)
        if not venv_parent_path:
            print("No directory path was specified and the call did not originate from inside a venv. "
                  "Pass a path by the -p argument; ex.: -p=some/path/to/directory, or call from inside a virtual "
                  "environment.")
            return
        else:
            argument_dict["-p"] = venv_parent_path

    # Check type of structure
    if not argument_dict["-t"]:
        argument_dict["-t"] = base_structure_path
    else:
        argument_dict["-t"] = base_structure_path
        pass  # Todo create for other structures

    # Start copying files from specified type of directory into set directory.
    copy_structure(from_dir=argument_dict["-t"], to_dir=argument_dict["-p"])

    return 0
