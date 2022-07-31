import json
from tinydb import TinyDB, Query, where
from pathlib import Path
from shutil import copy

class InitDB:
    """
    This class read json files from subdirectories /default/buildings, default/houses
    and creates db.json from them.
    """
    @staticmethod
    def load_from_json(json_file):
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {json_file} not found")

    @staticmethod
    def init(db: TinyDB):
        db.drop_tables()
        buildings = db.table('buildings')

        for path in Path('default', 'buildings').rglob('*.json'):
            building = InitDB.load_from_json(path)
            buildings.insert(building)

        for path in Path('default', 'houses').rglob('*.json'):
            building = InitDB.load_from_json(path)
            buildings.insert(building)


class DB:
    @staticmethod
    def create_user_profile(name):
        src = Path('app', 'data', "db.json")
        dst = Path('app', 'data', name)
        copy(src, dst)

    @staticmethod
    def get_building_by_name(db: TinyDB, name: str) -> dict:
        buildings = db.table('buildings')
        entry = buildings.get(Query().building_name == name)
        if entry:
            return dict(entry)
        else:
            raise ValueError(f"Building {name} not found in database. "
                             f"Check building name, it should be passed exactly as in model file, for ex. BUILD_BIBLIOTHEKE")

    @staticmethod
    def get_building_by_subtype(subtype: str) -> list[dict]:
        buildings = db.table('buildings')
        entries = buildings.search(Query().subtype == subtype)
        if len(entries) != 0:
            return entries
        else:
            raise ValueError(f"Subtype {subtype} not found in database. Available subtypes: elite_house, common_house,"
                             f"food, raw, workshop, service, storage, culture, gov, sanctuary, decor")

    @staticmethod
    def change_value_return_dictionary(entry: dict, name: str, difficulty: int, value) -> dict:
        default_values = entry['default_values']
        for i, dic in enumerate(default_values):
            if dic["name"] == name:
                entry["default_values"][i]["values"][difficulty] = str(value)
                return entry
            else:
                raise ValueError(f"Value {name} does not exist in entry. Value should be passed exactly as in model file")

    @staticmethod
    def get_search_line(db: TinyDB, name: str) -> str:
        buildings = db.table('buildings')
        entry = buildings.get(Query().building_name == name)
        if entry:
            if entry["type"] == "building":
                return f'{entry["bid"]},{entry["building_name"]}'
            elif entry["type"] == "house":
                return f'{entry["bid"]}: {entry["building_name"]}'
        else:
            raise ValueError(f"Building {name} not found in database. "
                             f"Check building name, it should be passed exactly as in model file, for ex. BUILD_BIBLIOTHEKE")

    @staticmethod
    def change_building_value_by_name(db, building_name, value_name, difficulty, value):
        """
        Change named value of certain difficulty and write back to database
        :param db:
        :param building_name:
        :param value_name:
        :param difficulty:
        :param value:
        :return:
        """
        buildings = db.table('buildings')
        entry_from_db = DB.get_building_by_name(db, building_name)
        entry_value_changed = DB.change_value_return_dictionary(entry_from_db, value_name, difficulty, value)

        buildings.update({"default_values": entry_value_changed["default_values"]},
                         where("building_name") == building_name)


if __name__ == '__main__':
    db = TinyDB("db.json")
    print(DB.get_building_by_subtype("food"))
