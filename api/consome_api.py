# choco install ngrok


import requests
import pandas as pd
from pyspark.sql import SparkSession

# 1. Requisição para API
url = "http://localhost:5000/api/tempo-uso"
response = requests.get(url)
dados_json = response.json()

# 2. Pandas DataFrame
df_pandas = pd.DataFrame(dados_json)

# 3. Criar SparkSession
spark = SparkSession.builder \
    .appName("ConsumoAPI") \
    .master("local[*]") \
    .getOrCreate()

# 4. Converter para DataFrame Spark
df_spark = spark.createDataFrame(df_pandas)

# 5. Exibir resultados
df_spark.printSchema()
df_spark.show(10)

# 6. (Opcional) Salvar como Parquet ou CSV
# df_spark.write.mode("overwrite").parquet("tempo_uso.parquet")
# df_spark.write.mode("overwrite").csv("tempo_uso.csv", header=True)
