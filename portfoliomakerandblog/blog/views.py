from django.shortcuts import render,get_object_or_404
from django . http import HttpResponse
from . models import Blog
# Create your views here.
def all_blogs(request):
    blog=Blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blog})
def detail(request,blog_id):# aisa likhne se request aygi with id 
    blog=get_object_or_404(Blog, pk=blog_id)#agr data h to send else 404 error means not found
    return render(request,'blog/details.html',{'blog':blog})


'''

                        #pk means primary kry use for id in the database
QUESTION_DESC=models.TextField(max_length=300,null=False,blank=True)
    def AddExam(request):
    
    global exam_id
    global admin_name
    global adminid
    global consec
    global aconsec
    global image_url
    consec=False
    aconsec=False

    if request.session.has_key('lca'):# it is true when user is logged in. other wise the dash board will not be opened
        request.session.set_expiry(2400) # i.e 40 minutes
        admin_name=request.session.get('admin_name','unknown')    
        adminid=request.session.get('adminid','unknown')
        aconsec=False
        if request.POST: # if add exam button is clicked validate the value and store in the database.
            return validate_add_exam(request)

        else:
            # it display a page with the fields of entering the exam details such as examid,examname...etc.
            exam_id='0' # same goes here. i mean reseting
            gd=[]# getting all exam ids w.r.t studid
            leid=len(list(GROUP_SUPER_ADMIN.objects.filter(ADMINID=adminid)))
            for i in range(leid):
                l2=str(list(GROUP_SUPER_ADMIN.objects.filter(ADMINID=adminid))[i])
                ml2=l2.split(';;')
                gd.append(ml2)
            #print(gd)
            return render(request, 'login/admin/main-add-exam.html',{'admin_name':admin_name,'gd':gd})
    
    else:
        return redirect('/asp/login/')






        def AddQuestions(request, *args, **kwargs):
    
    global exam_id
    global admin_name
    global adminid
    global consec
    global aconsec
    #print(request.session.session_key)
    consec=False

    if request.session.has_key('lca'):

        global ques
        request.session.set_expiry(2400) # i.e 40 minutes
        admin_name=request.session.get('admin_name','unknown')    
        adminid=request.session.get('adminid','unknown')
        
        if exam_id!='0':# initialy exami_id will be '0' suppose. if admin adds the examid then it changed and then inner part will be executed. so basically user should not access the add question part before add ing exam id. so this condition checnks that
            
            if request.POST: # if exam id is added and question detials also add then validate
                
                #aconsec=False
                return validate_add_questions(request, *args, **kwargs)
            
            elif aconsec==True:
                
                mysec=kwargs['i']
                
                if mysec=='all':
                    
                    ques=[]
                    mylen=len(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id)))
                    
                    for i in range(mylen):
                       
                        l=str(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id))[i])
                        ml=l.split(';;')
                        ques.append(ml)
                    
                    return render(request,'login/admin/add-question.html',{'ques':ques,'admin_name':admin_name})
                
                elif mysec=='A':
                    
                    #print("A")
                    mques=[]
                    mylen=len(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec)))
                    
                    for i in range(mylen):
                        
                        l=str(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec))[i])
                        ml=l.split(';;')
                        mques.append(ml)
                    
                    return render(request,'login/admin/add-question.html',{"ques":mques,'admin_name':admin_name})
                    #return HttpResponse("A")
                
                elif mysec=='B':
                    
                    mques=[]
                    mylen=len(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec)))
                    
                    for i in range(mylen):
                     
                        l=str(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec))[i])
                        ml=l.split(';;')
                        mques.append(ml)
                    
                    return render(request,'login/admin/add-question.html',{"ques":mques,'admin_name':admin_name})
                    #return HttpResponse("B")
                
                elif mysec=='C':
                    
                    mques=[]
                    mylen=len(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec)))
                    
                    for i in range(mylen):
                       
                        l=str(list(QUESTION.objects.filter(ADMINID=adminid,EXAMID=exam_id,SECTION=mysec))[i])
                        ml=l.split(';;')
                        mques.append(ml)
                    
                    return render(request,'login/admin/add-question.html',{"ques":mques,'admin_name':admin_name})
                    #return HttpResponse("C")                   
                
                else:
                    return render(request, 'login/admin/add-question.html',{"ques":ques,'admin_name':admin_name})
            
            else:
                aconsec=True
                return render(request, 'login/admin/add-question.html',{"ques":ques,'admin_name':admin_name})        
        
        else:

            return redirect('/asp/login/AdminDashboard/AddExam')
    
    else:
        return redirect('/asp/login/')
'''