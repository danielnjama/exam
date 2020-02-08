from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, permission_required
from results.models import final_results
from django.contrib.auth.models import AnonymousUser, User


# Create your views here.
def index(request):
    results = final_results.objects.all()
    return render(request,'english.html',{'results':results})

#@login_required(login_url="accounts/login/")
def get_marks(request):
    q1=request.POST.get('q1','')
    q2=request.POST.get('q2','')
    q3=request.POST.get('q3','')
    q4=request.POST.get('q4','')
    q5=request.POST.get('q5','')
    q6=request.POST.get('q6','')
    q7=request.POST.get('q7','')
    q8=request.POST.get('q8','')
    q9=request.POST.get('q9','')
    q10=request.POST.get('q10','')


    
     
    if q1 and q2 and q3 and q4 and q5 and q6 and q7 and q8 and q9 and q10:
        try:
            if q1 == 'A':
                m1=1
                comment=True
            else:
                m1=0
            
            if q2 == 'D':
                m2=1
                comment=True
            else:
                m2=0
            if q3 == 'B':
                m3=1
                comment=True
            else:
                m3=0

            if q4 == 'D':
                m4=1
                comment=True
            else:
                m4=0

            if q5 == 'D':
                m5=1
                comment=True
            else:
                m5=0

            if q6 == 'C':
                m6=1
                comment=True
            else:
                m6=0
            if q7 == 'B':
                m7=1
                comment=True
            else:
                m7=0
            if q8 == 'D':
                m8=1
                comment = True
            else:
                m8=0

            
            if q9 == 'C':
                m9=1
                comment=True
            else:
                m9=0
            

            if q10 == 'C':
                m10=1
                comment=True
            else:
                m10=0
            
            total_marks = m1+m2+m3+m4+m5+m6+m7+m8+m9+m10

            if total_marks >=8:
                message ='Congraturations!!'
            elif total_marks>=5:
                message ='Keep up!'
            else:
                message ='Work harder!'

            percentage = total_marks *10
            percentage = str(round(percentage,2))
            results = final_results.objects.all()

            candidate = request.user
            if final_results.objects.filter(name=candidate).exists():
                message=True
                return render(request,'results.html',{'results':results,'message':message})
            else:
                data = final_results(name=candidate,marks=total_marks,percentage=percentage,comment=message)
                data.save()
                
                context={
                    'total_marks':total_marks,
                    'percentage':percentage,
                    'message': message,
                    'results': results
                    


                }


                

                return render(request,'results.html',context)
        except:
            raise ValidationError('Make sure all the fields are selected')
    
    else:
        message='Make sure all the questions are attempted! \n Refresh or go back to continue selecting your answers'
        return render(request,'english.html',{'message':message})
