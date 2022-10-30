from pathlib import Path
import os
from ctypes import windll
import string
from typing import Generator


def get_all_drives_non_psutil() -> tuple[Path]:
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(Path(f"{letter}:\\ ").resolve())
        bitmask >>= 1

    return tuple(drives)


def iter_all_git_folder(in_drive: Path) -> Generator[Path, None, None]:
    recycle_bin_name = "$Recycle.Bin".casefold()

    for dirname, folderlist, filelist in os.walk(in_drive, True):

        if ".git" in folderlist and not dirname.casefold().endswith(recycle_bin_name):
            yield Path(dirname)
            folderlist.clear()
            filelist.clear()


if __name__ == '__main__':
    for drive in get_all_drives_non_psutil():

        for git_folder in iter_all_git_folder(drive):
            print(git_folder, flush=True)

            print("", flush=True)
