import json
import operator
from urllib import quote
import urllib2
from transferdb.models import *
import xlwt
from django.db.models import Q
import xlrd

def tvs_opid():
    travels = TripSingleData.objects.values("Tvs", "OpId").distinct()



    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
    style = xlwt.easyxf('font: bold True;')
    sheet.write(0, 0, "Id", style=style)
    sheet.write(0, 1, "Name", style=style)

    i = 0
    for t in travels:
        name = t["Tvs"]
        id = t["OpId"]
        i = i+1
        sheet.write(i, 0, id)
        sheet.write(i, 1, name)

    try:
        book.save("Travels.xls")
        print "Done"
    except:
        print "Error in saving"


def test():
    p = RouteData.objects.filter(fromCity__icontains="mumbai", toCity__icontains="pune").distinct()
    for i in p:
        s = i.serviceNumber
        c = RouteData.objects.filter(serviceNumber=s).count()
        print s, c


def all_cities():
    c = RouteData.objects.all().values_list("toCity", flat=True)
    c1 = RouteData.objects.all().values_list("fromCity", flat=True)
    c2= list(c)+list(c1)
    ci = list(set(list(c2)))
    return ci

def test2():

    cities = all_cities()
    service_count = []
    print "--"
    for i, city in enumerate(cities):

        count_from = RouteData.objects.filter(Q(fromCity__iexact=city)).values("serviceNumber").distinct().count()
        count_to = RouteData.objects.filter(Q(toCity__iexact=city)).values("serviceNumber").distinct().count()
        count = RouteData.objects.filter(Q(fromCity__iexact=city)|Q(toCity__iexact=city)).values("serviceNumber").distinct().count()
        print i, count, city
        service_count.append([city, count_from, count_to, count])

    print "--"
    print sorted(service_count, key=lambda x: x[3])


    # # sorted_x = sorted(service_count, key=service_count.get, reverse=True)
    #
    # for x in sorted_x:
    #     print x, service_count[x]


def get_state(cityname):
    key = 'AIzaSyBzBbJeeecA1eSGlzFZhxHYZw9QGILG2Po'
    url = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?' + \
          'input=' + quote(cityname + ' India', safe='') + \
          '&types=' + '(cities)' \
          + '&language=' + 'en' + \
          '&key=' + key

    # print url

    json_string_autocomplete = urllib2.urlopen(url)
    string_response_autocomplete = json_string_autocomplete.read().decode('utf-8')
    response_json_autocomplete = json.loads(string_response_autocomplete)
    if response_json_autocomplete['status'] == "OK":
        try:

            state = response_json_autocomplete['predictions'][0]['terms'][1]['value']
            print state
            return state

        except:
            print "ok"
            return "ok"
    else:
        print "not ok"
        return "not ok"


def create_cities():

    from_cities = RouteData.objects.all().values("fromCity", "fromCityId").distinct()
    to_cities = RouteData.objects.all().values("toCity", "toCityId").distinct()

    for k, i in enumerate(from_cities):
        print k
        city = i["fromCity"]
        id = i["fromCityId"]

        ci = City.objects.filter(cityid=id)
        if not ci:
            City(name=city, cityid=id).save()

    print "---------"

    for k, i in enumerate(to_cities):
        print k
        city = i["toCity"]
        id = i["toCityId"]

        ci = City.objects.filter(cityid=id)
        if not ci:
            City(name=city, cityid=id).save()

def dump_cities():

    cities = City.objects.all()

    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
    style = xlwt.easyxf('font: bold True;')
    sheet.write(0, 0, "CityId", style=style)
    sheet.write(0, 1, "Name", style=style)
    sheet.write(0, 2, "State", style=style)

    i = 0
    for t in cities:
        cityid = t.cityid
        name = t.name
        state = get_state(name)
        i = i+1
        sheet.write(i, 0, cityid)
        sheet.write(i, 1, name)
        sheet.write(i, 2, state)

    try:
        book.save("Cities.xls")
        print "Done"
    except:
        print "Error in saving"


def read_excel():
    book = xlrd.open_workbook("Cities.xls")
    first_sheet = book.sheet_by_index(0)

    num_rows = first_sheet.nrows
    num_col = first_sheet.ncols

    for row in range(num_rows):
        if row > 0:
            cityid = first_sheet.cell(row, 0).value
            name = first_sheet.cell(row, 1).value
            state = first_sheet.cell(row, 2).value
            zone = first_sheet.cell(row, 3).value

            print cityid, name, state, zone
            city = City.objects.get(cityid=cityid)
            city.state = state
            city.zone = zone
            city.save()
