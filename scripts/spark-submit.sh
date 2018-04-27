#!/usr/bin/env bash
/usr/hdp/2.4.2.0-258/spark/bin/spark-submit --class cn.leadeon.spark.HdfsEval \
    --master yarn \
    --deploy-mode client \
    --driver-memory 2g \
    --executor-memory 6g \
    --executor-cores 24 \
    --num-executors 200 \
    --queue default \
    $1 $2 $3 $4 $5
