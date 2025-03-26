from django.shortcuts import render , HttpResponse,get_object_or_404,redirect
from .models import Resume, Certificate, BlogPost


#certificate
def home(request):
    return render(request,'index.html')
    # return HttpResponse("hello im shweta")
def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def certificate(request):
    certificates= Certificate.objects.all()
    return render(request,'certificate.html',{'certificate':certificates})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})

def delete_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, id=cert_id)
    if request.method == 'POST':
        cert.delete()
        return redirect('certificate')

def blog(request):
    blogs=BlogPost.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def blog_details(request,title):
    blog=get_object_or_404(BlogPost,title=title)
    return render(request,'blog_detail.html',{'blog':blog})
