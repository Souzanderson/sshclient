import sys
import os 

args = "0.0.1"

try: args = sys.argv[1]
except: pass

os.system(f"pip install .\dist\malbsum-{args}-py3-none-any.whl")

