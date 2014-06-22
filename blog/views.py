from django.shortcuts import render_to_response
from blog.models import User
# Create your views here.
def index(req):
  emps = User.objects.all()
  return render_to_response('index.html',{'emps':emps})