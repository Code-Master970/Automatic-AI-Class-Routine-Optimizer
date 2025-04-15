from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .utils import save_periods_to_db  # Importing your utility function for saving periods
from .models import faculty, schedule, period

# Views for other pages
def Home(request):
    return render(request, "index.html")

def About(request):
    return render(request, "about.html")

# def Schedule(request):
#     return render(request, "schedule.html")

@login_required(login_url='/signup_or_login/')
def Today_schedule(request):
    return render(request, "today_schedule.html")

def create_periods_view(request):
    if request.method == "POST":
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        try:
            num_periods = int(request.POST.get('num_periods'))
            #save_periods_to_db(start_time, end_time, num_periods) 
            return HttpResponse("✅ Periods created successfully!")
        except ValueError as e:
             return HttpResponse(f"❌ Error: {str(e)}")
    
        return render(request, 'schedule.html')


from django.shortcuts import render
from .models import faculty, schedule, period
from django.db.models import Prefetch
from .models import day  
import datetime

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def schedule_view(request):
    selected_day = request.GET.get('day')

    # ✅ Default to today's day if not selected
    if not selected_day:
        today = datetime.datetime.today().strftime('%A')
        selected_day = today if today in DAYS else "Monday"

    try:
        selected_day_obj = day.objects.get(day_name__iexact=selected_day)
    except day.DoesNotExist:
        selected_day_obj = None

    # ✅ Prefetch only schedules for the selected day
    faculties = faculty.objects.prefetch_related(
        Prefetch(
            'schedules',
            queryset=schedule.objects.filter(day=selected_day_obj).select_related(
                'subject', 'section', 'room', 'period', 'day'
            ),
            to_attr='filtered_schedules'  # ⬅️ Custom attribute to access in template
        )
    ).all()

    periods = period.objects.order_by('period_number')
    
    return render(request, 'schedule.html', {
        'faculties': faculties,
        'periods': periods,
        'selected_day': selected_day,
        'days': DAYS,
    })

