from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from RapidAnalyzer.utils import Util
from pymongo import InsertOne, MongoClient
# Create your views here.

# record_structure = {
#         "lastTradePrice":110,
#         'previousClose':100,
#         "tradedOn":'2022-12-1 15:4x`3:34',
#         "open":'',
#         "high":'',
#         "low":"",
#         "close":"",
#         "exchange":"NSE",
#         "index":"NIFTY 50",
#         "sector":"",
#         "industry":""
#     }

res_g = {"msg": 'SUCCESS'}

class MongoData(APIView):

    def get(self, request):
        try:
            db = Util.createConnection()
            dummy_data = db['dummy_data']
            
            exchange = request.GET.get('exchange')
            sector = request.GET.get('sector')
            industry = request.GET.get('industry')
            index = request.GET.get('index')
            page_num = int(request.GET.get('page_num'))
            page_size = int(request.GET.get('page_size'))
            print("\nexchange : ",exchange, "\nsector : ",sector,"\nindustry : ",industry, "\nindex : ",index, "\npage_num : ",page_num,type(page_num), "\npage_size : ",page_size,type(page_size))
            resp = []



            if exchange and sector and industry and index:
                # resp = dummy_data.find({"exchange":exchange, "sector": sector, "industry":industry, "index":index}).skip(page_num).limit(page_size)
                # resp = Util.make_response(resp)
                # print("resp : ",len(resp), resp[0:2])
                resp = []
            elif exchange and sector and industry:
                resp = dummy_data.find({"exchange":exchange, "sector": sector, "industry":industry})
                resp = Util.make_response(resp)
                print("len(resp) : ",len(resp))
                resp = dummy_data.find({"exchange":exchange, "sector": sector, "industry":industry}).skip(page_num).limit(page_size)
                resp = Util.make_response(resp)
                print("resp : ",len(resp), resp)
            elif exchange and sector:
                resp = dummy_data.find({"exchange":exchange, "sector": sector}).skip(page_num).limit(page_size)
                resp = Util.make_response(resp)
                print("resp : ",len(resp), resp[0:2])
            elif exchange:
                resp = dummy_data.find({"exchange":exchange}).skip(page_num).limit(page_size)
                resp = Util.make_response(resp)
                print("resp : ",len(resp), resp)
                
            return Response({"msg": "Data Retrieved", 'data': resp})
        except Exception as e:
            print(f"Error ===> {e}")
            return Response({"msg": "FAILED, {e}"})


class DropdownApi(APIView):
    def get(self, request):
        try:
            print('This is a dropdown API')
            db = Util.createConnection()
            dummy_data_col = db['dummy_data']
            distinct_data = []

            if request.GET.get('exchange'):
                print('got exchange {}'.format(request.GET.get('exchange')))
                distinct_data  = dummy_data_col.find({"exchange":request.GET.get('exchange')}).distinct("sector")
                distinct_data = Util.make_response(distinct_data)
                print("distinct_data : ",distinct_data)
                return Response({"msg": 'SUCCESS, sectors returned.', "data":[]})

            elif request.GET.get('sector'):
                print('got sector {}'.format(request.GET.get('sector')))
                distinct_data  = dummy_data_col.find({"sector":request.GET.get('sector')}).distinct("industry")
                distinct_data = Util.make_response(distinct_data)
                print("distinct_data : ",distinct_data)
                return Response({"msg": 'SUCCESS, industries returned.', "data":distinct_data})

            elif request.GET.get('industry'):
                print('got industry {}'.format(request.GET.get('industry')))
                distinct_data  = dummy_data_col.find({"industry":request.GET.get('industry')}).distinct("stock")
                distinct_data = Util.make_response(distinct_data)
                print("distinct_data : ",distinct_data)
                return Response({"msg": 'SUCCESS, industries returned.', "data":distinct_data})
                
            else:
                raise NotImplementedError(f"unsupported method")

            return Response({"msg": 'SUCCESS', "data":distinct_data})
        except Exception as e:
            print("ERROR ==> ", e)
            return Response({"msg": f'FAILED, {e}', "data":[]})


