from django.http import HttpResponse
import datetime
import os
import pwd  # Import this to get username by UID
import subprocess

def htop(request):
    name = "Saikeerthan Suthraye"  # Replace with your full name
    try:
        username = pwd.getpwuid(os.geteuid()).pw_name
    except KeyError:
        username = "unknown"  # Fallback if username can't be determined

    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    response = f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
