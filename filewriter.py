from pathlib import Path
from folders import Folders


class FileWriter:
    """
    This class manages the scoreboard's text files.
    When a new point is added to the scoreboard,
    this class is called to set the new local or visitor point in its text file.
    When the txt file is changed, these changes are reproduced in the OBS application.
    """
    def __init__(self, info_path):
        self._rootpath = Path(info_path)
        self._folder_path = Folders(self._rootpath)
        self._set = 0
        self.actual_local = 0
        self.actual_visiting = 0
        self._folder_path.check_folders()

    def change_set(self, set_mch: int):
        self._folder_path.local = set_mch
        self._folder_path.visiting = set_mch

    def set_local_value(self, point):
        """
        Change the value to the actual local text file with the new point value.
        :param point: New poit value.
        :return:
        """
        file_path = self._folder_path.local
        with open(file_path, "w+") as f:
            f.write(f'{point}')

    def set_visiting_value(self, point):
        """
        Change the value to the actual visiting text file with the new point value.
        :param point: New poit value.
        :return:
        """
        file_path = self._folder_path.visiting
        with open(file_path, "w+") as f:
            f.write(f'{point}')


if __name__ == '__main__':
    score = FileWriter('/home/xabier/Scoreboard')
    score.set_local_value(1)
    score.change_set(2)
    score.set_local_value(8)
    score.set_visiting_value(9)
    print('aaaa')
