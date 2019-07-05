package com.aisiot.bigdata.flinkcore

import org.apache.flink.core.fs.FileSystem.WriteMode
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time._
import org.apache.flink.table.api.scala._



object flinkwc {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    val socketStream = env.socketTextStream("localhost",6996)

    val max_temp = socketStream.map{value => (  value.split(";")(0), value.split(";")(1), value.split(";")(2).toFloat, "temps")}
      .keyBy(3)
      .timeWindow(Time.seconds(5))
      .max(2)


    //val temps = wordsStream.map(number => number)
    //val keyedStream = wordsStream.keyBy(2)
    //val max_temp = keyedStream.reduce((x,y) => max(x,y))
    //wordsStream.print()

    max_temp.map { tuple => tuple._1 + "\t" + tuple._2 + "\t" + tuple._3 + "\r\n" }.writeAsText("C:\\work\\out",WriteMode.OVERWRITE)
    max_temp.print()

    env.execute("Mrinq")
  }
}
