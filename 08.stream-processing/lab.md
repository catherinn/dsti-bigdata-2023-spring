# Data Engineering with Spark

## Lab 6: Structured Streaming

### Goals

- Stream the NYC Taxi datasets on a socket
- Use Spark Streaming to analyze the stream

### Lab resources

- The `data` directory contains the NYC Taxi datasets;
- The `stream_taxi_data_socket.py` allows to stream a dataset through a socket on a given port.

### Streaming the datasets

To stream the NY datasets:

- Go to this directory:
  ```
  cd lab-resources 
  ```
- Create a checkpoint directory for Spark Streaming in your HDFS personal folder:
  ```bash
  hdfs dfs -mkdir -p "/education/ece/big-data/2020/fall/bda/gr1/$USER/spark-streaming/checkpoint"
  ```
- Run the `stream_taxi_data_socket.py` script. The script has 3 parameters: the server name to use to stream the data, the port on which to open the socket, the dataset to stream (can be either `fares` or `rides`)
  ```bash
  PORT=11111
  hdfs dfs -rm -r -f "/education/ece/big-data/2020/fall/bda/gr1/$USER/spark-streaming/checkpoint/*"
  python3 stream_taxi_data_socket.py edge-1.au.adaltas.cloud "$PORT" fares
  ```
Then start the processing on the fly in your spark shell. you first always select the data then process whatever you want.
<img width="1166" alt="Screenshot 2023-09-09 at 12 45 11" src="https://github.com/catherinn/dsti-bigdata-2023-spring/assets/31245352/4fe0f53e-9430-4444-939c-5d4e1f32b4c3">

If we want to implement the window, we can do it - search in google spark window streaming

how window works:
![Screenshot 2023-09-10 at 10 29 54](https://github.com/catherinn/dsti-bigdata-2023-spring/assets/31245352/50896d1f-2c96-4aa7-82dc-b0b49c84c9f9)

- on the cluster(remote or local)
```PORT=11225
hdfs dfs -rm -r -f "/dsti_spoc/$USER/spark-streaming/checkpoint/*"
python3 stream_taxi_data_socket.py edge-1.au.adaltas.cloud "$PORT" fares```

this si my location normally: ```dsti_spoc/$USER/```



# on the driver
```val stream = spark.readStream.format("socket").option("host","localhost").option("port","11225").load().select(split(col("value"),",").getItem(0).cast("int").as("id"),
split(col("value"),",").getItem(1).cast("int").as("longid"),
split(col("value"),",").getItem(3).cast("timestamp").as("start_date"),
split(col("value"),",").getItem(4).as("payment_type"),
split(col("value"),",").getItem(5).cast("double").as("tax"),
split(col("value"),",").getItem(6).cast("double").as("tip"),
split(col("value"),",").getItem(7).cast("double").as("total"))```
- here we cast timestamp as startdate

```stream.withWatermark(("start_date"), "1 minute").groupBy(window(col("start_date"), "10 minutes", "5 minutes")).sum("total")```
the 5 mins means sliding window, because the 1. defines the length of the windoiw and the 2. how often it is open
- you have max 3 windows at the time, 90% of the time 2 windows, 10% 3 windows. the - withWatermark is when is the window closed after it ended

- we want to see the results printed
res4.writeStream.format("console").start().awaitTermination()
- in prod we don't do thsi, because we are only writing an output on the console of the driver, but we could for example
- use kafka as the output, republish the agregagte on kafka and then showing the result on the website
