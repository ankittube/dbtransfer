from __future__ import unicode_literals

from django.db import models
# psycopg2.extras.register_json(oid=3802, array_oid=3807, globally=True)
from django.contrib.postgres.fields import JSONField, ArrayField, HStoreField
from django.core.validators import MinValueValidator

# Create your models here.



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class City(BaseModel):
    name = models.CharField(max_length=500, blank=True, null=True)
    cityid = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    zone = models.CharField(max_length=500, blank=True, null=True)


class TripData(BaseModel):
    status = models.CharField(max_length=500, blank=True, null=True)
    defaultSorting = models.CharField(max_length=500, blank=True, null=True)
    amenitiesData = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)


class TripSingleData(BaseModel):
    tripData = models.ForeignKey(TripData)
    DPList = JSONField(null=True)
    vt = models.CharField(max_length=500, blank=True, null=True)
    busType = models.CharField(max_length=500, blank=True, null=True)
    Tips = models.CharField(max_length=500, blank=True, null=True)
    BsSvid = models.CharField(max_length=500, blank=True, null=True)
    Sort = models.CharField(max_length=500, blank=True, null=True)
    IsDPA = models.CharField(max_length=500, blank=True, null=True)
    NSA = models.CharField(max_length=500, blank=True, null=True)
    params42 = JSONField(null=True)
    serviceName = models.CharField(max_length=500, blank=True, null=True)
    giry = models.CharField(max_length=500, blank=True, null=True)
    RbPrefCode = models.CharField(max_length=500, blank=True, null=True)
    WnSt = models.CharField(max_length=500, blank=True, null=True)
    DpTm = models.CharField(max_length=500, blank=True, null=True)
    IsAC = models.CharField(max_length=500, blank=True, null=True)
    RtId = models.CharField(max_length=500, blank=True, null=True)
    IsNAc = models.CharField(max_length=500, blank=True, null=True)
    IsSpF = models.CharField(max_length=500, blank=True, null=True)
    IsSlpr = models.CharField(max_length=500, blank=True, null=True)
    serviceId = models.CharField(max_length=500, blank=True, null=True)
    FareList = JSONField(null=True)
    Ament = JSONField(null=True)
    OpId = models.CharField(max_length=500, blank=True, null=True)
    BPList = JSONField(null=True)
    IsMTE = models.CharField(max_length=500, blank=True, null=True)
    Rtg = JSONField(null=True)
    IsBpDpSearch = models.CharField(max_length=500, blank=True, null=True)
    jDur = models.CharField(max_length=500, blank=True, null=True)
    isStr = models.CharField(max_length=500, blank=True, null=True)
    Tvs = models.CharField(max_length=500, blank=True, null=True)
    Cmpg = JSONField(null=True)
    BsSt = models.CharField(max_length=500, blank=True, null=True)
    ArTm = models.CharField(max_length=500, blank=True, null=True)


class RouteData(BaseModel):
    depTimeString = models.CharField(max_length=500, blank=True, null=True)
    maxUpperColumns = models.CharField(max_length=500, blank=True, null=True)
    fromCity = models.CharField(max_length=100,null=True, blank=True)
    maxLowerColumns = models.CharField(max_length=500, blank=True, null=True)
    maxLowerRows = models.CharField(max_length=500, blank=True, null=True)
    DPInformationList = JSONField(null=True)
    toCity = models.CharField(max_length=500, blank=True, null=True)
    maxUpperRows = models.CharField(max_length=500, blank=True, null=True)
    vehicleType = models.CharField(max_length=500, blank=True, null=True)
    BPInformationList = JSONField(null=True)
    travelDate = models.CharField(max_length=500, blank=True, null=True)
    busType = models.CharField(max_length=500, blank=True, null=True)
    MPax = models.CharField(max_length=500, blank=True, null=True)
    serviceName = models.CharField(max_length=500, blank=True, null=True)
    seatList = JSONField(null=True)
    toCityId = models.CharField(max_length=500, blank=True, null=True)
    operatorId = models.CharField(max_length=500, blank=True, null=True)
    amenities = models.CharField(max_length=500, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    dateOFJourney = models.CharField(max_length=500, blank=True, null=True)
    routeId = models.CharField(max_length=500, blank=True, null=True)
    travels = models.CharField(max_length=500, blank=True, null=True)
    arrTime = models.CharField(max_length=500, blank=True, null=True)
    arrTimeString = models.CharField(max_length=500, blank=True, null=True)
    serviceNumber = models.CharField(max_length=500, blank=True, null=True)
    aes = models.CharField(max_length=500, blank=True, null=True)
    mxSPrTxn = models.CharField(max_length=500, blank=True, null=True)
    depTime = models.CharField(max_length=500, blank=True, null=True)
    isBPMapLinkShown = models.CharField(max_length=500, blank=True, null=True)
    fromCityId = models.CharField(max_length=500, blank=True, null=True)
    param42 = JSONField(null=True)
