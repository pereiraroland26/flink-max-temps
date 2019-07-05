
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    

    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)
    
    sc = SparkContext(appName="PythonStreamingNetwork")
    ssc = StreamingContext(sc, 10)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    
    validNumbers = lines.map(lambda line: line.split("\t")[2])
    
    temps = validNumbers.map(lambda number: float(number))

    ##max_temp = temps.reduce(lambda x, y: max(x , y))
    
    max_temp = temps.reduceByWindow(lambda x, y: max(x , y), invReduceFunc=None, windowDuration=30, slideDuration=10)

    temps.pprint()
    max_temp.pprint()

    ssc.start()
ssc.awaitTermination()