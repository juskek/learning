from pathlib import Path
import pandas as pd
import os
def lib_function():
    pathOfFile = Path(__file__).resolve()
    pathOfData = os.path.join(pathOfFile.parent,'data')
    print('Hello from lib')
    print(f'This file exists in {pathOfFile}')
    df = pd.read_csv(os.path.join(pathOfData,'example.csv'))
    print(df)
    
    
if __name__ == "__main__":
    lib_function()