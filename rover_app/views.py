from django.shortcuts import render
import requests
from munch import munchify

# Create your views here.
def index(request):
    
    if request.method=='POST':

        api_key = 'KMYa9fgdIMxNz8nghVBlfqg49hiPG55Jy0w5yuO5'
        search_date = request.POST.get('search-date')
        
        all_photos = []

        # loop through every rover
        for rover in ['curiosity', 'opportunity', 'spirit']:
            new_results = True
            page = 1
            #loop through every page of results
            while new_results:
                url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={search_date}&page={page}&api_key={api_key}'   
                response = requests.get(url).json()
                new_results = response.get('photos', [])
                all_photos.extend(new_results)
                page += 1

        munchified_photos = []

        for photo in all_photos:
            munchified_photos.append(munchify(photo))


        context = {'search_date':search_date, "all_photos":munchified_photos}
        return render(request, 'rover_app/rover.html', context)

    return render(request, 'rover_app/rover.html')
    
  

    