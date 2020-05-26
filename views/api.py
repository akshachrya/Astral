from flask import Flask,render_template,request,Blueprint
from astral import LocationInfo
from astral.sun import sun
from astral.geocoder import database, lookup
from datetime import datetime,timedelta
import json
import pytz

api=Blueprint('api',__name__)

@api.route('/send',methods=['POST','GET'])
def send():
	if request.method=='POST':
		data=request.json
		startdate=datetime.strptime(data['date'],'%Y-%m-%d')
		enddate=datetime.strptime(data['date1'],'%Y-%m-%d')
		cityinfo=data['city']
		city=lookup(cityinfo, database())
		day = timedelta(days=1)
		table2=[]
		while startdate <= enddate:
			suns=sun(city.observer, date=startdate, tzinfo=pytz.timezone(city.timezone))
			dawn=suns['dawn'].strftime("%H:%M:%S")
			sunrise=suns['sunrise'].strftime("%H:%M:%S")
			sunset=suns['sunset'].strftime("%H:%M:%S")
			dusk=suns['dusk'].strftime("%H:%M:%S")
			noon=suns['noon'].strftime("%H:%M:%S")
			table2.append({'date':startdate.strftime('%Y-%m-%d'),'dawn':dawn,'sunrise':sunrise,'sunset':sunset,'dusk':dusk,'noon':noon})
			startdate=startdate+day
		table1={'city':city.name,'region':city.region,'timezone':city.timezone,'long':round(city.longitude,2),'lat':round(city.latitude,2)}
		return json.dumps({'table1':table1,'table2':table2})