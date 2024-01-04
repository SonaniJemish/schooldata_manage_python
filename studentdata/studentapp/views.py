from django.shortcuts import render, redirect
from studentapp.models import Student,schooldetails,StdPresent
from django.contrib import messages

# this is for ondex section
def index(request):
    return render(request, "index.html")




# this portion is for student list and details

def studentform(request):
    schoollist = schooldetails.objects.all()
    context = {
        "schlist": schoollist,
    }

    if request.method == "POST":
        sname = request.POST.get('sname')
        sroll = request.POST.get('sroll')
        sgender = request.POST.get('sgender')
        sstandard = request.POST.get('sstandard')
        ssubject = request.POST.get('ssubject')
        scity = request.POST.get('scity')
        scid = request.POST.get('scid')
        sjoindate = request.POST.get('sjoindate')
        sschool = schooldetails.objects.get(id=scid)
        student = Student(sname=sname, sroll=sroll, sgender=sgender, sstandard=sstandard, ssubject=ssubject, scity=scity, scid=sschool,sjoindate=sjoindate)
        student.save()
        messages.success(request, "Hello, Student your data has been sent.")

    return render(request, "studentform.html", context)


def updatestd(request, id):
    if request.method == "POST":
        sname = request.POST.get('sname')
        sroll = request.POST.get('sroll')
        sgender = request.POST.get('sgender')
        sstandard = request.POST.get('sstandard')
        ssubject = request.POST.get('ssubject')
        scity = request.POST.get('scity')
        scid = request.POST.get('scid')
        stdupdate = Student.objects.get(id=id)
        stdupdate.sname=sname
        stdupdate.sroll=sroll
        stdupdate.sgender=sgender
        stdupdate.sstandard=sstandard
        stdupdate.ssubject=ssubject
        stdupdate.scity=scity
        schools = schooldetails.objects.get(id=scid)
        stdupdate.scid=schools

        stdupdate.save()
        messages.info(request, "Hello, Student yor data has been Updated.")

    stdup = Student.objects.get(id=id)
    schoollist = schooldetails.objects.all()
    schoolname = stdup.scid
    schoolid = schooldetails.objects.get(scname=schoolname)
    context = {
        "updatestd": stdup,
        "schlist": schoollist,
        "schoolid":schoolid,
    }
    return render(request, "updatestudent.html", context)


def delstudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.warning(request, "Hello, Student yor data has been Deleted.")
    return redirect('/viewstdlist')


def viewstdlist(request,scid,id):
    schooldet = schooldetails.objects.get(id=scid)
    standard = id
    stddetail =Student.objects.filter(sstandard=id,scid=scid).order_by('id')
    return render(request,"viewstdlist.html", {'stddetails':stddetail,'schooldet':schooldet,"standard":standard})


def stdschdetail(request,id):
    stddetail = Student.objects.get(id=id)
    schoolname = stddetail.scid
    schoolid = schooldetails.objects.get(scname=schoolname)
    return render(request,"stdfulldetails.html", {'stddetails':stddetail,'schoolnames':schoolname,'schoolid':schoolid})






#below portion is schools list and details

def schoolform(request):
    if request.method == "POST":
        scname = request.POST.get('scname')
        sctrusty = request.POST.get('sctrusty')
        scprincipal = request.POST.get('scprincipal')
        studentcapacity = request.POST.get('studentcapacity')
        schooladd = request.POST.get('schooladd')
        SchoolD = schooldetails(scname=scname,sctrusty=sctrusty,scprincipal=scprincipal,studentcapacity=studentcapacity,schooladd=schooladd)
        SchoolD.save()
        messages.success(request, "Hello, School data has been send.")

    return render(request, "schooldetailform.html")


def updatesc(request, id):
    if request.method == "POST":
        scname = request.POST.get('scname')
        sctrusty = request.POST.get('sctrusty')
        scprincipal = request.POST.get('scprincipal')
        studentcapacity = request.POST.get('studentcapacity')
        schooladd = request.POST.get('schooladd')
        scupdate = schooldetails.objects.get(id=id)
        scupdate.scname=scname
        scupdate.sctrusty=sctrusty
        scupdate.scprincipal=scprincipal
        scupdate.studentcapacity=studentcapacity
        scupdate.schooladd=schooladd
        scupdate.save()
        messages.info(request, "Hello, School data has been Updated.")

    schoolup = schooldetails.objects.get(id=id)
    context = {
        "updatesc": schoolup,
    }
    return render(request, "updateschool.html", context)



def viewschoollist(request):
    schoollist = schooldetails.objects.all().order_by('id')
    context = {
        "sclist": schoollist,
    }
    return render(request, "schoollist.html", context)


def scfulldetails(request, id):
    schfulldetails = schooldetails.objects.get(id=id)
    context = {
        "schdetailers": schfulldetails,
    }
    return render(request, "scfulldetails.html", context)


def delschool(request, id):
    schooldel = schooldetails.objects.get(id=id)
    schooldel.delete()
    messages.warning(request, "Hello, Student yor data has been Deleted.")
    return redirect('/viewschoollist')







# student standard list

def standardlist(request,id):
    schooldet = schooldetails.objects.get(id=id)
    stddetail =Student.objects.filter(scid=id).order_by('id')
    stdcount = {}
    for i in range(1,13):
        stdcount[i] =stddetail.filter(sstandard=i).count()
    return render(request,"standardlist.html",{'schooldet':schooldet,"stdcount":stdcount})




#student attendace

def attendancelist(request,scid,id):
    schooldet = schooldetails.objects.get(id=scid)
    standard = id
    stddetail =Student.objects.filter(sstandard=id,scid=scid).order_by('sroll')

    if request.method == "POST":
        stddate = request.POST.get('stddate')
        stdstandard = request.POST.get('stdstandard')
        stdrolls = request.POST.getlist('stdroll')

        for stdroll in stdrolls:
                stdspresent = request.POST.get(f'stdspresent[{stdroll}]')
                stdattendance = StdPresent(stddate=stddate,stdroll=stdroll,stdstandard=stdstandard,stdspresent=stdspresent)
                stdattendance.save()
        messages.success(request, "Hello, Attendance has been sent.")
        return redirect('attendancelist', scid=scid, id=id)

    return render(request,"attendancelist.html", {'stddetails':stddetail,'schooldet':schooldet,'standard':standard})



def viewattendancelist(request, scid, id):
    schooldet = schooldetails.objects.get(id=scid)
    standard = id
    stddetail = Student.objects.filter(sstandard=id, scid=scid)
    studentattendance = []

    stdattendance = StdPresent.objects.all().order_by('stddate')

    for y in stddetail:
        stdproll = y.sroll
        astdpresent = stdattendance.filter(stdroll=stdproll)
        studentattendance.append({
            'stdproll': stdproll,
            'astdpresent': astdpresent,
        })

    return render(request, "viewattendancelist.html", {'stddetail': stddetail,'schooldet': schooldet,'standard': standard,'studentattendance': studentattendance,})


def test(request):
    return render(request,"test.html")