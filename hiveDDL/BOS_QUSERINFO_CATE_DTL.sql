USE BOS_LOG;
drop table if exists BOS_QUSERINFO_CATE_DTL;
CREATE EXTERNAL TABLE `BOS_QUSERINFO_CATE_DTL` (
serialName long ,
bizCode long ,
email string ,
realNameInfo string ,
starLevel string ,
starScore string ,
starTime string ,
userAdd string ,
userAge string ,
userBegin string ,
userBrand string ,
userID string ,
userLevel string ,
userName string ,
userNum string ,
userStatus string ,
zipCode string )
COMMENT '4.2.8-客户信息'
PARTITIONED BY (par_date STRING COMMENT '分区字段,由spark 程序自动生成')
STORED AS orc
LOCATION
  'hdfs://TESTCluster/data/bos_log/bos_quserinfo_cate_dtl';
