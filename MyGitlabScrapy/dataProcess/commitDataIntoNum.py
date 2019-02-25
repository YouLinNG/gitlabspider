# encoding=utf8
import sys
import json
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def getJavaConfigNum(info_data_item):
    java_count = 0
    rb_count = 0
    xml_count = 0
    config_count = 0
    pjava = re.compile('.*\.java.*')
    prb = re.compile('.*\.rb.*')
    pxml = re.compile('.*\.xml.*')
    pconfig = re.compile('.*\.config.*')
    for one_changed_file in info_data_item["changed_file"]:
        if re.search(pjava, one_changed_file):
            java_count = java_count + 1
        if re.search(prb, one_changed_file):
            rb_count = rb_count + 1
        if re.search(pxml, one_changed_file):
            xml_count = xml_count + 1
        if re.search(pconfig, one_changed_file):
            config_count = config_count + 1
    javaNum = java_count + rb_count
    configNum = xml_count + config_count
    return javaNum,configNum

def commitDataIntoNum():
    file_info = open("../data/commit_info_merge.json", "rb")
    info_data = json.load(file_info)

    final_data=[]
    p1 = re.compile('\d+')
    psuccess = re.compile('.*passed.*')
    last_build_result = "0"
    for info_data_item in info_data:
        if info_data_item["build_result"]:
            last_build_time =  int(re.search(p1, info_data_item["commit_time"]).group())
            break
    mydic = { "additions_num": "0 additions","deletions_num": "0 deletions","changed_file_num": "0 changed files","commit_title_length":"0","commit_description_length":"0","java_num":"0","config_num":"0","commit_count":"0","last_build_result":"0","time_interval":"0" }


    for info_data_item in info_data:
        mydic["additions_num"] = str(int(re.search(p1, mydic["additions_num"]).group())+ int(re.search(p1, info_data_item["additions_num"]).group())).decode('utf-8')
        mydic["deletions_num"] = str(int(re.search(p1, mydic["deletions_num"]).group()) + int(re.search(p1, info_data_item["deletions_num"]).group())).decode('utf-8')
        mydic["changed_file_num"] = str(int(re.search(p1, mydic["changed_file_num"]).group()) + int(re.search(p1, info_data_item["changed_file_num"]).group())).decode('utf-8')
        mydic["commit_title_length"] = str(int(re.search(p1, mydic["commit_title_length"]).group())+ len(str(info_data_item["commit_title"]))).decode('utf-8')
        mydic["commit_description_length"] = str(int(re.search(p1, mydic["commit_description_length"]).group()) + len(str(info_data_item["commit_description"]))).decode('utf-8')
        javaNumCal,configNumCal = getJavaConfigNum(info_data_item)
        mydic["java_num"] = str(int(re.search(p1, mydic["java_num"]).group()) + javaNumCal).decode('utf-8')
        mydic["config_num"] = str(int(re.search(p1, mydic["config_num"]).group()) + configNumCal).decode('utf-8')
        mydic["commit_count"] = str(int(re.search(p1, mydic["commit_count"]).group()) + 1).decode('utf-8')

        if info_data_item["build_result"]:
            mydic["author_name"] = info_data_item["author_name"]
            mydic["commit_href"] = info_data_item["commit_href"]
            mydic["commit_id"] = info_data_item["commit_id"]
            mydic["commit_time"] = info_data_item["commit_time"]

            mydic["length_all_description"] = str(int(re.search(p1, mydic["commit_title_length"]).group())+ int(re.search(p1, mydic["commit_description_length"]).group())).decode('utf-8')
            mydic["changed_code_lines"] = str(int(re.search(p1, mydic["additions_num"]).group()) + int(re.search(p1, mydic["deletions_num"]).group())).decode('utf-8')
            mydic["average_commit_filenum"] = str(int(re.search(p1, mydic["changed_file_num"]).group())//int(re.search(p1, mydic["commit_count"]).group())).decode('utf-8')

            mydic["last_build_result"] = last_build_result
            mydic["time_interval"] = str(int(re.search(p1, info_data_item["commit_time"]).group()) - last_build_time).decode('utf-8')

            if re.search(psuccess, info_data_item["build_result"]):
                mydic["build_result"] = "1"
                last_build_result = "1"
            else:
                mydic["build_result"] = "0"
                last_build_result = "0"
            last_build_time = int(re.search(p1, info_data_item["commit_time"]).group())

            final_data.append(mydic)
            mydic = {"additions_num": "0 additions", "deletions_num": "0 deletions", "changed_file_num": "0 changed files","commit_title_length":"0","commit_description_length":"0","java_num":"0","config_num":"0","commit_count":"0","last_build_result":"0","time_interval":"0" }

    with open('../data/test_result.json', 'w') as json_file:
        json_file.write(json.dumps(sorted(final_data, key=lambda x: x['commit_time']), indent=4))


def main():
    commitDataIntoNum()

if __name__ == '__main__':
    main()