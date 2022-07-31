import pytest
from app.builder.line_builder import BuildLine


class TestLineBuilder:
    building = {
        "data": {"bid": "202", "building_name": "BUILD_BIBLIOTHEKE", "default_values": [{"name": "CST", "values": ["18", "27", "35", "45", "50"], "description": "Cost of structure or of one tile of a structure (for walls etc)"}, {"name": "DES", "values": ["3", "3", "3", "3", "3"], "description": "Initial desirability value"}, {"name": "STP", "values": ["1", "1", "1", "1", "1"], "description": "desirability step (in tiles)"}, {"name": "SZE", "values": ["-1", "-1", "-1", "-1", "-1"], "description": "desirability step size"}, {"name": "RGE", "values": ["3", "3", "3", "3", "3"], "description": "max desirability range"}, {"name": "EMP", "values": ["5", "5", "5", "5", "5"], "description": "Number of people a building employs"}, {"name": "FRI", "values": ["5", "10", "15", "18", "25"], "description": "Fire Risk Increment"}, {"name": "DRI", "values": ["0", "0", "0", "0", "0"], "description": "Damage Risk Increment"}, {"name": "RES", "values": ["0", "0", "0", "0", "0"], "description": "Resource Used"}, {"name": "RRD", "values": ["0", "0", "0", "0", "0"], "description": "Risk Reducer"}], "type": "building", "subtype": "culture"},
        "expected": [
            '202,BUILD_BIBLIOTHEKE,{,18,3,1,-1,3,5,5,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',
            '202,BUILD_BIBLIOTHEKE,{,27,3,1,-1,3,5,10,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',
            '202,BUILD_BIBLIOTHEKE,{,35,3,1,-1,3,5,15,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',
            '202,BUILD_BIBLIOTHEKE,{,45,3,1,-1,3,5,18,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',
            '202,BUILD_BIBLIOTHEKE,{,50,3,1,-1,3,5,25,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
        ]
    }
    common_house = {
        "data": {"bid": "6", "building_name": "Apartment", "default_values": [{"name": "EVO_DES_LOW", "values": ["15", "15", "15", "15", "25"], "description": "DES level at which the house will devolve"}, {"name": "EVO_DES_HIG", "values": ["30", "30", "30", "40", "40"], "description": "DES level at which the house will evolve"}, {"name": "EVO_CULTURE", "values": ["35", "35", "35", "35", "35"], "description": "Culture or science needed to evolve"}, {"name": "EVO_H2O", "values": ["1", "1", "1", "1", "1"], "description": "Water needed to evolve"}, {"name": "EVO_EDU", "values": ["0", "0", "0", "0", "0"], "description": "Stadium or Museum needed to evolve"}, {"name": "EVO_PER_SOLDIERS", "values": ["25", "25", "25", "25", "20"], "description": "Percentage of population made soldiers"}, {"name": "EVO_MAX_HORSES", "values": ["0", "0", "0", "0", "0"], "description": "Maximum horse storage"}, {"name": "EVO_HORSES", "values": ["0", "0", "0", "0", "0"], "description": "Horses needed to evolve"}, {"name": "EVO_FOOD_TYPES", "values": ["1", "1", "1", "1", "1"], "description": "Food needed to evolve"}, {"name": "EVO_FLEECE", "values": ["1", "1", "1", "1", "1"], "description": "Fleece needed to evolve"}, {"name": "EVO_OLIVE_OIL", "values": ["1", "1", "1", "1", "1"], "description": "Olive Oil needed to evolve"}, {"name": "EVO_WINE", "values": ["0", "0", "0", "0", "0"], "description": "Wine needed to evolve"}, {"name": "EVO_ARMS", "values": ["0", "0", "0", "0", "0"], "description": "Armor required to evolve"}, {"name": "EVO_MAX_ARMOR", "values": ["0", "0", "0", "0", "0"], "description": "Maximum armor storage"}, {"name": "EVO_CRIME_INC", "values": ["0", "0", "5", "10", "10"], "description": "Crime Risk Increment"}, {"name": "EVO_CRIME_BASE", "values": ["0", "0", "0", "0", "0"], "description": "Crime Risk Base"}, {"name": "UNUSED1", "values": ["30", "30", "30", "30", "30"], "description": "UNUSED1"}, {"name": "EVO_CAPACITY", "values": ["48", "48", "48", "48", "48"], "description": "Population capacity"}, {"name": "EVO_TAX_RATE", "values": ["2", "2", "2", "2", "2"], "description": "tax rate multiplier"}, {"name": "UNUSED2", "values": ["0", "0", "0", "0", "0"], "description": "UNUSED2"}, {"name": "EVO_DISEASE_INC", "values": ["5", "5", "5", "15", "15"], "description": "Disease Risk Increment"}, {"name": "Unknown 1", "values": ["48", "48", "48", "48", "48"], "description": "Unknown 1"}, {"name": "Unknown 2", "values": ["4", "4", "4", "4", "4"], "description": "Unknown 2"}, {"name": "Unknown 3", "values": ["7.5", "7.5", "7.5", "7.5", "7.5"], "description": "Unknown 3"}], "type": "house", "subtype": "common_house"},
        "expected": [
            "6: Apartment,{,15,30,35,1,0,25,0,0,1,1,1,0,0,0,0,0,30,48,2,0,5,,48,4,7.5,,,,,,",
            "6: Apartment,{,15,30,35,1,0,25,0,0,1,1,1,0,0,0,0,0,30,48,2,0,5,,48,4,7.5,,,,,,",
            "6: Apartment,{,15,30,35,1,0,25,0,0,1,1,1,0,0,0,5,0,30,48,2,0,5,,48,4,7.5,,,,,,",
            "6: Apartment,{,15,40,35,1,0,25,0,0,1,1,1,0,0,0,10,0,30,48,2,0,15,,48,4,7.5,,,,,,",
            "6: Apartment,{,25,40,35,1,0,20,0,0,1,1,1,0,0,0,10,0,30,48,2,0,15,,48,4,7.5,,,,,,"
        ]
    }

    elite_house = {
        "data": {"bid": "2", "building_name": "Mansion", "default_values": [{"name": "EVO_DES_LOW", "values": ["46", "52", "56", "56", "60"], "description": "DES level at which the house will devolve"}, {"name": "EVO_DES_HIG", "values": ["60", "66", "70", "70", "75"], "description": "DES level at which the house will evolve"}, {"name": "EVO_CULTURE", "values": ["50", "60", "60", "60", "60"], "description": "Culture or science needed to evolve"}, {"name": "EVO_H2O", "values": ["0", "0", "0", "0", "0"], "description": "Water needed to evolve"}, {"name": "EVO_EDU", "values": ["0", "0", "0", "0", "0"], "description": "Stadium or Museum needed to evolve"}, {"name": "EVO_PER_SOLDIERS", "values": ["20", "20", "20", "20", "20"], "description": "Percentage of population made soldiers"}, {"name": "EVO_MAX_HORSES", "values": ["2", "2", "2", "2", "2"], "description": "Maximum horse storage"}, {"name": "EVO_HORSES", "values": ["0", "0", "0", "0", "0"], "description": "Horses needed to evolve"}, {"name": "EVO_FOOD_TYPES", "values": ["1", "1", "1", "1", "1"], "description": "Food needed to evolve"}, {"name": "EVO_FLEECE", "values": ["1", "1", "1", "1", "1"], "description": "Fleece needed to evolve"}, {"name": "EVO_OLIVE_OIL", "values": ["1", "1", "1", "1", "1"], "description": "Olive Oil needed to evolve"}, {"name": "EVO_WINE", "values": ["0", "0", "0", "0", "0"], "description": "Wine needed to evolve"}, {"name": "EVO_ARMS", "values": ["1", "1", "1", "1", "1"], "description": "Armor required to evolve"}, {"name": "EVO_MAX_ARMOR", "values": ["2", "2", "2", "2", "2"], "description": "Maximum armor storage"}, {"name": "EVO_CRIME_INC", "values": ["-20", "-20", "-20", "-20", "-20"], "description": "Crime Risk Increment"}, {"name": "EVO_CRIME_BASE", "values": ["0", "0", "0", "0", "0"], "description": "Crime Risk Base"}, {"name": "UNUSED1", "values": ["100", "100", "100", "100", "100"], "description": "UNUSED1"}, {"name": "EVO_CAPACITY", "values": ["10", "10", "10", "10", "10"], "description": "Population capacity"}, {"name": "EVO_TAX_RATE", "values": ["22", "18", "16", "14", "12"], "description": "tax rate multiplier"}, {"name": "UNUSED2", "values": ["0", "0", "0", "0", "0"], "description": "UNUSED2"}, {"name": "EVO_DISEASE_INC", "values": ["0", "0", "0", "5", "10"], "description": "Disease Risk Increment"}, {"name": "Unknown 1", "values": ["110", "90", "80", "70", "60"], "description": "Unknown 1"}, {"name": "Unknown 2", "values": ["16", "16", "16", "16", "16"], "description": "Unknown 2"}, {"name": "Unknown 3", "values": ["6.25", "6.25", "6.25", "6.25", "6.25"], "description": "Unknown 3"}], "type": "house", "subtype": "elite_house"},
        "expected": [
            'Elite 2: Mansion,{,46,60,50,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,22,0,0,,110,16,6.25,,,,,,',
            'Elite 2: Mansion,{,52,66,60,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,18,0,0,,90,16,6.25,,,,,,',
            'Elite 2: Mansion,{,56,70,60,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,16,0,0,,80,16,6.25,,,,,,',
            'Elite 2: Mansion,{,56,70,60,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,14,0,5,,70,16,6.25,,,,,,',
            'Elite 2: Mansion,{,60,75,60,0,0,20,2,0,1,1,1,0,1,2,-20,0,100,10,12,0,10,,60,16,6.25,,,,,,'
        ]
    }
    sanctuary = {
        "data": {"bid": "98", "building_name": "BUILD_LARGE_SANC_POSEIDON2", "default_values": [{"name": "CST", "values": ["2080", "2080", "2080", "2080", "2080"], "description": "Cost of structure or of one tile of a structure (for walls etc)"}, {"name": "DES", "values": ["20", "20", "20", "20", "20"], "description": "Initial desirability value"}, {"name": "STP", "values": ["1", "1", "1", "1", "1"], "description": "desirability step (in tiles)"}, {"name": "SZE", "values": ["-2", "-2", "-2", "-2", "-2"], "description": "desirability step size"}, {"name": "RGE", "values": ["6", "6", "6", "6", "6"], "description": "max desirability range"}, {"name": "EMP", "values": ["80", "80", "80", "80", "80"], "description": "Number of people a building employs"}, {"name": "FRI", "values": ["0", "0", "0", "0", "0"], "description": "Fire Risk Increment"}, {"name": "DRI", "values": ["0", "0", "0", "0", "0"], "description": "Damage Risk Increment"}, {"name": "RES", "values": ["0", "0", "0", "0", "0"], "description": "Resource Used"}, {"name": "RRD", "values": ["0", "0", "0", "0", "0"], "description": "Risk Reducer"}], "type": "building", "subtype": "sanctuary"},
        "expected": [
            "98,BUILD_LARGE_SANC_POSEIDON2,{,2080,20,1,-2,6,80,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "98,BUILD_LARGE_SANC_POSEIDON2,{,2080,20,1,-2,6,80,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "98,BUILD_LARGE_SANC_POSEIDON2,{,2080,20,1,-2,6,80,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "98,BUILD_LARGE_SANC_POSEIDON2,{,2080,20,1,-2,6,80,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "98,BUILD_LARGE_SANC_POSEIDON2,{,2080,20,1,-2,6,80,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
        ]
    }
    bad_building = {
        "data": {"bid": "24", "building_name": "BUILD_SHORT_OBELISK", "default_values": [{"name": "CST", "values": ["10", "15", "18", "22", "27"], "description": "Cost of structure or of one tile of a structure (for walls etc)"}, {"name": "DES", "values": ["6", "6", "6", "6", "6"], "description": "Initial desirability value"}, {"name": "STP", "values": ["1", "1", "1", "1", "1"], "description": "desirability step (in tiles)"}, {"name": "SZE", "values": ["-1", "-1", "-1", "-1", "-1"], "description": "desirability step size"}, {"name": "RGE", "values": ["2", "2", "2", "2", "2"], "description": "max desirability range"}, {"name": "EMP", "values": ["0", "0", "0", "0", "0"], "description": "Number of people a building employs"}, {"name": "FRI", "values": ["0", "0", "0", "0", "0"], "description": "Fire Risk Increment"}, {"name": "DRI", "values": ["0", "0", "0", "0", "0"], "description": "Damage Risk Increment"}, {"name": "RES", "values": ["0", "0", "0", "0", "0"], "description": "Resource Used"}, {"name": "RRD", "values": ["0", "0", "0", "0", "0"], "description": "Risk Reducer"}], "type": "building", "subtype": "decor"},
        "expected": [
            "24,BUILD_SHORT_OBELISK ,{,10,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "24,BUILD_SHORT_OBELISK ,{,15,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "24,BUILD_SHORT_OBELISK ,{,18,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "24,BUILD_SHORT_OBELISK ,{,22,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
            "24,BUILD_SHORT_OBELISK ,{,27,6,1,-1,2,0,0,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
        ]
    }

    @pytest.mark.parametrize('building', ["building","common_house","elite_house","sanctuary","bad_building"])
    def test_build_common_house_line_each_difficulty(self, building):

        for i in [0, 1, 2, 3, 4]:
            line = BuildLine.build_line((getattr(self, building))["data"], i)
            assert line == getattr(self, building)["expected"][i], f"Building line {line} should match expected result"
