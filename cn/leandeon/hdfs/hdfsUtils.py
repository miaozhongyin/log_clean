# -*- cording: UTF-8 -*-

from hdfs import *

hdfs_client = InsecureClient(url='http://hadoop1:50070', user='hdfs')


def file_exsit(file_path):

    check_res = hdfs_client.status(file_path, strict=False)
    if check_res is None:
        return "No"
    else:
        return "Yes"


def del_file(file_path):

    if file_exsit(file_path) == 'Yes':
        hdfs_client.delete(file_path, recursive=False)
        print("file :" + file_path + " is delete")
    else:
        print("file :" + file_path + " is not exist")


def upload_file(source_file, target_dir):
    hdfs_client.upload(hdfs_path=target_dir, local_path=source_file, overwrite=True)


