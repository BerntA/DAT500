#!/bin/bash

# Remove old data @ hdfs
hadoop fs -rm -r -f /data/census_* && \

# Remove old data @ local
rm -rf ./data/census_* && \
rm -rf ./data/.census_* && \

# Run preprocessing on raw data. Clean the data.
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -file ./preprocess_mapper.py -mapper preprocess_mapper.py -file ./preprocess_reducer.py -reducer preprocess_reducer.py -input /data/census.csv -output /output/preprocessed && \

# Move the output to our data folder.
hadoop fs -mv /output/preprocessed/part* /data/census_preprocessed.csv && \
hadoop fs -rm -r /output/preprocessed && \

# Run cleaned data through MRJob and/or Spark

# Generate info about births, '<birth year>,<municipality>,<count>' ...
python3 analyze_census_births.py --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -r hadoop hdfs:///data/census_preprocessed.csv --output-dir hdfs:///output/analyze_births --no-output && \
hadoop fs -mv /output/analyze_births/part* /data/census_births.csv && \
hadoop fs -rm -r /output/analyze_births && \

# Generate info about population registered in 19XX.
python3 analyze_census_pop.py --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -r hadoop hdfs:///data/census_preprocessed.csv --output-dir hdfs:///output/analyze_population --no-output && \
hadoop fs -mv /output/analyze_population/part* /data/census_population.csv && \
hadoop fs -rm -r /output/analyze_population && \

# Generate info about religions based in certain municipality and how many representatives they had in 19XX.
# Generate info about field of work, visualize where the most common type of work were more popular (geographically).
# Generate info about gender bias/division.
# Output from PySpark is merged and copied directly over to local disk.
spark-submit --master yarn analyze_census_spark.py && \

hadoop fs -getmerge -skip-empty-file /output/analyze_religion/part* ./data/census_religion.csv && \
hadoop fs -put ./data/census_religion.csv /data/census_religion.csv && \
hadoop fs -rm -r /output/analyze_religion && \

hadoop fs -getmerge -skip-empty-file /output/analyze_work/part* ./data/census_work.csv && \
hadoop fs -put ./data/census_work.csv /data/census_work.csv && \
hadoop fs -rm -r /output/analyze_work && \

hadoop fs -getmerge -skip-empty-file /output/analyze_gender/part* ./data/census_gender.csv && \
hadoop fs -put ./data/census_gender.csv /data/census_gender.csv && \
hadoop fs -rm -r /output/analyze_gender && \

# Remove cache crap from the getmerge func.
rm -rf ./data/.census_* && \

# Copy over results from hdfs
hadoop fs -get /data/census_births.csv ./data/census_births.csv && \
hadoop fs -get /data/census_population.csv ./data/census_population.csv

# Sync with git & open visualize.ipynb!