from pathlib import Path


def mkdir(path):
    if isinstance(path, str):
        path = Path(path)
    if not path.exists():
        path.mkdir(parents=True)


class Folders:
    """
    Select the folder and files to be used according to the current game set.
    """
    def __init__(self, root_path):
        self._first_set = Path(root_path / 'Set_1')
        self._second_set = Path(root_path / 'Set_2')
        self._third_set = Path(root_path / 'Set_3')
        self._local_name = 'Local_points.txt'
        self._visiting_name = 'Visiting_points.txt'
        self._local = self._first_set / self._local_name
        self._visiting = self._first_set / self._visiting_name

    @property
    def local(self):
        """
        Call this function to find out the path to the current local file.
        :return: Return the actual local file path.
        """
        return self._local

    @local.setter
    def local(self, value):
        if isinstance(value, int):
            if value == 1:
                self._local = self._first_set / self._local_name
            elif value == 2:
                self._local = self._second_set / self._local_name
            elif value == 3:
                self._local = self._third_set / self._local_name
            else:
                print('Set value higher than permitted')
        else:
            print('Set value incorrect it must be int (1, 2, 3)')

    @property
    def visiting(self):
        """
        Call this function to find out the path to the current visiting file.
        :return: Return the actual visiting file path.
        """
        return self._visiting

    @visiting.setter
    def visiting(self, value):
        if isinstance(value, int):
            if value == 1:
                self._visiting = self._first_set / self._visiting_name
            if value == 2:
                self._visiting = self._second_set / self._visiting_name
            if value == 3:
                self._visiting = self._third_set / self._visiting_name
            else:
                print('Set value higher than permitted')
        else:
            print('Set value incorrect it must be int (1, 2, 3)')

    @property
    def first_set(self):
        """
        Call this function to find out the path to the first set folder.
        :return: Return the first set folder path.
        """
        return self._first_set

    @property
    def second_set(self):
        """
        Call this function to find out the path to the second set folder.
        :return: Return the second set folder path.
        """
        return self._second_set

    @property
    def third_set(self):
        """
        Call this function to find out the path to the third set folder.
        :return: Return the third set folder path.
        """
        return self._third_set

    def check_folders(self):
        """
        This function checks if the required folder exists.
        If it does not exist, the folder is created.
        :return:
        """
        mkdir(self.first_set)
        mkdir(self.second_set)
        mkdir(self.third_set)
