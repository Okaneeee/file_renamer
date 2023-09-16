##############################################################
##############################################################
#######     ____           __                  __      #######
#######    / __/_  _______/ /__     ____ _____/ /____  #######
#######   / /_/ / / / ___/ //_/    / __ `/ __  / ___/  #######
#######  / __/ /_/ / /__/ ,<      / /_/ / /_/ (__  )   #######
####### /_/  \__,_/\___/_/|_|     \__,_/\__,_/____/    #######
##############################################################
##############################################################

"""
Initially made to rename the files of manga chapters downloaded from Rawkuma with HakuNeko (because page 2 is a trashy ad). \n
Use it for whatever you want, if it's legal. Modify it as you want if you want. \n

Author: Okane (Zinnia Scans)
    - Twitter: @Okaneeeeeeeee_e / @ZinniaScans
    - Github: https://github.com/Okaneeee
    - MangaDex: https://mangadex.org/group/8bd939e5-dbcd-4ec8-b105-e6a19e8d8862/zinnia-scans
"""

# imports
import os
from time import sleep

# class
class FileRenamer():
    def __init__(self) -> None:
        self.sleepTime: int

    def __setSleepTime(self, filelist: list[str]):
        """
            Set the sleep time depending on the number of files to rename.
        """
        if len(filelist) <= 30:
            self.sleepTime = 2
        elif len(filelist) <= 60:
            self.sleepTime = 3
        elif len(filelist) <= 120:
            self.sleepTime = 5
        elif len(filelist) <= 1000:
            self.sleepTime = 10
        else:
            self.sleepTime = 20

    def __renamer(self, path: str, file_extension: str, start_file_name: str, start_number: int, rename_format: str):
        """
            Rename any file in a folder, starting at a given number and avoid dupes. \n
        """
        i: int = start_number # No need to rename the files before the start
        new_name : str = rename_format

        self.__setSleepTime(os.listdir(path))

        for filename in os.listdir(path):

            if (filename != f"{start_file_name}{file_extension}"): # No need to rename the file before the start
                new_name += str(i)

                # File renaming
                new_name = f"n_{new_name}{file_extension}" # Setting the new name, n_ avoids duplication and bugs
                original_name = path + filename # Getting the original name
                new_name = path + new_name # Renaming the file

                os.rename(original_name, new_name) # Rename the file

                # Checks
                if i >= 9: # Reset the new_name variable (no 010.jpg)
                    new_name = ""
                else:
                    new_name = "0"

                i += 1
            
    def __remove_n(self, path: str, file_extension: str, start_file_name: str):
        """
            Remove the "n_" at the beginning of the file name, added by the rename function (n_01.jpg -> 01.jpg)
        """
        for filename in os.listdir(path):

            if (filename != f"{start_file_name}{file_extension}"):

                original_name = path + filename
                new_name = path + filename[2:] # Get the original name without the "n_" (basically remove the first two characters)

                os.rename(original_name, new_name)

    def rename(self, path: str, file_extension: str, start_file_name: str = "00", start_number: int = 0 , rename_format: str = ""):
        """
            Rename every file in a folder, in alphabetical order, starting at a given number (default 0) and a given file (00.file_extension). \n

        Args:
            path (str): The path to the folder containing the files to rename
            file_extension (str, optional): The extension of the files to rename and the extension of the renamed files. Defaults to ".jpg".
            start_file_name (str, optional): The name of the first file to rename +1. Defaults to "00" (If you want to start renaming at the second file (02, 03...), put "01")
            start_number (int, optional): The number of the first file to rename. Defaults to 0. (If you want to start renaming at the second file (02, 03...), put 2)
            rename_format (str, optional): The format of the renamed files. Defaults to blank. Can be "0", "00", etc. (""=1, 0=01, 00=001, etc.)
        """
        self.__renamer(path, file_extension, start_file_name, start_number, rename_format)
        sleep(self.sleepTime) # Wait X seconds before removing the "n_" (to avoid dupe bugs)
        self.__remove_n(path, file_extension, start_file_name)

# tests
if __name__ == '__main__':
    PATH: str

    fr = FileRenamer()
    fr.rename(PATH, ".jpg", "01", 2, "0")