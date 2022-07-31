from pathlib import Path
import pytest
from app.parser.file_grabber import ParseFile


class TestFileGrabber:
    @pytest.mark.parametrize('building_list', ["common_house", "elite_house", "decor", "sanctuary",
                                               "food", "raw", "workshop", "service", "storage",
                                               "culture", "gov"])
    def test_parse_buildings(self, building_list):
        path = Path.cwd() / f'Zeus_Model_Normal.txt'
        blist = getattr(ParseFile, building_list)
        result = ParseFile.parse_models('Zeus_Model_Normal.txt', blist, path)
        print(result)
        assert result, "Nothing was returned by the file grabber"
        assert len(result) == len(blist), f"Should be {len(blist)} buildings, but {len(result)} is returned"

        for b in blist:
            assert any(b in string for string in result), f"Building {b} should exist in result list"

    def test_grabbing_one_line(self):
        text = ParseFile.get_line_from_file('Zeus_Model_Normal.txt', '24,BUILD_SHORT_OBELISK')
        result = '24,BUILD_SHORT_OBELISK ,{,18,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
        assert text in result, f"Grabbed line does not contain searched text"
        assert text == result, f"Grabbed line is not correct"
