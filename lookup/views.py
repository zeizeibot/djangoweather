#Tämä on minun views.py tiedosto
from django.shortcuts import render

def home(request):
	import json
	import requests
	from requests_html import HTMLSession

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		s = HTMLSession()
		query = 'pikku huopalahti'
		url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{zipcode}'
		r = s.get(url)
		temp = r.html.find('span#wob_tm', first = True).text
#		temp = r.html.find('span#wob_tm', first = True).text		
		unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
		desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
#		category_color = "kylma"
		uus_temp = int(temp)
		
#		try:
#			session = HTMLSession()
#			response = session.get(url)
     
#		except requests.exceptions.RequestException as e:
#			response = "Error..."

	
#		api_request = requests.get("https://www.google.fi/search?q=s%C3%A4%C3%A4" + zipcode)
#		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=B232817F-BCAE-4762-8FD4-4C851B1FEDBA")
		
#		try:
#			api = json.loads(api_request.content)
#		except Exception as e:
#			api = "Error..."

		if  uus_temp < 32:
			category_description = "(<- 0) Kantsii alkaa miettii pitkii jussei"								#"(0 - 50)  Ilmanlaatu on tyydyttävä, ja ilmansaasteet aiheuttavat vain vähän tai ei lainkaan riskiä."
			category_color = "kylma"
			lampotila = uus_temp
			cels = unit
			olosuhde = desc
			paikka = zipcode

		elif uus_temp > 32:
			category_description = "(0 ->)	No nyt on lämmin, ei muutaku shortsit päälle"
			category_color = "good"
			lampotila = uus_temp
			cels = unit
			olosuhde = desc
			paikka = zipcode


#		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":	 	
#	  		category_description = "(101 -150) Herkkien ryhmien jäsenillä voi olla terveysvaikutuksia. Se vaikuttaa vähemmän todennäköisesti suuriin yleisöihin."
#	  		category_color = "usg"
#		elif api[0]['Category']['Name'] == "Unhealthy":
#			category_description = "(151-200) Joillakin kansalaisilla voi olla terveysvaikutuksia; herkkien ryhmien jäsenillä voi olla vakavampia terveysvaikutuksia."
#			category_color = "unhealthy"
#		elif api[0]['Category']['Name'] == "Very Unhealthy":
#			category_description = "(201-300) Terveyshälytys: Terveysvaikutusten riski kasvaa kaikille."
#			category_color = "veryunhealthy"
#		elif api[0]['Category']['Name'] == "Hazardous":
#	  		category_description = "(301 ->)	Terveysvaroitus poikkeusoloista: vaikuttaa todennäköisemmin kaikkiin."
#	  		category_color = "hazardous"

	  	 
	  	 
		return render(request, 'home.html', {'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})
#		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})



	else:

#		api_request = requests.get("https://www.google.fi/search?q=s%C3%A4%C3%A4")
#		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=B232817F-BCAE-4762-8FD4-4C851B1FEDBA")
		s = HTMLSession()
		query = 'Helsinki'
		url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{query}'
#		url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{query}'
		r = s.get(url)
#		temp = r.html.find('a.wob_t', first = True).text
		temp = r.html.find('span#wob_tm', first = True).text
		unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
		desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
		uus_temp = int(temp)
		if temp =='°Fahrenheit':
			
			unit=(unit-32)*5/9
			temp= '°C'
			
#		try:
#			api = json.loads(api_request.content)
#		except Exception as e:
#			api = "Error..."

		elif uus_temp < 32:
			category_description =	"(<- 0) Kantsii alkaa miettii pitkii jussei"
			category_color = "kylma"
			lampotila = uus_temp
			cels = unit
			olosuhde = desc
			paikka = query

		elif uus_temp > 32:
			category_description = "(0 ->)	No nyt on lämmin, ei muutaku shortsit päälle"
			category_color = "good"
			lampotila = uus_temp
			cels = unit
			olosuhde = desc
			paikka = query
#		elif api[0]['Category']['Name'] == "Moderate":
#			category_description = "(51 - 100)	Ilmanlaatu on hyväksyttävää. Joillekin ihmisille, erityisesti niille, jotka ovat epätavallisen herkkiä ilmansaasteille, voi kuitenkin olla riski."
#			category_color = "moderate"
#		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":	 	
#	  		category_description = "(101 -150) Herkkien ryhmien jäsenillä voi olla terveysvaikutuksia. Se vaikuttaa vähemmän todennäköisesti suuriin yleisöihin."
#	  		category_color = "usg"
#		elif api[0]['Category']['Name'] == "Unhealthy":
#			category_description = "(151-200) Joillakin kansalaisilla voi olla terveysvaikutuksia; herkkien ryhmien jäsenillä voi olla vakavampia terveysvaikutuksia."
#			category_color = "unhealthy"
#		elif api[0]['Category']['Name'] == "Very Unhealthy":
#			category_description = "(201-300) Terveyshälytys: Terveysvaikutusten riski kasvaa kaikille."
#			category_color = "veryunhealthy"
#		elif api[0]['Category']['Name'] == "Hazardous":
#	  		category_description = "(301 ->)	Terveysvaroitus poikkeusoloista: vaikuttaa todennäköisemmin kaikkiin."
#	  		category_color = "hazardous"

	  	 
	  	 

		return render(request, 'home.html', {'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})


def about(request):
	return render(request, 'about.html', {})

