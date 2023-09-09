1. Create a csv:
````
id,author,genre,quantity
1,hunter.fields,romance,15
2,leonard.lewis,thriller,81
3,jason.dawson,thriller,90
4,andre.grant,thriller,25
5,earl.walton,romance,40
6,alan.hanson,romance,24
7,clyde.matthews,thriller,31
8,josephine.leonard,thriller,1
9,owen.boone,sci-fi,27
10,max.mcBride,romance,75
```
=========

2. Load csv into dataframe in Spark
```
echo "id,author,genre,quantity" >> lab6.2.csv
echo "1,hunter.fields,romance,15" >> lab6.2.csv
echo "2,leonard.lewis,thriller,81" >> lab6.2.csv
echo "3,jason.dawson,thriller,90" >> lab6.2.csv
echo "4,andre.grant,thriller,25" >> lab6.2.csv
echo "5,earl.walton,romance,40" >> lab6.2.csv
echo "6,alan.hanson,romance,24" >> lab6.2.csv
echo "7,clyde.matthews,thriller,31" >> lab6.2.csv
echo "8,josephine.leonard,thriller,1" >> lab6.2.csv
echo "9,owen.boone,sci-fi,27" >> lab6.2.csv
echo "10,max.mcBride,romance,75"  >> lab6.2.csv
```

3. Generate number of writers per genre
```spark.sql("SELECT genre, count(*) FROM author GROUP BY genre")```

4. Ranking authors per number of written books:
```spark.sql("SELECT rank() over (order by quantity desc) as rank, author, quantity FROM author ORDER BY quantity DESC")
```

```
df("name")split("".").show()
val windowSpec = Window.orderBy(desc("quantity"))
df.withColumn("id",rank().over(windowSpec)).orderBy(desc("quantity"))
``` 

```
Ex of output:
ranking,author,genre,quantity
1,jason.dawson,thriller,90
2,leonard.lewis,thriller,81
3,max.mcBride,romance,75
4,earl.walton,romance,40
5,clyde.matthews,thriller,31
6,owen.boone,sci-fi,27
7,andre.grant,thriller,25
8,alan.hanson,romance,24
9,hunter.fields,romance,15
10,josephine.leonard,thriller,1

https://sparkbyexamples.com/spark/spark-sql-window-functions/


5. Rename name in a "standard" way 'jason.dawson' => 'Jason Dawson'
val resultDF = df.withColumn("author", regexp_replace($"author", "\\.", " "))
resultDF.withColumn("author", initcap(col("author"))).show

https://sparkbyexamples.com/spark/spark-sql-window-functions/


6. Load following set

val input = Seq(
  ("100","John", Some(35),None),
  ("100","John", None,Some("Georgia")),
  ("101","Mike", Some(25),None),
  ("101","Mike", None,Some("New York")),
  ("103","Mary", Some(22),None),
  ("103","Mary", None,Some("Texas")),
  ("104","Smith", Some(25),None),
  ("105","Jake", None,Some("Florida"))).toDF("id", "name", "age", "city")

scala> input.show
+---+-----+----+--------+
| id| name| age|    city|
+---+-----+----+--------+
|100| John|  35|    null|
|100| John|null| Georgia|
|101| Mike|  25|    null|
|101| Mike|null|New York|
|103| Mary|  22|    null|
|103| Mary|null|   Texas|
|104|Smith|  25|    null|
|105| Jake|null| Florida|
+---+-----+----+--------+


7. Merge cells of same id:
```var gr = input.groupBy("id","name").agg(first("city",true),(first("age",true)))```

scala> solution.show()
+---+-----+----+--------+
|id |name |age |city    |
+---+-----+----+--------+
|100|John |35  |Georgia |
|101|Mike |25  |New York|
|103|Mary |22  |Texas   |
|104|Smith|25  |null    |
|105|Jake |null|Florida |
+---+-----+----+--------+
