import os
from datetime import datetime

project_path = os.getcwd()
today = datetime.now()
parent_dir = project_path + "\\" + today.strftime('%Y%m%d')
if not os.path.isdir(parent_dir):
    os.mkdir(project_path + "\\" + today.strftime('%Y%m%d'))
    os.mkdir(parent_dir + "\\input")
    os.mkdir(parent_dir + "\\output")
    os.mkdir(parent_dir + "\\process")


input_folder = os.path.join(parent_dir, 'input')
output_folder = os.path.join(parent_dir, 'output')
process_folder = os.path.join(parent_dir, 'process')
