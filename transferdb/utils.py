from transferdb.models import *
import xlwt

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


def test2():
    p =