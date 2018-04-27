
USE BOS_LOG;
drop table if exists `BOS_QHISYFEE_CATE_DTL`;
CREATE EXTERNAL TABLE `BOS_QHISYFEE_CATE_DTL` (
serialName  long,
bizCode  long,
payType  string,
payTypeName  string,
paymentDate  string,
paymentDateCode  string,
staffappprem  string,
oprTime  string,
)
COMMENT '4.2.5-缴费记录查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_qhisyfee_cate_dtl';
