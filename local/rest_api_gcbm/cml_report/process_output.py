import os
import zipfile

output_zip = os.path.join('..','..','..','output.zip')
with zipfile.ZipFile(output_zip,'r') as zip_ref:
    zip_ref.extractall(os.path.join('..','..','..','output'))

output = os.path.join('..','..','..','output')
print("Output Measurements are:")
measurements = os.listdir(output)
print(measurements)
