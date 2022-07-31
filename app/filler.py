from pattern import CHOUSE_REGEXP, EHOUSE_REGEXP, BUILDING_REGEXP
import json
import os

from pathlib import Path
from parser.file_grabber import ParseFile
from parser.line_grabber import ParseLine

MODEL_FILES = ('Zeus_Model_VeryEasy', 'Zeus_Model_Easy', 'Zeus_Model_Normal', 'Zeus_Model_Hard',
               'Zeus_Model_Impossible')

"""
This is executed once to read default model files and create separate json for each building
"""


class Filler:

    @staticmethod
    def get_models_list_from_each_difficulty(model_files: tuple, building_type: str) -> list:
        """
        Build list of dictionaries with building strings for each difficulty model
        :param model_files: list of file names for difficulty models
        :param building_type: building type, one from file_grabber
        :return: list of dictionaries with keys as file model name, and models as list of builsings strings.
        """
        models_each_difficulty = []
        for model_file in model_files:
            models = ParseFile.parse_models(model_file, getattr(ParseFile, building_type))
            models_difficulty_dictionary = {
                "difficulty": model_file,
                "models": models
            }
            models_each_difficulty.append(models_difficulty_dictionary)

        return models_each_difficulty

    @staticmethod
    def get_values_lists_by_building(models_each_difficulty: list[list], expression):
        """
        Builds list of dictionaries with difficulty values for each building
        :param models_each_difficulty: list of strings for each difficulty
        :param expression: regular expression to parse string
        :return:
        """
        buildings_values = []
        for models in models_each_difficulty:
            values_from_file = []
            for building_model in models:
                parsed_building_model = ParseLine.model_parser(expression, building_model)
                values = parsed_building_model["values"]
                values_from_file.append({"building_name": parsed_building_model["building_name"],
                                         "bid": parsed_building_model["bid"],
                                         "values": values})

            buildings_values.append(values_from_file)

        buildings_values = list(map(list, zip(*buildings_values)))

        return buildings_values

    @staticmethod
    def get_values_in_list(building_values: list[dict]):
        building_values = [x['values'] for x in building_values]
        dfvl = list(map(list, zip(*building_values)))

        if len(dfvl) == 10:
            values_dictionary = [
                {"name": "CST", "values": dfvl[0],
                 "description": "Cost of structure or of one tile of a structure (for walls etc)"},
                {"name": "DES", "values": dfvl[1], "description": "Initial desirability value"},
                {"name": "STP", "values": dfvl[2], "description": "desirability step (in tiles)"},
                {"name": "SZE", "values": dfvl[3], "description": "desirability step size"},
                {"name": "RGE", "values": dfvl[4], "description": "max desirability range"},
                {"name": "EMP", "values": dfvl[5],
                 "description": "Number of people a building employs"},
                {"name": "FRI", "values": dfvl[6], "description": "Fire Risk Increment"},
                {"name": "DRI", "values": dfvl[7], "description": "Damage Risk Increment"},
                {"name": "RES", "values": dfvl[8], "description": "Resource Used"},
                {"name": "RRD", "values": dfvl[9], "description": "Risk Reducer"}
            ]
            return values_dictionary
        elif len(dfvl) == 24:
            values_dictionary = [
                {"name": "EVO_DES_LOW", "values": dfvl[0],
                 "description": "DES level at which the house will devolve"},
                {"name": "EVO_DES_HIG", "values": dfvl[1],
                 "description": "DES level at which the house will evolve"},
                {"name": "EVO_CULTURE", "values": dfvl[2],
                 "description": "Culture or science needed to evolve"},
                {"name": "EVO_H2O", "values": dfvl[3], "description": "Water needed to evolve"},
                {"name": "EVO_EDU", "values": dfvl[4],
                 "description": "Stadium or Museum needed to evolve"},
                {"name": "EVO_PER_SOLDIERS", "values": dfvl[5],
                 "description": "Percentage of population made soldiers"},
                {"name": "EVO_MAX_HORSES", "values": dfvl[6], "description": "Maximum horse storage"},
                {"name": "EVO_HORSES", "values": dfvl[7], "description": "Horses needed to evolve"},
                {"name": "EVO_FOOD_TYPES", "values": dfvl[8], "description": "Food needed to evolve"},
                {"name": "EVO_FLEECE", "values": dfvl[9], "description": "Fleece needed to evolve"},
                {"name": "EVO_OLIVE_OIL", "values": dfvl[10], "description": "Olive Oil needed to evolve"},
                {"name": "EVO_WINE", "values": dfvl[11], "description": "Wine needed to evolve"},
                {"name": "EVO_ARMS", "values": dfvl[12], "description": "Armor required to evolve"},
                {"name": "EVO_MAX_ARMOR", "values": dfvl[13], "description": "Maximum armor storage"},
                {"name": "EVO_CRIME_INC", "values": dfvl[14], "description": "Crime Risk Increment"},
                {"name": "EVO_CRIME_BASE", "values": dfvl[15], "description": "Crime Risk Base"},
                {"name": "UNUSED1", "values": dfvl[16], "description": "UNUSED1"},
                {"name": "EVO_CAPACITY", "values": dfvl[17], "description": "Population capacity"},
                {"name": "EVO_TAX_RATE", "values": dfvl[18], "description": "tax rate multiplier"},
                {"name": "UNUSED2", "values": dfvl[19], "description": "UNUSED2"},
                {"name": "EVO_DISEASE_INC", "values": dfvl[20], "description": "Disease Risk Increment"},
                {"name": "Unknown 1", "values": dfvl[21], "description": "Unknown 1"},
                {"name": "Unknown 2", "values": dfvl[22], "description": "Unknown 2"},
                {"name": "Unknown 3", "values": dfvl[23], "description": "Unknown 3"}
            ]
            return values_dictionary

    @staticmethod
    def write_to_json(building_type, building_name, building_subtype, data):
        if building_type in ['elite_house', 'common_house', 'house']:
            path = f'data/default/houses/{building_subtype}/house_{building_name}.json'
        else:
            path = f'data/default/buildings/{building_subtype}/{building_name}.json'

        with open(os.path.join(os.path.dirname(__file__), path), 'w') as f:
            json.dump(data, f)

    @staticmethod
    def write_to_file(models_files: tuple, building_type, building_subtype, regexp):
        models_lists_dif = Filler.get_models_list_from_each_difficulty(models_files, building_subtype)
        models_lists_dif = [x['models'] for x in models_lists_dif]

        lists_of_values = Filler.get_values_lists_by_building(models_lists_dif, regexp)
        base_dictionary = {"type": building_type, "subtype": building_subtype}
        entries_list = []

        for list_of_values in lists_of_values:
            name = list_of_values[0]['building_name']
            bid = list_of_values[0]['bid']
            values = Filler.get_values_in_list(list_of_values)
            values_dictionary = {"bid": bid, "building_name": name, "default_values": values}
            entry = values_dictionary | base_dictionary
            entries_list.append(entry)

        for entry in entries_list:
            Filler.write_to_json(building_type, entry['building_name'], building_subtype, entry)

    @staticmethod
    def execute(model_files=MODEL_FILES):
        Path("data", "default", "houses", "common_house").mkdir(parents=True, exist_ok=True)
        Path("data", "default", "houses", "elite_house").mkdir(parents=True, exist_ok=True)
        for folder in ['food', 'raw', 'workshop', 'service', 'storage', 'culture', 'gov',
                       'sanctuary', 'decor']:
            Path("data", "default", "buildings", folder).mkdir(parents=True, exist_ok=True)

        Filler.write_to_file(model_files, 'house', 'elite_house', EHOUSE_REGEXP)
        Filler.write_to_file(model_files, 'house', 'common_house', CHOUSE_REGEXP)

        Filler.write_to_file(model_files, 'building', 'food', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'raw', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'workshop', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'service', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'storage', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'culture', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'gov', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'sanctuary', BUILDING_REGEXP)
        Filler.write_to_file(model_files, 'building', 'decor', BUILDING_REGEXP)


if __name__ == '__main__':
    Filler.execute()
