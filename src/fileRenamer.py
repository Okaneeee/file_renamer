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

# Class
class FileRenamer():
    def __renamer(self, path: str, start: int = 0):
        """
            Rename the files of a manga chapter downloaded from rawkuma with HakuNeko (because page 2 is a trashy ad). \n
            The first file is not renamed because it's not displaced.
        """
        i: int = start # No need to rename the files before the start
        new_name : str = "0"

        for filename in os.listdir(path):

            if filename != f"0{start-1}.jpg": # No need to rename the file before the start
                new_name += str(i)

                # File renaming
                new_name = "n_" + new_name + ".jpg" # Setting the new name
                original_name = path + filename # Getting the original name
                new_name = path + new_name # Renaming the file

                os.rename(original_name, new_name) # Rename the file

                # Checks
                if i >= 9: # Reset the new_name variable (no 010.jpg)
                    new_name = ""
                else:
                    new_name = "0"

                i += 1
            
    def __remove_n(self, path: str):
        """ Remove the "n_" at the beginning of the file name, added by the rename function (n_01.jpg -> 01.jpg)

        Args:
            path (str): _description_
        """
        for filename in os.listdir(path):

            if filename != "01.jpg":
                original_name = path + filename
                new_name = path + filename[2:] # Get the original name without the "n_" (basically remove the first two characters)

                os.rename(original_name, new_name)

    def rename(self, path: str, start: int = 0):
        self.__renamer(path)
        self.__remove_n(path)

# tests
if __name__ == '__main__':
    fr = FileRenamer()
    fr.rename("", 2)