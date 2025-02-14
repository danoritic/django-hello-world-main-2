from datetime import datetime

from django.http import HttpResponse,JsonResponse

def family_view(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel's {family_view}!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    # return HttpResponse(html)
    return JsonResponse({"data":"atad","special":"yoruba atata"})
# def family_view(request):
