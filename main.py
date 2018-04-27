# -*- cording: UTF-8 -*-

from cn.leandeon.utils.projectUtils import ProjectUtils
from cn.leandeon.spark.logClean import *
if __name__ == "__main__":

    log_dir = ProjectUtils.get_conf("log_dir")
    json_dir = ProjectUtils.get_conf("json_dir")
    input_dir = ProjectUtils.get_conf("input_dir")
    output_dir = ProjectUtils.get_conf("output_dir")
    par_date = time.strftime("%Y%m%d", time.localtime())
    table_info = ProjectUtils.get_tb_info()
    """step 1 :convert localhost log file to json file"""
    for tb_name, tb_fields in table_info.items():
        tb_name = tb_name.upper()
        log_path = log_dir + tb_name + par_date + ".log"
        json_path = json_dir + tb_name + par_date + ".json"

        """start convert log to json"""
        #convert_log(log_path, json_path)
        """step 2: put json file to hdfs dir """
        #put_file(json_path, input_dir)
        """step 3: start spark job """
        #run_spark_job(input_dir, output_dir, tb_name, tb_fields, par_date)
        print(tb_name + ":" + tb_fields)

    pass