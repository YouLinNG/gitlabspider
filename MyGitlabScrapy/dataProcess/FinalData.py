# encoding=utf8
import sys
import json
import re
import pandas as pd
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

def finalDataChoose():
    file_info = open("../data/test_result.json", "rb")
    info_data = json.load(file_info)

    info_dataset = pd.DataFrame(info_data, columns=[ 'changed_code_lines', 'changed_file_num', 'java_num', 'config_num',  'commit_count',  'average_commit_filenum', 'length_all_description','build_result'])
    info_dataset = info_dataset.convert_objects(convert_numeric=True)
    col = info_dataset.columns.values.tolist()
    col1 = col[2:-1]
    data_x = np.array(info_dataset[col1])
    data_y = info_dataset['build_result']
    return data_x,data_y

def main():
    finalDataChoose()

if __name__ == '__main__':
    main()