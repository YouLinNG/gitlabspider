# encoding=utf8
import json
import re
import datetime
import time
import pytz

def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return int(time.mktime(time.strptime(time_str, local_format)))

def commits_info_merge():
    file_info = open("commit_info.json", "rb")
    info_data = json.load(file_info)
    file_result = open("project_commit.json", "rb")
    result_data = json.load(file_result)

    p1 = re.compile('[^/]+(?!.*/)')

    commit_info_merge=[]
    i=0
    for result_item in result_data:
        search_id = re.search(p1, result_item["commit_href"]).group(0)
        print search_id
        for info_item in info_data:
            commit_id = info_item["commit_id"]
            if search_id==commit_id[0]:
                i=i+1
                print i
                info_item["commit_href"]=result_item["commit_href"]
                info_item["build_result"] = result_item["build_result"]

                info_item["commit_id"]=info_item["commit_id"][0]
                info_item["additions_num"] = info_item["additions_num"][0]
                info_item["commit_title"] = info_item["commit_title"][0]
                info_item["author_name"] = info_item["author_name"][0]
                info_item["changed_file_num"] = info_item["changed_file_num"][0]
                info_item["deletions_num"] = info_item["deletions_num"][0]
                if info_item["commit_description"]:
                    info_item["commit_description"] = info_item["commit_description"][0]
                else:
                    info_item["commit_description"] =""
                info_item["commit_time"] = str(utc_to_local(info_item["commit_time"][0]))

                commit_info_merge.append(info_item)
                break

    with open('commit_info_merge.json', 'w') as json_file:
          json_file.write(json.dumps(sorted(commit_info_merge, key=lambda x: x['commit_time']), indent=4))


def main():
    commits_info_merge()

if __name__ == '__main__':
    main()
