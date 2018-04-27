USE BOS_LOG;
drop table if exists BOS_QSCOREHIS_CATE_DTL;
CREATE EXTERNAL TABLE `BOS_QSCOREHIS_CATE_DTL` (
serialName long ,
bizCode long ,
oprTime string ,
contentDesc string ,
cousPonit string ,
cousTime string ,
opType string ,
ponitType string ,
remark string ,
serviceNum string
)
COMMENT '4.2.15-积分记录查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION 
'hdfs://TESTCluster/data/bus_bos/bos_qscorehis_cate_dtl';
