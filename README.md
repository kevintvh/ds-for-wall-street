# ds-for-wall-street
Source code to accompany "Data Science for Wall Street" tutorial at Hadoop World NYC 2015

Clone (download) project into a directory (referenced below)

Download Spark distribution from https://spark.apache.org/downloads.html

Extract archive into a directory (referenced below)

```shell
cd directory_of_ds-for-wall-street
mkvirtualenv -p /usr/bin/python wallstreet # optionally
export SPARK_HOME=directory_of_spark-distribution
python ./setup.py install # or use other installers
ipython notebook
```
