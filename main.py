# -*- cording: UTF-8 -*-

from cn.leandeon.utils.projectUtils import ProjectUtils
from cn.leandeon.spark.logClean import *
from cn.leandeon.hdfs.hdfsUtils import *
import datetime
if __name__ == "__main__":

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
        try:
            """start convert log to json"""
            convert_log(log_path, json_path)
            """step 2: put json file to hdfs dir """
            put_file(json_path, input_dir,  json_file_name)
            """step 3: start spark job """
            run_spark_job(input_dir, output_dir, tb_name, tb_fields, par_date)
            log.logger.info(tb_name + ":" + par_date + log_date + tb_fields)
        except Exception, e:
            log.logger.error(e)
            exit(1)

    pass
