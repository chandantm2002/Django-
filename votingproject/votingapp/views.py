from django.shortcuts import render

def voting_data(request):
    states = ["RAICHUR", "CHITRADURG", "RAMANAGARA", "TUMKUR","YADGIRI"]
    voting_percentages = [83, 70, 92, 78, 86 ]
    data = zip(states, voting_percentages)
    return render(request, 'votingapp/voting_data.html', {'data': data})
