import pytest
from pathlib import Path
from app.builder.file_builder import BuildFile


class TestFileBuilder:
    model_files = {
        0: "Zeus_Model_VeryEasy.txt",
        1: "Zeus_Model_Easy.txt",
        2: "Zeus_Model_Normal.txt",
        3: "Zeus_Model_Hard.txt",
        4: "Zeus_Model_Impossible.txt"
    }

    @pytest.mark.parametrize('difficulty', [0, 1, 2, 3, 4])
    def test_model_file_copy_output(self, difficulty):
        BuildFile.copy_model_file(difficulty)
        output = Path('output', self.model_files[difficulty])

        assert output.exists(), f"File {output} was not created in expected path"
        assert output.stat().st_size > 0, f"File {output} exist, but is empty"

        output.unlink()

    @pytest.mark.parametrize('difficulty', [0, 1, 2, 3, 4])
    def test_line_replace_in_output_file(self, difficulty):
        line_to_replace = '31,BUILD_WHEAT_FARM'
        replace = 'This is test line that replaced previous text'

        BuildFile.copy_model_file(difficulty)
        output = Path('output', self.model_files[difficulty])

        BuildFile.replace_line_in_file(difficulty, line_to_replace, replace)
        with open(output, 'r', encoding="utf_8_sig") as file:
            line = file.readlines()[98:99][0]

        assert line == replace + "\n"
        output.unlink()

