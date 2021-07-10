from django.shortcuts import render, redirect
from .models import Form, Cuantovaser
import os
import folium
from .forms import SdcForm
from . import views
from geopy.geocoders import Nominatim
import geocoder



#Opcion 1, geocode address

"""
def home(request):

    address = Cuantovaser.get(address)
    location = geocoder.osm('27 Genova, Guadalajara')
    lat = location.lat
    lng =location.lng
    country = location.country
"""


#Opcion 2, geocode address


def home(request):

    address = Cuantovaser.get(address)
    url = 'http://localhost/nominatim/'

    g = geocoder.osm(address)

    if (bool(g.osm)==True):
        lon=g.osm['x']
        lat=g.osm['y']
        state=g.osm['addr:state']
        country=g.osm['addr:country']

        print (address,',',lat,',',lon,',',state,',',country)
    else:
        print ('address not found!')


    # folium

    m = folium.Map(width=800, height=500, location=[20.67937121,-103.36152288], zoom_start=15, tiles='cartodb positron')

    folium.Marker([lat, lon], tooltip='Click for more', popup=country).add_to(m)

    ## style
    """
    style_pacientes = {'color': '#228B22'}

    ## adding to view

    folium.GeoJson(os.path.join(shp_dir,'pacientes.geojson'),name='pacientes',style_function=lambda x:style_pacientes).add_to(m)

    folium.LayerControl().add_to(m)
    """

    ## exporting

    m= m._repr_html_()

    context = {'my_map': m}

    # rendering

    return render(request,'cta/home.html',context)


def process_form(nombre, apellido, edad, domicilio, interpretacion, calle, numero, colonia, municipio, urgente, nombre_2, apellido_2, celular):
    form = Form(
    nombre=nombre,
    apellido=apellido,
    edad=edad,
    interpretacion=interpretacion,
    domicilio =domicilio,
    calle=calle,
    numero=numero,
    colonia=colonia,
    municipio=municipio,
    urgente=urgente,
    nombre_2=nombre_2,
    apellido_2=apellido_2,
    celular=celular,
    )
    form.save()
   
    return


def add_user(request):
    if "POST" in request.method:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        edad = request.POST.get("edad")
        interpretacion = request.POST.get("interpretacion")
        domicilio = request.POST.get("domicilio")
        calle = request.POST.get("calle")
        numero = request.POST.get("numero")
        colonia = request.POST.get("colonia")
        municipio = request.POST.get("municipio")
        urgente = request.POST.get("urgente")
        nombre_2 = request.POST.get("nombre_2")
        apellido_2 = request.POST.get("apellido_2")
        celular = request.POST.get("celular")

        process_form(nombre, apellido, edad, interpretacion, domicilio, calle, numero, colonia, municipio, urgente, nombre_2, apellido_2, celular)

        return redirect("/")

    return render(request, "cta/add_user.html")



