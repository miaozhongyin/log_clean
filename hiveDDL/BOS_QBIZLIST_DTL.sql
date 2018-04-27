USE BOS_LOG;
drop table if exists `BOS_QBIZLIST_DTL`;
CREATE EXTERNAL TABLE `BOS_QBIZLIST_DTL` (
serialName long,
bizCode long,
bizCode string,
bunessCode string,
bunessFree string,
bunessName string,
bunessType string,
deadTime string,
feeType string,
orderingTime string,
showType string,
spid string,
startTime string,
displayType string,
productType string,
oprTime string,
)
COMMENT '4.2.3-已订购业务查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bus-logs/bos_qbizlist_dtl';
