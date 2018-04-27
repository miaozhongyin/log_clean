USE BOS_LOG;
drop table if exists `BOS_QSCORE_CATE_DTL`;
CREATE EXTERNAL TABLE `BOS_QSCORE_CATE_DTL` (
 `serialNumber` bigint COMMENT '手机号码',
 `bizCode` bigint COMMENT '返回编码',
 `brand` STRING COMMENT '品牌信息',
 `point_name` STRING COMMENT '积分名称',
 `point_value` STRING COMMENT '积分值',
 `pointValue` STRING COMMENT '可用积分')
 COMMENT '4.2.1-积分查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_qscore_cate_dtl';
--ALTER TABLE `BOS_QSCORE_CATE_DTL` ADD IF NOT EXISTS PARTITION (par_date='2018-04-04') LOCATION 'hdfs://TESTCluster/data/bus-logs/bos_qscore_cate_dtl/par_date=2018-04-04'; 
