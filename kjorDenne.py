import subprocess

filer_i_rekkefolge = [
    "setUp.py",
    "dataSetUp.py",
    "setupStykke1.py",
    "setupStykke2.py",
]

for fil in filer_i_rekkefolge:
    process = subprocess.Popen(["python3", fil], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return_code = process.wait()
    
    if return_code == 0:
        print(f"Fil {fil} ble kjørt uten feil.")
    else:
        print(f"Noe gikk galt under kjøring av {fil}. Return code: {return_code}")