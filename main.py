from tinydb import TinyDB
from builder.file_builder import BuildFile
from data.db import DB



if __name__ == '__main__':
    line_to_replace = '31,BUILD_WHEAT_FARM,{,20,-3,1,1,3,10,5,0,0,0,},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
    replace = 'Hello!'
    BuildFile.copy_model_file(0)
    BuildFile.replace_line_in_file("Zeus_Model_VeryEasy.txt",line_to_replace,replace)

    #db = TinyDB('data/db.json')
    #print(DB.get_building_by_name(db, 'BUILD_BIBLIOTHEKE'))
    #DB.create_user_profile("user.json")

