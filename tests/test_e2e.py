from app.builder.file_builder import BuildFile
from app.builder.line_builder import BuildLine
from app.parser.file_grabber import ParseFile
from app.data.db import DB
from tinydb import TinyDB, Query


class TestWorkflow:

    def test_change_single_building_cost_very_easy(self):
        BuildFile.copy_model_file(0)
        DB.create_user_profile('user.json')

        db = TinyDB('app/data/user.json')

        DB.change_building_value_by_name(db,'BUILD_GRANARY','CST', 0, 15)

        old_line = ParseFile.get_line_from_file("output/Zeus_Model_VeryEasy.txt","BUILD_GRANARY")
        building_dictionary = DB.get_building_by_name(db, 'BUILD_GRANARY')
        line_to_replace = DB.get_search_line(db,'BUILD_GRANARY')
        replace = BuildLine.build_line(building_dictionary,0)

        BuildFile.replace_line_in_file(0, line_to_replace,replace)
        new_line = ParseFile.get_line_from_file("output/Zeus_Model_VeryEasy.txt","BUILD_GRANARY")
        #check file
        assert new_line == replace, f"New line {new_line} is not equal to built line {replace}"

    def test_building_category(self):
        pass

    def test_action_increase_common_house_capacity(self):
        BuildFile.copy_model_file(0)
        DB.create_user_profile('user.json')
        db = TinyDB('app/data/user.json')
        buildings = db.table('buildings')
        entries = buildings.search(Query().subtype == "common_house")
        for entry in entries:
            entry["default_values"][17]["values"][0] = str(round(int(entry["default_values"][17]["values"][0]) * 3.5))
            print(entry["default_values"][17]["values"])

    def test_action_increase_elite_house_capacity(self):
        pass

    def test_action_reduce_workers(self):
        pass

    def test_action_parse_from_config(self):
        pass