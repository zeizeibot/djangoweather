#Tämä on minun views.py tiedosto
from django.shortcuts import render
from . import muuntaja
def home(request):
	import json
	import requests
	from requests_html import HTMLSession
	

	if request.method == "POST" and "GET":
		zipcode = request.POST['zipcode']
		s = HTMLSession()
		url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{zipcode}'
		r = s.get(url)
		

		try:
			
			temp = r.html.find('span#wob_tm', first = True).text
			
		except Exception:
			s = HTMLSession()
			query = 'Helsinki'
			url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{query}'
			r = s.get(url)
			temp = r.html.find('span#wob_tm', first = True).text
			unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
			desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
			uus_temp = int(temp)
			desc = muuntaja.muuttaja(desc)

			if unit == ('°Fahrenheit') or ('°F') :
				desc = muuntaja.muuttaja(desc)
				uus_temp = (uus_temp-32)*5/9
				uus_temp = int(uus_temp)
				unit = '°C'
				lampotila = uus_temp
				cels = unit
				olosuhde = desc
				paikka = query

				if uus_temp < 0:
					huuto = "!!! !!! !!!"
					virhe = "Nyt et antanu paikan nimee, mietippä uudestaa. Palautin sinut takaisin Helsinkiin."
					category_description = "(<- 0) Kantsii alkaa miettii pitkii jussei"
					category_color = "kylma"
					return render(request, 'home.html', {'huuto':huuto,'virhe': virhe,'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})

				elif uus_temp >= 0:
					huuto = "!!! !!! !!!"
					virhe = "Nyt et antanu paikan nimee, mietippä uudestaa. Palautin sinut takaisin Helsinkiin."
					category_description = "(0 ->) No nyt on lämmin, ei muutaku shortsit päälle"
					category_color = "good"
					return render(request, 'home.html', {'huuto':huuto,'virhe': virhe,'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})
		else:
			zipcode = request.POST['zipcode']
			s = HTMLSession()
			url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{zipcode}'
			r = s.get(url)
			temp = r.html.find('span#wob_tm', first = True).text
			unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
			desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
			uus_temp = int(temp)
			desc = muuntaja.muuttaja(desc)
		

			if unit == ('°Fahrenheit') or ('°F'):
				desc = muuntaja.muuttaja(desc)
				uus_temp = (uus_temp-32)*5/9
				uus_temp = int(uus_temp)
				unit = '°C'
				lampotila = uus_temp
				cels = unit
				olosuhde = desc
				paikka = zipcode
			
				if uus_temp < 0:
					category_description =	"(<- 0) Kantsii alkaa miettii pitkii jussei"
					category_color = "kylma"
					return render(request, 'home.html', {'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})
				elif uus_temp >= 0:
					category_description = "(0 ->)	No nyt on lämmin, ei muutaku shortsit päälle"
					category_color = "good"
					return render(request, 'home.html', {'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})
				
	
	else:

		s = HTMLSession()
		query = 'Helsinki'
		url = f'https://www.google.fi/search?q=s%C3%A4%C3%A4+{query}'
		r = s.get(url)
		temp = r.html.find('span#wob_tm', first = True).text
		unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
		desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
		uus_temp = int(temp)
		desc = muuntaja.muuttaja(desc)

		if unit == ('°Fahrenheit') or ('°F') :
			desc = muuntaja.muuttaja(desc)
			uus_temp = (uus_temp-32)*5/9
			uus_temp = int(uus_temp)
			unit = '°C'
			lampotila = uus_temp
			cels = unit
			olosuhde = desc
			paikka = query

			if uus_temp < 0:
				category_description =	"(<- 0) Kantsii alkaa miettii pitkii jussei"
				category_color = "kylma"
				

			elif uus_temp >= 0:
				category_description = "(0 ->)	No nyt on lämmin, ei muutaku shortsit päälle"
				category_color = "good"

	  	 
		return render(request, 'home.html', {'category_description': category_description, 'category_color': category_color,'lampotila':lampotila, 'cels':cels, 'olosuhde':olosuhde, 'paikka':paikka})


def about(request):
	return render(request, 'about.html', {})

