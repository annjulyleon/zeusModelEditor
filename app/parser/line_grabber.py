"""
Provide classes and methods to operate building lines from the model files.

The module contains following methods:
- `ParseLine.model_parser(regular_expression, building_string)` - Returns a dictionary of parsed values from the line
"""
import re

class ParseLine:
    """Building lines parsing operations"""
    @staticmethod
    def model_parser(regular_expression: re.Pattern, building_string: str) -> dict:
        """With given pattern parse given string with building model and returns a dictionary

        Args:
            regular_expression: regular expression pattern passes in the re.Pattern format
            building_string: string with building model line from the model file

        Returns:
            dictionary with contains `bid` as building id from the file, `building_name` as building name,
            and `values` as list of parse values from the string
        """
        building_model = regular_expression.search(building_string)
        bid = building_model.group(1)
        name = building_model.group(2)
        values = list(filter(None,building_model.group(3).split(',')))

        return {"bid": bid, "building_name": name, "values": values}
