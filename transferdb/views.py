from django.shortcuts import render
from pymongo import MongoClient
from models import *

# Create your views here.

def saveRoute():
    client = MongoClient("localhost", 27017)
    db = client.scrapping
    cursor = db.route_data.find()
    for each in cursor:
        r = RouteData(
            depTimeString=str(each.get('depTimeString')),
            maxUpperColumns=str(each.get('maxUpperColumns')),
            fromCity=str(each.get('FromCity')),
            maxLowerColumns=str(each.get('maxLowerColumns')),
            maxLowerRows=str(each.get('maxLowerRows')),
            DPInformationList=each.get('DPInformationList'),
            toCity=str(each.get('ToCity')),
            maxUpperRows=str(each.get('maxUpperRows')),
            vehicleType=str(each.get('vehicleType')),
            BPInformationList=each.get('BPInformationList'),
            travelDate=str(each.get('travelDate')),
            busType=str(each.get('busType')),
            MPax=str(each.get('MPax')),
            serviceName=str(each.get('serviceName')),
            seatList=str(each.get('seatlist')),
            toCityId=str(each.get('ToCityId')),
            operatorId=str(each.get('operatorId')),
            amenities=str(each.get('amenties')),
            notes=str(each.get('Notes')),
            dateOFJourney=str(each.get('DateOfJourney')),
            routeId=str(each.get('RouteId')),
            travels=str(each.get('Travels')),
            arrTime=str(each.get('arrTime')),
            arrTimeString=str(each.get('arrTimeString')),
            serviceNumber=str(each.get('serviceNo')),
            aes=str(each.get('aes')),
            mxSPrTxn=str(each.get('mxSPrTxn')),
            depTime=str(each.get('depTime')),
            isBPMapLinkShown=str(each.get('isBPMapLinkShown')),
            fromCityId=str(each.get('FromCityId')),
            param42=each.get('param42')
        )
        r.save()
        # break


def saveTrip():
    client = MongoClient("localhost", 27017)
    db = client.scrapping
    cursor = db.trip.find()

    for each in cursor:
        data = each.get('data')
        t = TripData(
            status=str(each.get('status')),
            defaultSorting=each.get('DefaultSorting'),
            amenitiesData=str(each.get('amenitiesData')),
            message=str(each.get('message'))
        )
        t.save()
        try:
            for singleData in data:
                try:
                    tsd = TripSingleData(
                        tripData=t,
                        DPList=singleData.get('DPLst'),
                        vt=str(singleData.get('vt')),
                        busType=str(singleData.get('BsTp')),
                        Tips=str(singleData.get('Tips')),
                        BsSvid=str(singleData.get('BsSvId')),
                        Sort=str(singleData.get('Sort')),
                        IsDPA=str(singleData.get('IsDPA')),
                        NSA=str(singleData.get('NSA')),
                        params42=singleData.get('param42'),
                        serviceName=str(singleData.get('serviceName')),
                        giry=str(singleData.get('Glry')),
                        RbPrefCode=str(singleData.get('RbPrefCode')),
                        WnSt=str(singleData.get('WnSt')),
                        DpTm=str(singleData.get('DpTm')),
                        IsAC=str(singleData.get('IsAc')),
                        IsNAc=str(singleData.get('IsNAc')),
                        RtId=str(singleData.get('RtId')),
                        IsSpF=str(singleData.get('IsSpF')),
                        IsSlpr=str(singleData.get('IsSlpr')),
                        serviceId=str(singleData.get('serviceId')),
                        FareList=singleData.get('FrLst'),
                        Ament=singleData.get('Ament'),
                        OpId=str(singleData.get('OpId')),
                        BPList=singleData.get('BPLst'),
                        IsMTE=str(singleData.get('IsMTE')),
                        Rtg=singleData.get('Rtg'),
                        IsBpDpSearch=str(singleData.get('IsBpDpSearch')),
                        jDur=str(singleData.get('jDur')),
                        isStr=str(singleData.get('IsStr')),
                        Tvs=str(singleData.get('Tvs')),
                        Cmpg=singleData.get('Cmpg'),
                        BsSt=str(singleData.get('BsSt')),
                        ArTm=str(singleData.get('ArTm'))
                    )
                    tsd.save()
                except:
                    pass
        except:
            pass
            # break
        # break















