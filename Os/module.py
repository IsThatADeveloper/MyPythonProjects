import os
from datetime import datetime

os.chdir('/Users/Eshaan/OneDrive/Documents/Code/')

print(os.environ.get('HOME'))

print(dir(os.path))

# for dirpath, dirnames, filenames in os.walk('/Users/Eshaan/OneDrive/Documents/Code/'):
    # print('Current Path:', dirpath)
    # print('Directories:', dirnames)
    # print('Files:', filenames)
    # print()

    

# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1')

# os.rmdir('OS-Demo-2')
# os.removedirs('OS-Demo-2/Sub-Dir-1')

# os.rename('OS-Demo-2', 'OS-Demo')

# mod_time = os.stat('OS-Demo-2').st_mtime

# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

