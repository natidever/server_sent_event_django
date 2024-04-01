from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import User
event_queue = []
def user_creation(request):
    if request.method == 'POST':
        # Assuming the request contains user data
        user_data = request.POST
        new_user = User.objects.create(name=user_data['name'], email=user_data['email'])
        # Add an event to the queue
        event_queue.append("hello")
        return HttpResponse('User created\n')
    else:
        return HttpResponse('Method not allowed\n', status=405)
    
    
    
from django.http import StreamingHttpResponse
import time

# Simulate a global event queue
event_queue = []

def stream_updates(request):
    def event_stream():
        while True:
            if event_queue:
                # Pop the first event from the queue
                event = event_queue.pop(0)
                # Yield the event as a Server-Sent Event
                yield f"data: {event}\n\n"
            else:
                # Wait for a short period before checking the queue again
                time.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


