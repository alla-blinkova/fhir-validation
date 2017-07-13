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

#"java.exe" "-jar org.hl7.fhir.validator.jar " + res_path + " -defn " + def_path;
validatorPath = script_dir + '\\FhirValidator\\org.hl7.fhir.validator.jar'
definitionsPath = script_dir + '\\FhirValidator\\definitions.json.zip'
    
files = os.listdir(script_dir + '\\resourses') 
json_files = filter(lambda x: x.endswith('.json'), files)
for f in json_files:
    resPath = script_dir + '\\resourses\\' + f
    cmd = 'java.exe -jar ' + validatorPath + ' ' + resPath + ' -defn ' + definitionsPath
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd)
    p.wait()

