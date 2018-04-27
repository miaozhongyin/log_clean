USE BOS_LOG;
drop table if exists  `BOS_BILL_CATE_DTL`;
CREATE EXTERNAL TABLE `BOS_BILL_CATE_DTL` (
serialName long,
bizCode long,
billCycleEndDate string,
billCycleStartDate string,
billEntries string,
billEntriesValue string,
thirdItemsName string,
thirdItemsValue string,
inBill string,
totalBill string,
oprTime string,
transIDO string
)
COMMENT '4.2.12-详单查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_bill_cate_dtl';
