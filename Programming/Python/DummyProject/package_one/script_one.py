from module_one import ModuleOne

'''
    Trying to import sibling package. 
    Methods:
    1. setup.py and pip install -e .
        - Add setup.py in root directory of project 
        - pip install -e . from root directory of project 
    2. sys.path.insert
        - .. 
        - ../
'''

# ! ModuleNotFoundError: No module named 'lib'
# from lib.package_common.module_common i\mport ModuleCommon
# ! ImportError: attempted relative import with no known parent package
# from ..lib.package_common.module_common import ModuleCommon

import sys, os
# relative to directory you are executing script_one from
# sys.path.insert(0, os.path.abspath('.')) 

# relative to directory containing script_one. 
sys.path.insert(0, os.path.abspath('./')) 
# from lib.package_common.module_common import ModuleCommon
# ModuleCommon.sayHi()
from package_one.nested.module_nested import ModuleNested

ModuleOne.sayHi()
ModuleNested.getCommonModuleToSayHi()