# coding:utf8
from __future__ import print_function

from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName('PythonWordCount') \
        .getOrCreate()

    path = "../data/word_count.txt"
    lines = spark.read.text(path).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