class CreateData(APIView):
    def post(self, request):
        try:
            db = Util.createConnection()
            dummy_data_col = db['dummy_data']
            data_to_create = []
            # return Response({'msg':'SUCCESSfdsfsfsa'})

            exchangeList = ["NSE", "BSE"]
            indexList = ["NIFTY 50", "NIFTY BANK", "NIFTY"]
            niftyBank = ["HDFC Bank", "ICICI Bank", "State Bank of India", "Kotak Mahindra Bank", "Axis Bank", "Bank of Baroda", "IDFC First Bank",
                         "IndusInd Bank", "Punjab National Bank", "AU Small Finance Bank", "Bandhan Bank", "Federal Bank"]

        #     record_structure = {
        #     "lastTradePrice":0,
        #     'previousClose':0,
        #     "tradedOn":'2022-12-1 15:4x`3:34',
        #     "open":0,
        #     "high":0,
        #     "low":0,
        #     "close":0,
        #     "exchange":"NSE",
        #     "index":"NIFTY",
        #     "sector":"",
        #     "industry":""
        # }

            from datetime import datetime, timedelta
            from dateutil.relativedelta import relativedelta
            import calendar
            import random

            startDate = '2022-01-1'
            startTime = "9:00:00"
            # endTime="15:29:59"
            date_time_format = "%Y-%m-%d %H:%M:%S"

            startDateTime = startDate+" "+startTime
            startDateTime = datetime.strptime(startDateTime, date_time_format)
            print(startDateTime, type(startDateTime))

            year = startDateTime.year
            total_days_in_year = 0
            for i in range(1, 13):
                total_days_in_year += calendar.monthrange(year, i)[1]

            i = 1
            sectorIndustryJson = Util.sectorIndustry()
            for sector, value in sectorIndustryJson.items():
                for indus, value in sectorIndustryJson[sector].items():
                    for stock in value:
                        print(f"for stock {i} :  {stock}")
                        previousClose = 10
                        upper_circuit = previousClose + (previousClose*9.5)/100
                        # print("upper_circuit  : ", upper_circuit)
                        lower_circuit = previousClose - (previousClose*9.5)/100
                        # print("lower_circuit  : ", lower_circuit)
                        lastTradePrice = previousClose

                        for day in range(total_days_in_year):
                            startDateTime_dup = startDateTime + \
                                timedelta(days=day)
                            for mnt in range(24):
                                startDateTime_dup = startDateTime_dup+timedelta(minutes=15, seconds=1) if mnt == 0 else startDateTime_dup+timedelta(
                                    minutes=14, seconds=57) if mnt == 23 else startDateTime_dup+timedelta(minutes=15)
                                lastTradePrice = round(random.uniform(
                                    lower_circuit, upper_circuit), 2)
                                obj = {
                                    # "id":mnt,
                                    'previousClose': previousClose,
                                    "lastTradePrice": lastTradePrice,
                                    "tradedOn": startDateTime_dup,
                                    "exchange": "NSE",
                                    "index": indexList[1] if "bank" in stock else indexList[2],
                                    "sector": sector,
                                    "industry": indus,
                                    "stock": stock
                                }
                                data_to_create.append(InsertOne(obj))
                                # data_to_create.append(obj)
                            previousClose = lastTradePrice
                        i += 1
            print(
                f"Data created successfully, writing {len(data_to_create)} records into collection...")

            # result = dummy_data_col.bulk_write(data_to_create)
            # print("result : ", result)

            return Response({'msg': f'SUCCESS, {len(data_to_create)} records created.', "data": []})

        except Exception as e:
            print(f"Error ===> {e}")
            return Response({'msg': f'FAILED, {e}', "data": []})
