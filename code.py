import pandas as pd
import os
from pathlib import Path
import sys

def csv_combiner(argv):
    
    # Checking if atleast 1 file is provided in argument
    if not len(argv):
        return "No arguments provided"
    files = list(argv)
    
    # Checking if filepath provided actually exists in the system
    path_check = Path(files[i])
    if not path_check.exists():
        raise IOError('File or Path does not exist')
    
    # Checking if all the files provided in argument are csv files
    for i in range(len(files)):
        _, ext = os.path.splitext(files[i])
        if ext!= '.csv':
            raise Exception('Filename specified in argument is not a csv file')
                
    # Reading in chunks of 1M, Creating additional filename column and displaying csv output in stdout
    for i in range(len(files)):
        reader = pd.read_csv(files[i],chunksize=1000000,low_memory=False) 
        for chunk in reader:
            chunk['filename'] = os.path.basename(files[i])
            if i==0:
                print(','.join(chunk.columns))
            print(chunk.to_csv(chunksize=1000000, index=False, header=False))

            
if __name__ == '__main__':
    csv_combiner(sys.argv[1:])