from django.shortcuts import render
import requests
from munch import munchify
from datetime import datetime

# Create your views here.
def index (request):
    return render(request, 'rover_app/rover.html')

def meet (request):
    return render(request, 'rover_app/meet.html')

def about (request):
    return render(request, 'rover_app/about.html')


def results (request):
    api_key = 'KMYa9fgdIMxNz8nghVBlfqg49hiPG55Jy0w5yuO5'
    search_date = request.POST.get('search-date')
    datetime_search_date = datetime.strptime(search_date, '%Y-%m-%d')
    filter_rover = request.POST.getlist('filter-rover')
    filter_camera = request.POST.getlist('filter-camera')
    
    # for what shows up in the dropdown filter menu
    if len(filter_rover) == 3:
        filter_rover_string = "All Rovers"
    else:
        filter_rover_string = ", ".join(filter_rover)
        
    if len(filter_camera) == 1:
        filter_camera_string = filter_camera[0]
    elif len(filter_camera) == 9:
        filter_camera_string = "ALL CAMERAS"
    else:
        filter_camera_string = str(len(filter_camera)) + " Selected"
    
    all_photos = []

    # loop through every rover specified
    if filter_rover:
        rover_loop = filter_rover
    else:
        rover_loop = ['Curiosity', 'Opportunity', 'Spirit']
    for rover in rover_loop:
        new_results = True
        page = 1
        #loop through every page of results
        while new_results:
            url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={search_date}&page={page}&api_key={api_key}'
            response = requests.get(url).json()
            new_results = response.get('photos', [])
            all_photos.extend(new_results)
            page += 1

    #turn each photo-dict values into attributes using munch
    #because django templates doesn't allow access to dictionary values easily
    munchified_photos = []
    for photo in all_photos:
        munchified_photos.append(munchify(photo))

    #check if there's a camera filter and remove photos that aren't relevant
    if filter_camera:
        munchified_photos = list(filter(lambda x: x.camera.name in filter_camera, munchified_photos))



    context = {
        'search_date':search_date,
        'datetime_search_date': datetime_search_date,
        "filter_rover":filter_rover,
        "filter_rover_string":filter_rover_string,
        "filter_camera":filter_camera,
        "filter_camera_string":filter_camera_string,
        "all_photos":munchified_photos
    }

    return render(request, 'rover_app/results.html', context)


def photo (request, photo_date, photo_id,):
    api_key = 'KMYa9fgdIMxNz8nghVBlfqg49hiPG55Jy0w5yuO5'
    all_photos = []

    for rover in ['Curiosity', 'Opportunity', 'Spirit']:
        new_results = True
        page = 1
        #loop through every page of results
        while new_results:
            url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={photo_date}&page={page}&api_key={api_key}' 
            response = requests.get(url).json()
            new_results = response.get('photos', [])
            all_photos.extend(new_results)
            page += 1

    #Munch provides attribute-style access (a la JavaScript objects) for Python dict objects.
    munchified_photos = []
    for photo in all_photos:
        munchified_photos.append(munchify(photo))
    
    individual_photo = list(filter(lambda x: x.id == int(photo_id), munchified_photos))[0]
    
    individual_photo_date = datetime.strptime(individual_photo.earth_date, '%Y-%m-%d')

    return render(request, 'rover_app/photo.html', {"individual_photo":individual_photo, 'individual_photo_date':individual_photo_date})
