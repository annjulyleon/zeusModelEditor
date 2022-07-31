from pathlib import Path
from shutil import copy


class BuildFile:
    """Class is used to build model file from the json.
    """

    @staticmethod
    def copy_model_file(difficulty):
        """Copy original model files of specified difficulty

                Args:
                    difficulty (int): 0 to 4 with 0 being Easy, 4 - Impossible
                Returns:
                    None
                Raises:
                    ValueError: if difficulty value is not integer or in the model_files
        """
        Path("output").mkdir(parents=True, exist_ok=True)
        model_files = {
            0: "Zeus_Model_VeryEasy.txt",
            1: "Zeus_Model_Easy.txt",
            2: "Zeus_Model_Normal.txt",
            3: "Zeus_Model_Hard.txt",
            4: "Zeus_Model_Impossible.txt"
        }
        if difficulty in model_files.keys():
            src = Path('app', 'data', 'default', 'models', model_files[difficulty])
            dst = Path('output', model_files[difficulty])
            copy(src, dst)
        else:
            raise ValueError("Difficulty should be passed as integer from 0 to 4 included")

    @staticmethod
    def replace_line_in_file(difficulty: int, line_to_replace, line):
        """Replace line in the mode file

            Args:
                difficulty (int): 0 to 4 with 0 being Easy, 4 - Impossible
                line_to_replace (str): string by wich line inf file is found
                line (str): text to replace line with
            Returns:
                None
            Raises:
                ValueError: if line is not found in mode file
                FileNotFoundError: if model file is not found
        """
        model_files = {
            0: "Zeus_Model_VeryEasy.txt",
            1: "Zeus_Model_Easy.txt",
            2: "Zeus_Model_Normal.txt",
            3: "Zeus_Model_Hard.txt",
            4: "Zeus_Model_Impossible.txt"
        }
        path = Path('output', model_files.get(difficulty))
        try:
            with open(path, 'r') as file:
                file_data = file.readlines()
        except FileNotFoundError:
            print(f'File "{path}" not found')

        flag = 0
        for number, line_text in enumerate(file_data):
            if line_to_replace in line_text:
                file_data[number] = line + '\n'
                flag = 1
                break

        if flag == 0:
            raise ValueError(f"Line {line_to_replace} not found in file")

        with open(path, 'w') as file:
            file.writelines(file_data)
