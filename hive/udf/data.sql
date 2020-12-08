--建表
create table mytable(
fname string,
lname string)

--加载数据
load datal local inpath '/tmp/data.txt' into table mytable;

--创建临时UDF
--第一种
select transform(stuff)
using 'script'
as thing1,thing2

--第二种
select transform(stuff)
using 'script'
as (thing1 int, thing2 int)

--步骤
add file /tmp/iteblog.py

select transform(fname) using "python iteblog.py" as (fname,lname) from mytable;