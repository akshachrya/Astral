from flask import Flask,render_template
from astral import LocationInfo
from datetime import datetime
from astral.sun import sun

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
	orgdate='2018-03-04'
	cityinfo="Dallas"
	options='Aberdeen, Abu Dhabi, Abu Dhabi, Abuja, Accra, Addis Ababa, Adelaide, Al Jubail, Albany, Albuquerque, Algiers, Amman, Amsterdam, Anchorage, Andorra la Vella, Ankara, Annapolis, Antananarivo, Apia, Ashgabat, Asmara, Astana, Asuncion, Athens, Atlanta, Augusta, Austin, Avarua, Baghdad, Baku, Baltimore, Bamako, Bandar Seri Begawan, Bangkok, Bangui, Banjul, Barrow-In-Furness, Basse-Terre, Basseterre, Baton Rouge, Beijing, Beirut, Belfast, Belgrade, Belmopan, Berlin, Bern, Billings, Birmingham, Birmingham, Bishkek, Bismarck, Bissau, Bloemfontein, Bogota, Boise, Bolton, Boston, Bradford, Brasilia, Bratislava, Brazzaville, Bridgeport, Bridgetown, Brisbane, Bristol, Brussels, Bucharest, Bucuresti, Budapest, Buenos Aires, Buffalo, Bujumbura, Burlington, Cairo, Canberra, Cape Town, Caracas, Cardiff, Carson City, Castries, Cayenne, Charleston, Charlotte, Charlotte Amalie, Cheyenne, Chicago, Chisinau, Cleveland, Columbia, Columbus, Conakry, Concord, Copenhagen, Cotonou, Crawley, Dakar, Dallas, Damascus, Dammam, Denver, Des Moines, Detroit, Dhaka, Dili, Djibouti, Dodoma, Doha, Douglas, Dover, Dublin, Dushanbe, Edinburgh, El Aaiun, Fargo, Fort-de-France, Frankfort, Freetown, Funafuti, Gaborone, George Town, Georgetown, Gibraltar, Glasgow, Greenwich, Guatemala, Hanoi, Harare, Harrisburg, Hartford, Havana, Helena, Helsinki, Hobart, Hong Kong, Honiara, Honolulu, Houston, Indianapolis, Islamabad, Jackson, Jacksonville, Jakarta, Jefferson City, Jerusalem, Juba, Jubail, Juneau, Kabul, Kampala, Kansas City, Kathmandu, Khartoum, Kiev, Kigali, Kingston, Kingston, Kingstown, Kinshasa, Koror, Kuala Lumpur, Kuwait, La Paz, Lansing, Las Vegas, Leeds, Leicester, Libreville, Lilongwe, Lima, Lincoln, Lisbon, Little Rock, Liverpool, Ljubljana, Lome, London, Los Angeles, Louisville, Luanda, Lusaka, Luxembourg, Macau, Madinah, Madison, Madrid, Majuro, Makkah, Malabo, Male, Mamoudzou, Managua, Manama, Manchester, Manchester, Manila, Maputo, Maseru, Masqat, Mbabane, Mecca, Medina, Melbourne, Memphis, Mexico, Miami, Milwaukee, Minneapolis, Minsk, Mogadishu, Monaco, Monrovia, Montevideo, Montgomery, Montpelier, Moroni, Moscow, Moskva, Mumbai, Muscat, N’Djamena, Nairobi, Nashville, Nassau, Naypyidaw, New Delhi, New Orleans, New York, Newark, Newcastle, Newcastle Upon Tyne, Ngerulmud, Niamey, Nicosia, Norwich, Nouakchott, Noumea, Nuku’alofa, Nuuk, Oklahoma City, Olympia, Omaha, Oranjestad, Orlando, Oslo, Ottawa, Ouagadougou, Oxford, P’yongyang, Pago Pago, Palikir, Panama, Papeete, Paramaribo, Paris, Perth, Philadelphia, Phnom Penh, Phoenix, Pierre, Plymouth, Podgorica, Port Louis, Port Moresby, Port of Spain, Port-Vila, Port-au-Prince, Portland, Portland, Porto-Novo, Portsmouth, Prague, Praia, Pretoria, Pristina, Providence, Quito, Rabat, Raleigh, Reading, Reykjavik, Richmond, Riga, Riyadh, Road Town, Rome, Roseau, Sacramento, Saint Helier, Saint Paul, Saint Pierre, Saipan, Salem, Salt Lake City, San Diego, San Francisco, San Jose, San Juan, San Marino, San Salvador, Sana, Sana’a, Santa Fe, Santiago, Santo Domingo, Sao Tome, Sarajevo, Seattle, Seoul, Sheffield, Singapore, Sioux Falls, Skopje, Sofia, Southampton, Springfield, Sri Jayawardenapura Kotte, St. George’s, St. John’s, St. Peter Port, Stanley, Stockholm, Sucre, Suva, Swansea, Swindon, Sydney, T’bilisi, Taipei, Tallahassee, Tallinn, Tarawa, Tashkent, Tbilisi, Tegucigalpa, Tehran, Thimphu, Tirana, Tirane, Tokyo, Toledo, Topeka, Torshavn, Trenton, Tripoli, Tunis, Ulaanbaatar, Ulan Bator, Vaduz, Valletta, Vienna, Vientiane, Vilnius, Virginia Beach, W. Indies, Warsaw, Washington DC, Wellington, Wichita, Willemstad, Wilmington, Windhoek, Wolverhampton, Yamoussoukro, Yangon, Yaounde, Yaren, Yerevan, Zagreb'
	cities=options.split(",")
	city = LocationInfo(cityinfo)
	timezone = city.timezone
	long = city.longitude
	lat = city.latitude
	date=datetime.strptime(orgdate, "%Y-%m-%d")
	suns=sun(city.observer, date=date)
	dawn=suns['dawn'].strftime("%H:%M:%S")
	sunrise=suns['sunrise'].strftime("%H:%M:%S")
	sunset=suns['sunset'].strftime("%H:%M:%S")
	dusk=suns['dusk'].strftime("%H:%M:%S")
	noon=suns['noon'].strftime("%H:%M:%S")
	table1={'city':city.name,'region':city.region,'timezone':timezone,'long':long,'lat':lat}
	table2={'date':orgdate,'dawn':dawn,'sunrise':sunrise,'sunset':sunset,'dusk':dusk,'noon':noon}
	return render_template('home.html',cities=cities,table1=table1,table2=table2)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

