from flask import Flask,render_template,request,Blueprint
from astral import LocationInfo
from datetime import datetime
from astral.sun import sun
from astral.geocoder import database, lookup
import json
import pytz

api=Blueprint('api',__name__)

@api.route('/send',methods=['POST','GET'])
def send():
	if request.method=='POST':
		data=request.json
		orgdate=data['date']
		cityinfo=data['city']
		city=lookup(cityinfo, database())
		date=datetime.strptime(orgdate, "%Y-%m-%d")
		suns=sun(city.observer, date=date, tzinfo=pytz.timezone(city.timezone))
		dawn=suns['dawn'].strftime("%H:%M:%S")
		sunrise=suns['sunrise'].strftime("%H:%M:%S")
		sunset=suns['sunset'].strftime("%H:%M:%S")
		dusk=suns['dusk'].strftime("%H:%M:%S")
		noon=suns['noon'].strftime("%H:%M:%S")
		table1={'city':city.name,'region':city.region,'timezone':city.timezone,'long':city.longitude,'lat':city.latitude}
		table2={'date':orgdate,'dawn':dawn,'sunrise':sunrise,'sunset':sunset,'dusk':dusk,'noon':noon}
		return json.dumps({'table1':table1,'table2':table2})