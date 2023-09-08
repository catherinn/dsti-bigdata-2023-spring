dowload spark shell
launch it in terminal by going to to the spark directory you dowhloaded and typing in: spark-shell
Note: it is also possible to use the cluster to run it, but as it will be shut down at some point, it is better to use the shell. There also launch it with typing spark-shell


1. Create a csv:
  ....
  echo "id,nom,prenom,age" >> myfile.txt
  echo "1,sauvage,pierre,31" >> myfile.txt

  #add other values
  echo "....." >> myfile.txt

=========

If you run spark in cluster, please also put myfile in the cluster

hdfs dfs -put myfile.txt ./myfile.txt

2. load csv into RDD in spark

```
val rdd = sc.textFile("file:///home/<my_user>/monfichier.txt")

# or from hdfs
val rdd = sc.textFile("hdfs:///user/<my_user>/monfichier.txt")
res5.collect.foreach(println)
```

# at this point the file is not loaded yet. it created the file, but not loaded.
Even if we are local rdd is distributed - it has executors, so it will be on the executors. is a variable in the cluster, not on the driver.

We will ask spark to get the data the rdd that are in the cluster and get them in the driver and then from there print them. So we ask the executor to broadcast their variable to the driver: gie me back my rdd which is in the driver.

2b. Print content of RDD
```rdd.collect().foreach(println)``` # collect is an action
In reality we never do this. because we deal with huuuge data.

2c: Filter rdd : delete lines where age is smaller than 18 
```rdd.filter((s) => s.split(",")(3).toInt > 18)``` # index 4 because it starts with 0
When we check the result, there is an error because we cannot filter the header. rdd doesn't work with headers it is a problem because we are mixing metadata with data
So we remove the header then,
```
val rdd = sc.textFile("hdfs:///pathtomyfile/myfile.txt")
rdd.filter((s) => s.split(",")(3).toInt > 18)
res5.collect.foreach(println)
```

2d: Convert RDD in dataframe (google est votre ami)

========

3. load csv into dataframe in Spark
   ```val df = spark.read.format("csv").option("header","true").load("file:///Users/katarinalechner/Documents/DSTI/big_data/myfile.txt")```
   
 
3b. Print content of DF
``` df.show()```

3c: Filtrer DF: delete lines where age < 18
by using the df API and mix it
```df.filter("age>18").show()```

pure df API
df.dilter(col(age) > lit(18)).show()

if we want to do pure SQL = sql api first:
``` df.createOrReplaceTempView("person")```
then write the SQL
spark.sql("SELECT * FROM person WHERE age > 18")
refxy.show()

or mix the 2 ways

bonus:  In Spark native API, then in SQL (spark.sql("..."))

3d: Print minimal, maximal, average age

```df.schema``` prints a schema of the data

creating a df from rdd
we have a rdd of string
split the rdd into an array of string + 
rdd.map((s) => s.split(",")  # we see that df is just a dataset of rows with schema on top of it
wrap my rdd of array into a row of elements
import org.apache.spar.sql.Row
val rddrow = rdd.map((s) => s.split(",")).map((s) => Row(s(0),s(1),s(2),s(3),))
add schema
val dfrow = spark.createDataFrame(rddrow,df.schema)
