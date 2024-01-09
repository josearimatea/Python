from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("ExemploSparkCore")
sc = SparkContext(conf=conf)

# Criar um RDD a partir de uma coleção local
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Realizar operações no RDD
resultado = rdd.map(lambda x: x * 2).reduce(lambda a, b: a + b)

# Exibir o resultado
print(f"Resultado: {resultado}")

# Fechar o SparkContext
sc.stop()
