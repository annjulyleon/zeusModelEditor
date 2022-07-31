# Zeus Model Editor

This is set of python files to work with Zeus Master of Olympus model files. **Work in Progress.**
Model files are stored inside `/Model` game directory:

- Zeus_Model_VeryEasy.txt
- Zeus_Model_Easy.txt
- Zeus_Model_Normal.txt
- Zeus_Model_Hard.txt
- Zeus_Model_Impossible.txt

Project files include:

- `/app/parser` - read and parse model files and lines
- `/app/builder` - build lines and files from .json building data
- `/filler.py` - one time to run script to parse model files to TinyDB db.json format
- `/data` - scripts to work with TinyDB. Contains `default` model files and json files separated by building
- `/gui.py` - **wip** simple ugly gui to edit building data
- `/tests` - tests with usage examples
