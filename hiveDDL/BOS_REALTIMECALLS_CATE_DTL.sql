USE BOS_LOG;
drop table if exists `BOS_REALTIMECALLS_CATE_DTL`;
CREATE EXTERNAL TABLE `BOS_REALTIMECALLS_CATE_DTL` (
serialName long,
bizCode long,
curFee string,
curFeeTotal string,
oweFee string,
realFee string
 )
COMMENT '4.2.6-实时话费查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_realtimecalls_cate_dtl';
--ALTER TABLE `BOS_REALTIMECALLS_CATE_DTL` ADD IF NOT EXISTS PARTITION (par_date='2018-04-04') LOCATION 'hdfs://TESTCluster/data/bus-logs/BOS_REALTIMECALLS_CATE_DTL/par_date=2018-04-04'; 
