# encoding=utf8
import sys
import json
import re


reload(sys)
sys.setdefaultencoding('utf-8')
file_info = open("test.json", "rb")
info_data = json.load(file_info)

pjava = re.compile('.*\.java.*')
prb = re.compile('.*\.rb.*')
pxml = re.compile('.*\.xml.*')
pconfig = re.compile('.*\.config.*')

for info_data_item in info_data:
    java_count = 0
    rb_count = 0
    xml_count = 0
    config_count = 0
    for one_changed_file in info_data_item["changed_file"]:
        print one_changed_file
        if re.search(pjava, one_changed_file):
            java_count=java_count+1
        if re.search(prb, one_changed_file):
            rb_count = rb_count + 1
        if re.search(pxml, one_changed_file):
            xml_count = xml_count + 1
        if re.search(pconfig, one_changed_file):
            config_count = config_count + 1
    print java_count + rb_count
    print xml_count + config_count

def getJavaConfigNum(info_data_item):
    java_count = 0
    rb_count = 0
    xml_count = 0
    config_count = 0
    for one_changed_file in info_data_item["changed_file"]:
        print one_changed_file
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