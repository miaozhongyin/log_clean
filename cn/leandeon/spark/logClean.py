# -*- cording: UTF-8 -*-
import pandas as pd
import json
import time
import subprocess
import os
from cn.leandeon.utils.projectUtils import ProjectUtils

__doc__ = "use pandas to convert log to json "
__author__ = "ZhongYin.miao"


def convert_log(input_path, output_path):

    if input_path == "" or output_path == "":
        print("please input log file path and json file out path , like '/home/test.log and /home/test.json'")
    if os.path.exists(input_path) and (not os.path.exists(output_path)):
        df = pd.read_table(input_path, sep='\|\#\$', engine='python', names=['serialName', 'bizCode', 'jsonData'])
        data = df.to_dict(orient='records')
        for _ in data:
            _.update(json.loads(_['jsonData'], encoding='utf-8'))
            del _['jsonData']

        df1 = pd.DataFrame(data)
        df1.to_json(output_path, orient='records', force_ascii=False)


def run_spark_job(input_dir, output_dir, tb_name, fields, par_date):
    script = ProjectUtils.get_root_dir()+ProjectUtils.delimiter+"scripts"+ProjectUtils.delimiter+ProjectUtils.get_conf("clean_script")
    cmd = 'sh '+script
    obj = subprocess.Popen([cmd, input_dir, output_dir, tb_name, fields, par_date], stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_out = obj.stdout.read()
    obj.stdout.close()
    cmd_err = obj.stderr.read()
    obj.stderr.close()
    print("cmd_out :" + cmd_out + "\n")
    print("cmd_err :" + cmd_err + "\n")


def put_file(source_path, target_dir):
    result = subprocess.check_output(['hdfs dfs -put ', source_path, target_dir], shell=False)
    print(result)


def start_convert_log():

    log_dir = ProjectUtils.get_conf("log_dir")
    json_dir = ProjectUtils.get_conf("json_dir")
    input_dir = ProjectUtils.get_conf("input_dir")
    output_dir = ProjectUtils.get_conf("output_dir")
    par_date = time.strftime("%Y%m%d", time.localtime())
    table_info = ProjectUtils.get_tb_info()
    """step 1 :convert localhost log file to json file"""
    for tb_name, tb_fields in table_info.items():
        tb_name = tb_name.upper()
        log_path = log_dir+tb_name+par_date+".log"
        json_path = json_dir+tb_name+par_date+".json"

        """start convert log to json"""
        convert_log(log_path, json_path)
        """step 2: put json file to hdfs dir """
        put_file(json_path, input_dir)
        """step 3: start spark job """
        run_spark_job(input_dir, output_dir, tb_name, tb_fields, par_date)
        print(tb_name + ":" + tb_fields)


















