class BuildLine:

    @staticmethod
    def build_line(data: dict, difficulty: int):
        """Build line in Zues Model format from json data

            Args:
                data (dict): building data passed as dictionary
                difficulty (int): difficulty
            Returns:
                line (str): built line
            Raises:
                Exception: Difficulty should be int
                Exception: Building type should be one of 'house' of 'building'
        """
        bad_buildings = ['BUILD_TALL_OBELISK','BUILD_SHORT_OBELISK','BUILD_WATER_PARK','BUILD_DOLPHIN_SCULPTURE',
                         'BUILD_ORRERY','BUILD_SHELL_GARDEN','BUILD_BATHS','BUILD_BIRD_BATH']
        if difficulty in [0,1,2,3,4]:
            values = [x['values'][difficulty] for x in data['default_values']]
        else:
            raise Exception(f"Difficulty should be int as: "
                            f"0 (VeryEasy), 1 (Easy), 2 (Normal), 3 (Hard), 4 (Impossible)")

        if data["type"] == "house":
            values_string = f',{",".join(values[0:21])},,{",".join(values[21:24])},,,,,,'
            line = f"{data['bid']}: {data['building_name']},{{{values_string}"
            if data["subtype"] == "elite_house":
                line = f"Elite {line}"

        elif data["type"] == "building":
            values_string = f',{{,{",".join(values)}'

            if data["building_name"] in bad_buildings:
                line = f"{data['bid']},{data['building_name']} {values_string},}}{''.join([','] * 57)}"
            else:
                line = f"{data['bid']},{data['building_name']}{values_string},}}{''.join([','] * 57)}"
        else:
            raise Exception(f"Building type should be one of 'house' of 'building'")

        return line
