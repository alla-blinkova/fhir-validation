import subprocess
import os
import sys
import inspect

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

script_dir = get_script_dir() 
cmd = script_dir + '\\bin\\ValidationTest.exe'

#если аргументов нет, по умолчанию Schema.json
if len(sys.argv) == 1:
    schemaPath = script_dir + '\\schemas' + '\\Schema.json'
else:
    print(sys.argv[0])
    schemaPath = script_dir + '\\schemas' + '\\' + sys.argv[1]


files = os.listdir(script_dir + '\\resources') 
json_files = filter(lambda x: x.endswith('.json'), files)
for f in json_files: 
    resoursePath = script_dir + '\\resources\\' + f
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd + ' ' + schemaPath + ' ' + resoursePath)
    p.wait()

