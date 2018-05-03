# -*- cording: UTF-8 -*-
import pandas as pd
import json
import datetime
import subprocess
import os
from cn.leandeon.hdfs.hdfsUtils import *
from cn.leandeon.utils.projectUtils import ProjectUtils
from cn.leandeon.utils.logger import Log

__doc__ = "use pandas to convert log to json "
__author__ = "ZhongYin.miao"


log = Log("logClean")


def convert_log(input_path, output_path):

    if input_path == "" or output_path == "":
        log.logger.error("please input log file path and json file out path , like '/home/test.log and /home/test.json'")
        return 1
    if os.path.exists(input_path) and (not os.path.exists(output_path)):
        df = pd.read_table(input_path, sep='\|\#\$', engine='python', names=['serialName', 'bizCode', 'jsonData'])
        data = df.to_dict(orient='records')
        for _ in data:
            _.update(json.loads(_['jsonData'], encoding='utf-8'))
            del _['jsonData']

        df1 = pd.DataFrame(data)
        df1.to_json(output_path, orient='records', force_ascii=False)
        log.logger.info("log convert json is done")
        return 0
    else:
        log.logger.error("log file path or json file exist....")
        return 1


def run_spark_job(input_dir, output_dir, tb_name, fields, par_date):
    script = ProjectUtils.get_root_dir()+ProjectUtils.delimiter+"scripts"+ProjectUtils.delimiter+ProjectUtils.get_conf("clean_script")
    cmd = 'sh '+script + " " + input_dir + " " + output_dir + " " + par_date + " " + tb_name + " " + fields
    obj = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_out = obj.stdout.read()
    obj.stdout.close()
    cmd_err = obj.stderr.read()
    obj.stderr.close()
    log.logger.info("cmd_out :" + cmd_out + "\n")
    log.logger.error("cmd_err :" + cmd_err + "\n")


def put_file(source_path, target_dir, json_file_name):
    file_path = target_dir + json_file_name
    del_file(file_path)
    if os.path.exists(source_path):
        log.logger.info("start upload local file to hadoop ")
        upload_file(source_path, target_dir)
        return 0
    else:
        log.logger.error("source_path :" + source_path + "is not  exist ")
        return 1


def start_convert_log():

    log_dir = ProjectUtils.get_conf("log_dir")
    json_dir = ProjectUtils.get_conf("json_dir")
    input_dir = ProjectUtils.get_conf("input_dir")
    output_dir = ProjectUtils.get_conf("output_dir")
    log_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    par_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")
    table_info = ProjectUtils.get_tb_info()
    """step 1 :convert localhost log file to json file"""
    for tb_name, tb_fields in table_info.items():
        tb_name = tb_name.upper()
        json_file_name = tb_name + par_date + ".json"
        log_file_name = tb_name + par_date + ".log"
        log_path = log_dir + log_date + '/' + log_file_name
        json_path = json_dir + json_file_name

        """start convert log to json"""
        convert_log(log_path, json_path)
        """step 2: put json file to hdfs dir """
        put_file(json_path, input_dir,  json_file_name)
        """step 3: start spark job """
        run_spark_job(input_dir, output_dir, tb_name, tb_fields, par_date)
        log.logger.info(tb_name + ":" + par_date + log_date + tb_fields)

    pass

















