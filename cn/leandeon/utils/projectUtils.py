
# -*- cording: UTF-8 -*-
import json
import os
import platform

__doc__ = "use pandas to convert log to json "
__author__ = "ZhongYin.miao"


class ProjectUtils:

    def __init__(self):
        pass

    delimiter = '\\' if platform.system() == "Windows" else '/'
    project_conf = "project_conf.json"
    table_info = "table_fields1.txt"

    @staticmethod
    def get_root_dir():
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        pro_dir = os.path.dirname(os.path.split(os.path.split(cur_dir)[0])[0])
        return pro_dir

    @staticmethod
    def get_res_dir():

        pro_dir = ProjectUtils.get_root_dir()
        res_path = pro_dir+ProjectUtils.delimiter+"resources"
        return res_path

    @staticmethod
    def get_conf(key):
        """
        read project_conf.json file and return value according what's you input key
        :param key: key
        :return: value
        """
        res_dir = ProjectUtils.get_res_dir()
        res_path = res_dir+ProjectUtils.delimiter + ProjectUtils.project_conf
        with open(res_path, "r") as f:
            context = json.loads(f.read())
            if key in context.keys():
                return context[key]
            else:
                return ""

    @staticmethod
    def get_tb_info():
        """
         read table_fields.txt and return table fields info
        :return: {key=tableName,value=table fields}
        """
        res_dir = ProjectUtils.get_res_dir()
        tb_info = {}
        file_name = res_dir+ProjectUtils.delimiter + ProjectUtils.table_info
        with open(file_name) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                    pass
                else:
                    info = [info for info in line.split("=")]
                    if len(info) == 2:
                        tb_info[info[0]] = info[1]
                    else:
                        pass

        return tb_info






