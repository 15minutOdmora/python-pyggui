"""
Module for building current game into an executable using pyinstaller.
"""

from typing import List


def main(argv: List[str]) -> int:
    """
    Main function for creating the structure needed to start developing a game using pyggui.

    Args:
        argv (List[str]): sys.argv, not including "build".

    Returns:
        int: Exit code
    """
    call_path = argv[0]  # Get path of where call originated from, either some sort of venv or pythons path
    print("Building...")

    return 0
