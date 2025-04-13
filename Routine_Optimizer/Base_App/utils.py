
# from datetime import datetime, timedelta
# from .models import period 

# # Function to generate periods with start and end times
# def generate_periods(start_time_str, end_time_str, num_periods, break_period_number=5):
#     start_time = datetime.strptime(start_time_str, "%H:%M")
#     end_time = datetime.strptime(end_time_str, "%H:%M")

#     if end_time <= start_time:
#         raise ValueError("End time must be after start time.")

#     # Total available time in minutes
#     total_minutes = (end_time - start_time).seconds // 60
#     period_duration = total_minutes // num_periods  # Duration for each period

#     if period_duration == 0:
#         raise ValueError("Not enough time for the given number of periods.")

#     periods = []
#     current_start = start_time

#     for i in range(1, num_periods + 1):
#         current_end = current_start + timedelta(minutes=period_duration)
#         periods.append({
#             'period_number': i,
#             'start_time': current_start.strftime('%H:%M'),  # Format the start time
#             'end_time': current_end.strftime('%H:%M'),  # Format the end time
#             'is_break': (i == break_period_number)  # Mark if this is the break period
#         })
#         current_start = current_end

#     # Print all periods and count
#     for p in periods:
#         print(p)

#     print("Number of periods saved:", len(periods))  # To check how many periods were created

#     return periods


# # Function to save the generated periods to the database
# def save_periods_to_db(start_time, end_time, num_periods, break_period_number=5):
#     print("🔧 save_periods_to_db called with:", start_time, end_time, num_periods)
    
#     # Clear the existing periods from the DB
#     period.objects.all().delete()  
    
#     # Generate the periods based on the provided times
#     period_data = generate_periods(start_time, end_time, num_periods, break_period_number)

#     # Save the generated periods to the database
#     for data in period_data:
#         period.objects.create(
#             period_number=data['period_number'],
#             start_time=data['start_time'],
#             end_time=data['end_time'],
#             is_break=data['is_break']
#         )

#     print("🔧 Periods saved to DB successfully.")

