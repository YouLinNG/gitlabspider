# encoding=utf8
import sys
import json
import re
reload(sys)
sys.setdefaultencoding('utf-8')

# 最近五次项目构建的成功率
def build_success_rate_five():
    file_info = open("../data/test_result.json", "rb")
    info_data = json.load(file_info)

    final_data=[]
    p1 = re.compile('\d+')
    mydic ={}
    tag = 0

    for info_data_item in info_data:
        mydic["commit_time"] = info_data_item["commit_time"]
        if tag>=5:
            success = 0
            for i in range(tag-5,tag):
                if int(re.search(p1, info_data[i]["build_result"]).group()) == 1:
                    success = success + 1
            success_rate = success / 5.0
            mydic["success_last_five"] = str(success_rate).decode("utf-8")
        else:
            mydic["success_last_five"] = "0"
        mydic["tag"] = str(tag).decode("utf-8")
        tag = tag + 1

        final_data.append(mydic)
        mydic ={}

    with open('../data/result_project_success.json', 'w') as json_file:
        json_file.write(json.dumps(sorted(final_data, key=lambda x: x['commit_time']), indent=4))


def main():
    build_success_rate_five()

if __name__ == '__main__':
    main()