from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime,timedelta
from django.http import HttpResponse
from bson.json_util import dumps
from bson.objectid import ObjectId
import csv
connection = MongoClient()
db = connection.querydata
# Create your views here.

#1] From a given trip, give me all the data for "Sensor X" over time
def trip(request):
    # connection = MongoClient()
    # db = connection.querydata
    trip_id ='63d4228e01afc1d6b6813e38'
    sensor_name="GPS"
    from_time=datetime.now()-timedelta(days=90)
    to_time=datetime.now()
    sensor_data=db.vesseltripdata.aggregate([{"$match":{"dateTime": {"$gte": from_time,"$lte" :to_time},"tripId":trip_id,'sensorName':sensor_name}},{"$project": {"_id":0}}])
    # print(db)
    # print(sensor_data)
    # print(type(sensor_data))
    # print()
    # print(dumps(list(sensor_data)))
    data=list(sensor_data)
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='sensor_data_trip')
        return res
    return render(request,'trip_data.html',{'data':data})

#2] From a given timespan, give me all the data for "Sensor X" over time
def timespan(request):
    sensor_name="GPS"
    from_time=datetime.now()-timedelta(days=60)
    # print(from_time)
    to_time=datetime.now()
    # print(to_time)
    sensor_data=db.vesseltripdata.aggregate([{"$match":{"dateTime": {"$gte": from_time,"$lte" :to_time},'sensorName':sensor_name}},{"$project": {"_id":0}}])
    # print(sensor_data)
    # print(type(sensor_data))
    # print(list(sensor_data))
    data = list(sensor_data)
    # print(data)
    # print(type(data))
    # print(len(data))
    # print(dumps(list(sensor_data)))
    # print(type(dumps(list(sensor_data))))
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='sensor_data_timespan')
        return res
    return render(request, 'timespan_data.html',{'data':data})

#3] From a given trip, give the sum of "Sensor X" throughout the entire trip
def sum_entire_trip(request):
    trip_id ='63d4228e01afc1d6b6813e38'
    sensor_name="GPS"
    sensor_sum_data=db.vesseltripdata.aggregate([{"$match":{"tripId":trip_id,'sensorName':sensor_name}},{"$addFields": {"arraySize":{"$size":"$dataPoints"}}},{"$group": {"_id":"$sensorName","index0_sum":{"$sum":{"$arrayElemAt":["$dataPoints",0]}},"index1_sum":{"$sum":{"$arrayElemAt":["$dataPoints",1]}},"index2_sum":{"$sum":{"$arrayElemAt":["$dataPoints",2]}}}}])
    # print(sensor_sum_data)
    data = list(sensor_sum_data)
    data[0]['sensor_name']=data[0].pop('_id')
    # print(data)
    # print(data[0].keys())
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='sensor_sum_data')
        return res
    return render(request, 'sum_entire_trip_data.html', {'data':data})

#4] From a given trip, give the average of "Sensor X" throughout the entire trip
def avg_entire_trip(request):
    trip_id ='63d4228e01afc1d6b6813e38'
    sensor_name="GPS"
    sensor_avg_data=db.vesseltripdata.aggregate([{"$match":{"tripId":trip_id,'sensorName':sensor_name}},{"$addFields": {"arraySize":{"$size":"$dataPoints"}}},{"$group": {"_id":"$sensorName","index0_avg":{"$avg":{"$arrayElemAt":["$dataPoints",0]}},"index1_avg":{"$avg":{"$arrayElemAt":["$dataPoints",1]}},"index2_avg":{"$avg":{"$arrayElemAt":["$dataPoints",2]}}}}])
    data = list(sensor_avg_data)
    # print(data)
    data[0]['sensor_name']=data[0].pop('_id')
    # print(data)
    # for i in data:
    #     print(i['sensor_name'])
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='sensor_avg_data')
        return res
    return render(request,'avg_entire_trip_data.html',{'data':data})

#5] From a given boat, give the average of “Sensor X” for each day between these dates
def boat_avg(request):
    from_time=datetime.now()-timedelta(days=60)
    # print(from_time)
    to_time=datetime.now()
    # print(to_time)
    sensor_name="GPS"
    boatsensor_sum_data=db.vesseltripdata.aggregate([{"$match":{"dateTime": {"$gte": from_time,"$lte" :to_time},'sensorName':sensor_name}},{"$addFields": {"arraySize":{"$size":"$dataPoints"}}},{"$group": {"_id":{"day":{"$dayOfMonth":"$dateTime"},"month":{"$month":"$dateTime"},"year":{"$year":"$dateTime"}},"index0_avg":{"$avg":{"$arrayElemAt":["$dataPoints",0]}},"index1_avg":{"$avg":{"$arrayElemAt":["$dataPoints",1]}},"index2_avg":{"$avg":{"$arrayElemAt":["$dataPoints",2]}}}}])
    # print(boatsensor_sum_data)
    # print(type(boatsensor_sum_data))
    data = list(boatsensor_sum_data)
    # for i in data:
    #     print(i)
    data[0]['from_time']=data[0].pop('_id')
    # print(data)
    # print(request.GET.get("export",None))
    # print(request.path)
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='boatsensor_sum_data')
        return res
    return render(request, 'boat_avg_data.html',{'data':data})

#6] For a given trip, tell me which sensors were available
def trip_sensors(request):
    trip_id ='63d4228e01afc1d6b6813e38'
    trip_sensors_data=db.vesseltripdata.aggregate([{"$match":{"tripId":trip_id}},{"$group": {"_id":"$tripId","sensors":{"$addToSet":"$sensorName"}}}])
    # print(trip_sensors_data)
    data = list(trip_sensors_data)
    data[0]['trip_id']=data[0].pop('_id')
    # print(data)
    if request.GET.get("export",None)=="True":
        res=export_csv(data,file='trip_sensors_data')
        return res
    return render(request,'trip_sensor_data.html',{'data':data})

# Data Exporting to CSV file
def export_csv(data,file):
    print("working")
    print(data)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename='+file+'.csv'},
    )
    keys = data[0].keys()
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
    # writer = csv.writer(response)
    # keys = data[0].keys()
    # print(keys)
    # writer.writerow(keys)
    # print(data)
    # for x in data:
    #     writer.writerow((x["index0_avg"],x['index1_avg'],x['index2_avg']))
    # with open(file_name+'.csv', 'w', newline='') as output_file:
        
    #     dict_writer = csv.DictWriter(output_file, keys)
    #     dict_writer.writeheader()
    #     dict_writer.writerows(data)
    return response