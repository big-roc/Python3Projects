SET mapreduce.job.queuename=root.stats;
SET hive.exec.max.dynamic.partitions = 6000;
SET hive.exec.max.dynamic.partitions.pernode=6000;

CREATE TEMPORARY MACRO pi() 3.141592653897232384626;
CREATE TEMPORARY MACRO month_before(data_date string, n int)
int(regexp_replace(date_sub(from_unixtime(unix_timestamp(data_date ,'yyyyMMdd'), 'yyyy-MM-dd'), 31*n), '-',''));
CREATE TEMPORARY MACRO lng_(coordinate string) float(split(coordinate,',')[0]);
CREATE TEMPORARY MACRO lat_(coordinate string) float(split(coordinate,',')[1]);
CREATE TEMPORARY MACRO valid_coordinate(coordinate string)
if(lng_(coordinate)>=-180 and lng_(coordinate)<=180 and lat_(coordinate)>=-90 and lat_(coordinate)<=90, true, false);
CREATE TEMPORARY MACRO geo_hash_encode_(coordinate string, n int)
if(valid_coordinate(coordinate), geo_hash_encode(coordinate, n), NULL);

CREATE TEMPORARY MACRO week_day_n(itime bigint)
from_unixtime(int(substring(string(itime),0,10)),'u');
CREATE TEMPORARY MACRO ihour(itime bigint)
from_unixtime(int(substring(string(itime),0,10)),'HH');
CREATE TEMPORARY MACRO is_weekday_day(itime bigint)
if(week_day_n(itime) not in (6, 7) and (ihour(itime) between 9 and 12 or ihour(itime) between 13 and 19), true, false);
CREATE TEMPORARY MACRO is_weekday_night(itime bigint)
if(week_day_n(itime) not in (6, 7) and ihour(itime) between 0 and 7, true, false);
