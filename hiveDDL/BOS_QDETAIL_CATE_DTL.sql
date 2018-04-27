USE BOS_LOG;
drop table if exists `BOS_QDETAIL_CATE_DTL`;
CREATE EXTERNAL TABLE `BOS_QDETAIL_CATE_DTL` (
serialName long,
bizCode long,
billCycleEndDate string,
billCycleStartDate string,
callList_commFee string,
callList_commMode string,
callList_commPlac string,
callList_commTime string,
callList_commTimeH5 string,
callList_commType string,
callList_eachOtherNm string,
callList_mealFavorable string,
callList_tmemRecord_startTime string,
messageList_bunessName string,
messageList_commFee string,
messageList_commMode string,
messageList_commPlac string,
messageList_eachOtherNm string,
messageList_infoType string,
messageList_meal string,
messageList_startTime string,
netPlayList_commFee string,
netPlayList_commPlac string,
netPlayList_commTime string,
netPlayList_meal string,
netPlayList_netPlayType string,
netPlayList_netType string,
netPlayList_startTime string,
netPlayList_sumFlow string,
otime string,
tmemType string,
totalCount string
)
COMMENT '4.2.1-详单查询'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_qdetail_cate_dtl';
