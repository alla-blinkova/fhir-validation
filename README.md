# Fhir-validation
This project is designed for the validation of FHIR resourses by using different methods, such as JSON schema and FHIR Validator.
## Validation by using JSON schema
### Getting started
1. Install Visual Studio.
2. Compile the library FhirJsonValidator and console application ValidationTest which uses this library. 
To compile the library you need to download packages Newtonsoft.Json and Newtonsoft.Json.Schema which can be installed 
by using NuGet:
```
Install-Package Newtonsoft.Json
Install-Package Newtonsoft.Json.Schema
```
3. Install Python.

### Running the tests
1. Put ValidationTest.exe and dll files to the folder "script".
2. Run the script start_validation.py without parameters to perform validation of all resourses located in the folder "resourses"
and default schema. 
To use your own schema, put it to the folder "script/schemas" and run the script with parameter - file name of the schema.

## Validation by using FHIR Validator
### Getting started
1. Install Java. 
2. Install Python.
3. Clone this repository. Definitions and jar-file with FHIR Validator are located in the folder "FhirValidator".
### Running the tests
To run the validation you need to run script start_validation.py without parameters. 
It will perform validation of all resourses located in the folder "resourses".