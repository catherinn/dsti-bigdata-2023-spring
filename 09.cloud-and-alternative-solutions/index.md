---
duration: 3 hours
---

# Cloud and alternative platforms

## Types of cloud computing

![Types of cloud computing](./assets/iaas-paas-saas.png)

## On-premise vs Cloud

- Elastic computing:
  - Cloud storage
  - Elastic compute
  - Pay at usage
- Time to market
- Total Cost of Ownership
  - It’s easy
  - It’s expensive
- CLOUD Act

## Kubernetes/Cloud native

- Object storage (S3-like):
  - [Rook](https://rook.io/) + [Ceph](https://ceph.io/en/)
  - [MinIO](https://min.io/)
- Kubernetes-native distributed execution engines:
  - Apache Spark
  - [Trino](https://trino.io/)

## Solutions and tools - IaaS

- **Bare-metal** server renting:
  - Private and public clouds (IBM, OVH)
  - Enterprise distribution (pay for support)
  - Scalable but slow
- **Big Data Cloud** solutions:
  - Amazon EMR, Azure HDInsight, Google Dataproc
  - Elastic infrastructure, dynamic VM allocation

## Solutions and tools - PaaS

- **Data Warehouse** platforms: Snowflake, Teradata
- **Data Analysis** platforms: Databricks (Azure, AWS, GCP)
- **Managed Big Data** platforms: Elastic Cloud, Cloudera Data Platform

## Solutions and tools - ETL/Dataﬂow/Streaming

- **ETL**: Talend, Informatica
- **Dataflow**: Apache NiFi, StreamSets, SnapLogic
- **Messaging**: Kafka (Confluent), RabbitMQ
- **Streaming frameworks**: Spark Streaming (Databricks), Flink (Ververica), Kafka Streams (Confluent)

## Solutions and tools - BI & Monitoring

- **Business Intelligence**: Qlikview, Tableau, Power BI, MicroStrategy
  - apache superset! cheap. start with a docker container
- **Monitoring**: Datadog, Splunk, Prometheus, Grafana

## Solutions and tools - ML Platforms

- Dataiku
- H2O
- MLFlow (Databricks)

## What’s next in Big Data? Data mesh

Hadoop was first implemented by Yahoo (DOug Cutting), after google published a scientific paper on how they do distributed systems. So google invented it and yahoo implemented it.

[How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html)



Databricks
- founded by the founders of spark
- platform for data engineering and data science
- it's a jupyter notebook style, like zepelin
- first? datalake house deltalake, which has both properties of the datawarehouse and data lake
- analytical platform for DE/DS
<img width="519" alt="Screenshot 2023-09-11 at 14 12 44" src="https://github.com/catherinn/dsti-bigdata-2023-spring/assets/31245352/8f5c4ae6-3627-4e79-af42-0fc20e47ffe9">
