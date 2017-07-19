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

validatorPath = script_dir + '\\FhirValidator\\org.hl7.fhir.validator.jar'
definitionsPath = script_dir + '\\FhirValidator\\definitions.json.zip'
    
files = os.listdir(script_dir + '\\resources') 
json_files = list(filter(lambda x: x.endswith('.json'), files))
count_valid = 0
for f in json_files:
    resPath = script_dir + '\\resources\\' + f
    cmd = 'java.exe -jar ' + validatorPath + ' ' + resPath + ' -defn ' + definitionsPath
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = ' '
    while out:
        out = p.stdout.readline()
        print(out.rstrip().decode('ascii'))
        if (out.decode()).find("error:0") != -1:
            count_valid = count_valid + 1
    p.wait()

print ("Valid / All: ", count_valid, "/", len(json_files))


