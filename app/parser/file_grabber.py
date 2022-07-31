import itertools
from pathlib import Path

#https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
class ParseFile:
    """Class is used to parse model file.

    Attributes:
        common_house: a tuple of common houses names as in model file
        elite_house: a tuple of elite houses names as in model file
        decor: a tuple of decoration buildings names as in model file
        sanctuary: a tuple of sanctuary building names as in model file
        food: a tuple of food building names as in model file
        raw: a tuple of raw building names as in model file
    """
    common_house = ('Hut', 'Shack', 'Hovel', 'Homestead', 'Tenement', 'Apartment', 'Townhouse')
    elite_house = ('Devolved', 'Residence', 'Mansion', 'Manor', 'Estate')
    decor = ('BUILD_FLOWER_GARDEN','BUILD_GAZEBO','BUILD_HEDGE_MAZE','BUILD_FISH_POND','BUILD_TALL_OBELISK',
             'BUILD_SUNDIAL','BUILD_TOPIARY','BUILD_SPRING','BUILD_STONE_CIRCLE','BUILD_SHORT_OBELISK',
             'BUILD_WATER_PARK','BUILD_BOULEVARD','BUILD_BENCH','BUILD_GARDENS','BUILD_DORIC_COLUMN',
             'BUILD_IONIC_COLUMN','BUILD_CORINTHIAN_COLUMN','BUILD_DOLPHIN_SCULPTURE','BUILD_ORRERY',
             'BUILD_SHELL_GARDEN','BUILD_BATHS','BUILD_BIRD_BATH')
    sanctuary = ('BUILD_LARGE_SANC_ZEUS', 'BUILD_LARGE_SANC_POSEIDON', 'BUILD_LARGE_SANC_DEMETER',
                 'BUILD_LARGE_SANC_APOLLO', 'BUILD_LARGE_SANC_ARTEMIS', 'BUILD_LARGE_SANC_ARES',
                 'BUILD_LARGE_SANC_APHRODITE', 'BUILD_LARGE_SANC_HERMES', 'BUILD_LARGE_SANC_ATHENA',
                 'BUILD_LARGE_SANC_HEPHAISTOS', 'BUILD_LARGE_SANC_DIONYSUS', 'BUILD_LARGE_SANC_HADES',
                 'BUILD_LARGE_SANC_HERA', 'BUILD_LARGE_SANC_ATLAS', 'BUILD_LARGE_SANC_POSEIDON2')
    food = ('BUILD_WHEAT_FARM', 'BUILD_ONION_FARM', 'BUILD_CARROT_FARM', 'BUILD_GROWERS_LODGE',
            'BUILD_SHEEP_FARM', 'BUILD_GOAT_FARM', 'BUILD_FISHING_WHARF', 'BUILD_URCHIN_COLLECTOR',
            'BUILD_HUNTING_LODGE', 'BUILD_FRUIT_GROWERS_LODGE', 'BUILD_CORRAL_SLAUGHTER')
    raw = ('BUILD_MINT', 'BUILD_MARBLE_QUARRY', 'BUILD_FOUNDRY', 'BUILD_TIMBER_MILL',
           'BUILD_ORICHALC_REFINERY', 'BUILD_BLACK_MARBLE_SHOP')
    workshop = ('BUILD_WINERY', 'BUILD_OIL_PRESS', 'BUILD_SCULPTURE_STUDIO', 'BUILD_ARTISANS_GUILD',
                 'BUILD_CHARIOT_WORKSHOP', 'BUILD_ARMORY')
    service = ('BUILD_FOUNTAIN', 'BUILD_INFIRMARY', 'BUILD_TAX_OFFICE', 'BUILD_GUARDPOST')
    storage = ('BUILD_GRANARY', 'BUILD_STOREHOUSE,', 'BUILD_DOCK,', 'BUILD_TRADING_POST', 'BUILD_FOOD_VENDOR',
               'BUILD_FLEECE_VENDOR', 'BUILD_OIL_VENDOR', 'BUILD_WINE_VENDOR', 'BUILD_ARMS_VENDOR',
               'BUILD_HORSE_TRAINER', 'BUILD_CHARIOT_VENDOR')
    #: tuple of str: Doc comment *before* attribute, with type specified
    culture = ('BUILD_COLLEGE', 'BUILD_DRAMA_SCHOOL', 'BUILD_GYMNASIUM', 'BUILD_STADIUM', 'BUILD_PODIUM',
               'BUILD_THEATRE', 'BUILD_BIBLIOTHEKE', 'BUILD_OBSERVATORY', 'BUILD_UNIVERSITY',
               'BUILD_LABORATORY',
               'BUILD_INVENTORS_WORKSHOP', 'BUILD_MUSUEM')
    gov = ('BUILD_TOWER', 'BUILD_HORSE_RANCH', 'BUILD_WARSHIP_WHARF')

    buildings_all = itertools.chain(decor, sanctuary, food, raw, workshop, service, storage, culture, gov)

    @staticmethod
    def parse_models(file_name: str, building_names: tuple, path: Path = None) -> list:
        """Returns list of parsed lines from path/file_name that contains building_names passes as a tuple

        Args:
            file_name (str): name of the model file, if path is not specified - in the `data/default/models`
            building_names (tuple): name of the buildings to parse from the model file
            path (Path, optional): if specified, look for `file_name` in this directory

        Returns:
            list: list of the parsed lines from the model file with specified `building_names`
        """
        if not path:
            path = Path.cwd() / 'data' / 'default' / 'models' / f'{file_name}.txt'
        with open(path, 'r', encoding="utf_8_sig") as file:
            lines = file.readlines()
            lines_filtered_by_names = []
            for line in lines:
                for model_name in building_names:
                    if model_name in line:
                        lines_filtered_by_names.append(line)

        lines = [b.rstrip() for b in lines_filtered_by_names]
        lines = list(set(lines))
        return lines

    @staticmethod
    def get_line_from_file(file_path, line_to_search: str):
        """Returns line of text which contains line_to_search from the file file_path

        Args:
            file_path (str): path to file from current directory
            line_to_search (str): line or text to search in the model file
        Returns:
            str: single line which contains `line_to_search`
        Raises:
            ValueError: if `line_to_search` is no found in the model file
        """
        path = Path.cwd() / file_path
        with open(path, 'r') as file:
            file_lines = file.readlines()

        line = False
        flag = 0
        for number, line_text in enumerate(file_lines):
            if line_to_search in line_text:
                line = line_text
                flag = 1
                break

        if flag == 0:
            raise ValueError(f"Line {line_to_search} not found in file")

        return line.rstrip()
