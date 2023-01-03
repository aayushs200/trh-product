from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from RapidAnalyzer.utils import Util
from pymongo import MongoClient
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

class MongoData(APIView):
    
    def get(self, request):
        try: 
            res = []
            sectorIndustryJson = Util.sectorIndustry()
            for key, value  in sectorIndustryJson.items():
                print("sector : ", key)
                for key, value in sectorIndustryJson[key].items():
                    print("    industry: ", key)
                    res.extend(value)
            print(len(res))
            
            return Response({"msg":"Data Retrieved", 'data':res})
        except:
            pass
            # filtered_data=[]
            
            # db = Utils.createConnection()
            
            # '''accessing live data collection'''
            # live_data_col = db['live_data'] 
            # cursor = live_data_col.find({"InstrumentIdentifier":"NIFTY 50"})
            # r = Utils.make_response(cursor)
            # print('filter_res : ',len(r) ,r[0:1])
            
            # return Response({"msg":"SUCCESS"})
            
            
        #     res = []
        #     sectorIndustryJson = Utils.sectorIndustry()
        #     sector = request.GET.get('sector')
        #     industry = request.GET.get('industry')
        #     print(sector, industry)
        #     if sector and industry:
        #         for key, value in sectorIndustryJson.items():
        #             if sector == key:
        #                 for indus in sectorIndustryJson[key]:
        #                     if industry == indus:
        #                         res = sectorIndustryJson[key][indus]

        #     return Response({'msg':'SUCCESS', 'data':res})
        # except Exception as e:
        #     print('error ==> ', e)
        #     return Response({'msg':'FAILED, exception occured.', 'data':[]})
            
class CreateData(APIView):
    def post(self, request):
        data_to_create = []
        
        exchangeList = ["NSE", "BSE"]
        indexList = ["NIFTY 50", "NIFTY BANK", "NIFTY"]
        niftyBank = ["HDFC Bank", "ICICI Bank", "State Bank of India", "Kotak Mahindra Bank", "Axis Bank", "Bank of Baroda", "IDFC First Bank",
                     "IndusInd Bank", "Punjab National Bank", "AU Small Finance Bank", "Bandhan Bank", "Federal Bank"]
        
        record_structure = {
        "lastTradePrice":0,
        'previousClose':0,
        "tradedOn":'2022-12-1 15:4x`3:34',
        "open":0,
        "high":0,
        "low":0,
        "close":0,
        "exchange":"NSE", 
        "index":"NIFTY",
        "sector":"",
        "industry":""
    }
        
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        import calendar
        startDate = '2022-11-1'
        startTime="9:15:1"
        endTime="15:29:59"
        date_time_format = "%Y-%m-%d %H:%M:%S"
        
        startDateTime = startDate+" "+startTime
        startDateTime = datetime.strptime(startDateTime, date_time_format)
        print(startDateTime, type(startDateTime))
        
        year = startDateTime.year
        
        total_days_in_year = 0
        for i in range(1,13):
            total_days_in_year+=calendar.monthrange(year,i)[1]
                    
        sectorIndustryJson = Util.sectorIndustry()
        for sector, value  in sectorIndustryJson.items():
            # print("sector : ", sector)
            for indus, value in sectorIndustryJson[sector].items():
                # print("    industry: ", indus)
                # data_to_create.extend(value)
                for stock in value:
                    lastTradePrice = 10
                    previousClose  = 10
                    tradedOn = ''
                    
                    for day in range(total_days_in_year):
                        for hr in range(12):
                            obj = {
                                "lastTradePrice":19,
                                'previousClose':10,
                                "tradedOn":'',
                                "open":10,
                                "high":19,
                                "low":1,
                                "close":19,
                                "exchange":"NSE", 
                                "index":"NIFTY",
                                "sector":"",
                                "industry":""
                            }
                            data_to_create.append(obj)
            #                 break
            #         break
            #     break
            # break
        print("data_to_create : ",  len(data_to_create))
        return Response({'msg':f'SUCCESS, {data_to_create} records created.', "data":[]})
