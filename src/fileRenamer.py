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
Initially made to rename the files of a manga chapter downloaded from rawkuma with HakuNeko (because page 2 is a trashy ad). \n
Use it for whatever you want, if it's legal. Modify it as you want if you want. \n

Author: Okane (Zinnia Scans)
    - Twitter: @Okaneeeeeeeee_e / @ZinniaScans
    - Github: https://github.com/Okaneeee
    - MangaDex: https://mangadex.org/group/8bd939e5-dbcd-4ec8-b105-e6a19e8d8862/zinnia-scans
"""

# imports
import os
from time import sleep

# Class
class FileRenamer():
    def __renamer(self, path: str, file_extension: str, start: int = 0 , rename_format = "0"):
        """
            Rename any file in a folder, starting at a given number (default 0). \n
        """
        i: int = start # No need to rename the files before the start
        new_name : str = "0"

        for filename in os.listdir(path):

            if (filename != f"0{start-1}{file_extension}"): # No need to rename the file before the start
                print(filename)
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
            
    def __remove_n(self, path: str, file_extension: str, start: int = 0 ):
        """
            Remove the "n_" at the beginning of the file name, added by the rename function (n_01.jpg -> 01.jpg)
        """
        for filename in os.listdir(path):

            if (filename != f"0{start-1}{file_extension}"):
                print(filename)

                original_name = path + filename
                new_name = path + filename[2:] # Get the original name without the "n_" (basically remove the first two characters)

                os.rename(original_name, new_name)

    def rename(self, path: str, file_extension: str, start: int = 0 , rename_format = "0"):
        """
            Rename any file in a folder, starting at a given number (default 0). \n

        Args:
            path (str): The path to the folder containing the files to rename
            start (int, optional): The number of the first file to rename. Defaults to 0. (If you want to start renaming at the second file (02, 03...), put 2)
            file_extension (str, optional): The extension of the files to rename and the extension of the renamed files. Defaults to ".jpg".
            rename_format (str, optional): The format of the renamed files. Defaults to "0". Can be "00", "000", etc. (0=01, 00=001, etc.)
        """
        self.__renamer(path, file_extension, start, rename_format)
        sleep(3)
        self.__remove_n(path, file_extension, start)

# tests
if __name__ == '__main__':

    fr = FileRenamer()
    fr.rename("", 2)