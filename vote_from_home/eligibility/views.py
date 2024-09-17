from django.http import HttpResponse

def check_eligibility(request, age):
    threshold_age = 60
    age = int(age)
    if age < threshold_age:
        difference = threshold_age - age
        message = f"You cannot avail Vote from Home as you are {difference} years younger than the threshold age."
    else:
        difference = age - threshold_age
        message = f"You are eligible for Vote from Home as you exceed {difference} years than the threshold age."
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vote from Home Eligibility</title>
    </head>
    <body>
        <h5>NAME:BHARATH N C</h5>
    <h5>USN:-1DT22IS404</h5>
        <h1>Vote from Home Eligibility</h1>
        <p>{message}</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
