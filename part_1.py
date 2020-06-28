
# import findspark
# findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext


spark = SparkSession \
            .builder \
            .appName("Python Spark create RDD example") \
            .master("local[*]") \
            .config("spark.driver.extraClassPath", "/Library/PostgreSQL/pgJDBC/postgresql-42.2.5.jar") \
            .getOrCreate()
spark.conf.set("spark.executor.memory", "12g")
sqlContext = SQLContext(sparkContext=spark.sparkContext,sparkSession=spark)
## User information
user = 'postgres'
pw   = 'priya12345'

## Database information
table_name = 'public.ghtorrent'
url = 'jdbc:postgresql://localhost:5431/ghtorrent?user='+user+'&password='+pw
properties ={'driver': 'org.postgresql.Driver', 'password': pw,'user': user}

#df = spark.read.jdbc(url=url, table=table_name, properties=properties).load()
df=sqlContext.read.format('jdbc').options(url=url,  dbtable=table_name, properties=properties).load()

df.show(5)
df.printSchema()
