from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from students.models import Student
# Create your views here.
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students = [{'name': s.name, 'id': s.id} for s in students]

        return JsonResponse(students, safe=False)
    if request.method == 'POST':
        name = request.POST.get('name')
        student = Student(name=name)
        student.save()

        context = {
            'code': 200,
            'msg': 'post success!'
        }
        return JsonResponse(context)
        
