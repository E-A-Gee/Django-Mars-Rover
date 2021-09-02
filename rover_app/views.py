from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='POST':
        search_date = request.POST.get('search-date')
        if search_date:
            context = {'search_date':search_date}
            return render(request, 'rover_app/rover.html', context)
    return render(request, 'rover_app/rover.html')

    