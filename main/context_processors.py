from .models import news
from .forms import messageForm

def include(request):
    error = ''
    if request.method == 'POST':
        form  = messageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Не верно введены данные'
    form = messageForm()
    new = news.objects.order_by('-date')
    return ({'news': new, 'form': form, 'error': error})
