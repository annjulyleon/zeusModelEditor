import pytest
from app.parser.line_grabber import ParseLine
from app.pattern import CHOUSE_REGEXP, EHOUSE_REGEXP, BUILDING_REGEXP
from assertions import Assertions


class TestLineGrabber():
    common_house = '4: Homestead,{,-2,10,15,1,0,20,0,0,1,1,0,0,0,0,10,0,20,32,2,0,10,,32,4,5,,,,,,'
    elite_house = 'Elite 2: Mansion,{,56,70,60,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,16,0,0,,80,16,6.25,,,,,,'
    building = '202,BUILD_BIBLIOTHEKE,{,35,3,1,-1,3,5,15,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
    building_with_space = '19,BUILD_TALL_OBELISK ,{,24,8,1,0,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'

    def test_grabber_common_house_string(self):
        result = ParseLine.model_parser(CHOUSE_REGEXP, self.common_house)
        expected_list = ['-2', '10', '15', '1', '0', '20', '0', '0', '1', '1', '0', '0', '0',
                         '0', '10', '0', '20', '32', '2', '0', '10', '32', '4', '5']

        assert result, "Result is empty"
        Assertions.assert_keys_exists(['bid','building_name','values'], result)

        assert len(result["values"]) == 24, f"Should be a list with exactly 24 values and not {len(result['values'])}"
        Assertions.assert_key_value(result,"bid","4")
        Assertions.assert_key_value(result,"building_name", "Homestead")
        Assertions.assert_key_value(result,"values", expected_list)

    def test_grabber_elite_house_string(self):
        result = ParseLine.model_parser(EHOUSE_REGEXP, self.elite_house)
        expected_list = ['56', '70', '60', '0', '0', '20', '2', '0', '1', '1', '1', '0', '1', '2', '-20',
                         '0', '100', '10', '16', '0', '0', '80', '16', '6.25']

        assert result, "Result is empty"
        Assertions.assert_keys_exists(['bid', 'building_name', 'values'], result)

        assert len(result["values"]) == 24, f"Should be a list with exactly 24 values and not {len(result['values'])}"
        Assertions.assert_key_value(result, "bid", "2")
        Assertions.assert_key_value(result, "building_name", "Mansion")
        Assertions.assert_key_value(result, "values", expected_list)

    def test_grabber_building(self):
        result = ParseLine.model_parser(BUILDING_REGEXP, self.building)
        expected_list = ['35', '3', '1', '-1', '3', '5', '15', '0', '0', '0']

        assert result, "Result is empty"
        Assertions.assert_keys_exists(['bid', 'building_name', 'values'], result)

        assert len(result["values"]) == 10, f"Should be a list with exactly 10 values and not {len(result['values'])}"
        Assertions.assert_key_value(result, "bid", "202")
        Assertions.assert_key_value(result, "building_name", "BUILD_BIBLIOTHEKE")
        Assertions.assert_key_value(result, "values", expected_list)

    def test_grabber_building_with_space(self):
        result = ParseLine.model_parser(BUILDING_REGEXP, self.building_with_space)
        expected_list = ['24', '8', '1', '0', '2', '0', '0', '0', '0', '0']

        assert result, "Result is empty"
        Assertions.assert_keys_exists(['bid', 'building_name', 'values'], result)

        assert len(result["values"]) == 10, f"Should be a list with exactly 10 values and not {len(result['values'])}"
        Assertions.assert_key_value(result, "bid", "19")
        Assertions.assert_key_value(result, "building_name", "BUILD_TALL_OBELISK")
        Assertions.assert_key_value(result, "values", expected_list)
