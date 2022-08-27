from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')


def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)


from .models import plan_settings

def admin_plan_settings_add(request):
    if request.method == 'POST':
        plan_type = request.POST.get('plan_type')
        jm = plan_settings(plan_type=plan_type)
        jm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_plan_settings_add.html', context)
    else:
        return render(request, './myapp/admin_plan_settings_add.html')

def admin_plan_settings_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        plan_type = request.POST.get('plan_type')
        jm = plan_settings.objects.get(id=int(s_id))

        jm.plan_type = plan_type
        jm.save()
        msg = 'Record Updated'
        jm_l = plan_type.objects.all()
        context = {'plan_list': jm_l, 'msg': msg}
        return render(request, './myapp/admin_plan_settings_view.html', context)
    else:
        id = request.GET.get('id')
        jm = plan_settings.objects.get(id=int(id))
        context = {'plan_type': jm.plan_type, 's_id': jm.id}
        return render(request, './myapp/admin_plan_settings_edit.html',context)


def admin_plan_settings_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    jm = plan_settings.objects.get(id=int(id))
    jm.delete()
    msg = 'Record Deleted'
    jm_l = plan_settings.objects.all()
    context = {'plan_list': jm_l, 'msg':msg}
    return render(request, './myapp/admin_plan_settings_view.html',context)


def admin_plan_settings_view(request):
    jm_l = plan_settings.objects.all()
    context = {'plan_list':jm_l}
    return render(request, './myapp/admin_plan_settings_view.html',context)


######### Architect ###############
from .models import architect_details
from datetime import datetime
from django.core.files.storage import FileSystemStorage

def architect_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd,u_type='architect')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/architect_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/architect_login.html',context)
    else:
        return render(request, 'myapp/architect_login.html')

def architect_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/architect_home.html',context)

def architect_details_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(u_file.name, u_file)

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = int(request.POST.get('age'))

        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        descrp = request.POST.get('descrp')
        image = pic_path

        password = '1234'
        uname=email
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='architect')
        ul.save()

        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = architect_details(user_id=user_id,fname=fname,lname=lname,age=age,gender=gender,addr=addr,pin=pin,contact=contact,
                               email=email,descrp=descrp,image=image,status=status)
        ud.save()


        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/architect_login.html',context)

    else:
        return render(request, 'myapp/architect_details_add.html')

def architect_details_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = architect_details.objects.get(user_id=int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = int(request.POST.get('age'))

        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        descrp = request.POST.get('descrp')

        up.fname = fname
        up.lname = lname
        up.age = age

        up.gender = gender
        up.addr = addr
        up.pin = pin
        up.contact = contact
        up.email = email
        up.descrp = descrp
        up.save()


        context = {'msg': 'Arcitect Details Updated','up':up}
        return render(request, 'myapp/architect_details_update.html',context)

    else:
        user_id = request.session['user_id']
        up = architect_details.objects.get(user_id=int(user_id))
        context={'up':up}
        return render(request, 'myapp/architect_details_update.html',context)


def artist_photo_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = architect_details.objects.get(user_id=int(user_id))

        u_file = request.FILES['document']
        fs = FileSystemStorage()
        image = fs.save(u_file.name, u_file)
        up.image = image
        up.save()
        #print(user_id)
        context = {'msg': 'User Picture Updated','pic_path': up.image}
        return render(request, 'myapp/architect_photo_update.html',context)

    else:
        user_id = request.session['user_id']
        up = architect_details.objects.get(user_id=int(user_id))
        context = {'pic_path': up.image}
        return render(request, 'myapp/architect_photo_update.html',context)

def architect_changepassword(request):
    if request.method == 'POST':
        user_id = request.session['user_id']

        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/architect_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/architect_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/architect_changepassword.html', context)
    else:
        context = {}
        return render(request, './myapp/architect_changepassword.html',context)

def architect_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return architect_login_check(request)
    else:
        return architect_login_check(request)


from .models import architect_plans

def architect_plans_add(request):
    if request.method == 'POST':
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        title = request.POST.get('title')
        descrp = request.POST.get('descrp')
        amount = float(request.POST.get('amount'))
        plan_id = int(request.POST.get('plan_id'))

        arch_id = request.session['user_id']

        pm = architect_plans(plan_id=plan_id,arch_id=arch_id,title=title,descrp=descrp,amount=amount,dt=dt,tm=tm)
        pm.save()

        scm_l = plan_settings.objects.all()
        context = {'plan_list':scm_l,'msg':'Record added'}
        return render(request, 'myapp/architect_plans_add.html',context)

    else:
        scm_l = plan_settings.objects.all()
        context = {'plan_list':scm_l,'msg':''}
        return render(request, 'myapp/architect_plans_add.html',context)

def architect_plans_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = architect_plans.objects.get(id=int(id))
    pm.delete()

    arch_id = request.session['user_id']
    pm_l = architect_plans.objects.filter(arch_id=int(arch_id))
    scm_l = plan_settings.objects.all()

    context ={'plan_list':scm_l,'ar_plan_list': pm_l,'msg':'Record deleted'}
    return render(request,'myapp/architect_plans_view.html',context)

def architect_plans_view(request):
    arch_id = request.session['user_id']
    pm_l = architect_plans.objects.filter(arch_id=int(arch_id))
    scm_l = plan_settings.objects.all()

    context = {'plan_list': scm_l, 'ar_plan_list': pm_l, 'msg': ''}
    return render(request, 'myapp/architect_plans_view.html', context)


from .models import plan_details

def architect_plan_details_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        image = fs.save(u_file.name, u_file)

        descrp = request.POST.get('descrp')
        title = request.POST.get('title')
        ar_plan_id = int(request.POST.get('ar_plan_id'))

        arch_id = request.session['user_id']

        pm = plan_details(ar_plan_id=ar_plan_id,image=image,descrp=descrp,title=title )
        pm.save()

        context = {'ar_plan_id':ar_plan_id,'msg':'Record added'}
        return render(request, 'myapp/architect_plan_details_add.html',context)

    else:
        ar_plan_id = int(request.GET.get('ar_plan_id'))

        context = {'ar_plan_id':ar_plan_id,'msg':''}
        return render(request, 'myapp/architect_plan_details_add.html',context)

def architect_plan_details_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = plan_details.objects.get(id=int(id))
    pm.delete()

    ar_plan_id = int(request.GET.get('ar_plan_id'))
    arch_id = request.session['user_id']

    pm_l = plan_details.objects.filter(ar_plan_id=int(ar_plan_id))


    context ={'plan_details_list': pm_l,'msg':'Record deleted','ar_plan_id':ar_plan_id}
    return render(request,'myapp/architect_plan_details_view.html',context)

def architect_plan_details_view(request):
    ar_plan_id = int(request.GET.get('ar_plan_id'))
    castingteam_id = request.session['user_id']

    pm_l = plan_details.objects.filter(ar_plan_id=int(ar_plan_id))

    context = {'ar_plan_id':ar_plan_id,'plan_details_list': pm_l, 'msg': ''}
    return render(request, 'myapp/architect_plan_details_view.html', context)


def architect_sales_master_view(request):
    user_id = request.session['user_id']
    plan_id = request.POST.get('plan_id')
    pm_l = sales_master.objects.filter(arch_id=int(user_id))

    scm_l = architect_plans.objects.all()
    ar_l = user_details.objects.all()
    context = {'user_list':ar_l,'ar_plan_list': scm_l, 'sales_list': pm_l, 'msg': ''}
    return render(request, 'myapp/architect_sales_master_view.html', context)


def architect_plan_ratings_view(request):
    user_id = request.session['user_id']
    plan_id = request.GET.get('plan_id')
    pm_l = user_rating.objects.filter(plan_id=int(plan_id))

    scm_l = architect_plans.objects.all()
    ar_l = user_details.objects.all()
    context = {'user_list':ar_l,'ar_plan_list': scm_l, 'rating_list': pm_l, 'msg': ''}
    return render(request, 'myapp/architect_plan_ratings_view.html', context)


def architect_user_proposal_view(request):

    user_id = request.session['user_id']

    pm_l = user_proposal.objects.filter(arch_id=int(user_id))

    ar_l = user_details.objects.all()
    context ={'user_list':ar_l,'proposal_list': pm_l,'msg':''}
    return render(request,'myapp/architect_user_proposal_view.html',context)



def architect_user_proposal_reply(request):
    if request.method == 'POST':

        user_id = request.session['user_id']
        proposal_id = int(request.POST.get('proposal_id'))
        remark = request.POST.get('remark')

        suc = user_proposal.objects.get(id=int(proposal_id))
        suc.remark = remark
        suc.save()

        pm_l = user_proposal.objects.filter(arch_id=int(user_id))

        ar_l = user_details.objects.all()
        context = {'user_list': ar_l, 'proposal_list': pm_l, 'msg': ''}
        return render(request, 'myapp/architect_user_proposal_view.html', context)

    else:
        user_id = request.session['user_id']
        proposal_id = int(request.GET.get('id'))

        context = { 'proposal_id': proposal_id}
        return render(request, './myapp/architect_user_proposal_reply.html', context)



#############User###################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def user_plans_search(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        pm_l = architect_plans.objects.filter(title__contains=query)

        scm_l = plan_settings.objects.all()
        ar_l = architect_details.objects.all()
        context = {'architect_list':ar_l,'plan_list': scm_l, 'ar_plan_list': pm_l, 'msg': ''}
        return render(request, 'myapp/user_architect_plans_view.html', context)
    else:
        return render(request, 'myapp/user_plans_search.html')


def user_plan_type_search(request):

    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        pm_l = architect_plans.objects.filter(plan_id=int(plan_id))

        scm_l = plan_settings.objects.all()
        ar_l = architect_details.objects.all()
        context = {'architect_list':ar_l,'plan_list': scm_l, 'ar_plan_list': pm_l, 'msg': ''}
        return render(request, 'myapp/user_architect_plans_view.html', context)
    else:
        scm_l = plan_settings.objects.all()
        context = { 'plan_list': scm_l,  'msg': ''}
        return render(request, 'myapp/user_plan_type_search.html',context)

def user_architect_plan_details_view(request):
    ar_plan_id = int(request.GET.get('ar_plan_id'))
    castingteam_id = request.session['user_id']

    pm_l = plan_details.objects.filter(ar_plan_id=int(ar_plan_id))

    context = {'ar_plan_id':ar_plan_id,'plan_details_list': pm_l, 'msg': ''}
    return render(request, 'myapp/user_architect_plan_details_view.html', context)

def user_architect_search(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        ar_l = architect_details.objects.filter(fname__contains=query)

        context = {'architect_list':ar_l, 'msg': ''}
        return render(request, 'myapp/user_architect_details_view.html', context)
    else:
        return render(request, 'myapp/user_architect_search.html')

from .models import sales_master
def user_sales_master_view(request):
    user_id = request.session['user_id']
    plan_id = request.POST.get('plan_id')
    pm_l = sales_master.objects.filter(user_id=int(user_id))

    scm_l = architect_plans.objects.all()
    ar_l = architect_details.objects.all()
    context = {'architect_list':ar_l,'ar_plan_list': scm_l, 'sales_list': pm_l, 'msg': ''}
    return render(request, 'myapp/user_sales_master_view.html', context)


def user_sales_master_add(request):
    if request.method == 'POST':
        plan_id = int(request.POST.get('plan_id'))
        user_id = request.session['user_id']
        arch_id = int(request.POST.get('arch_id'))
        commision = request.POST.get('commision')
        print('Commission',commision)
        card = request.POST.get('card')
        number = request.POST.get('number')
        cvv = request.POST.get('cvv')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')


        pm = sales_master(plan_id=plan_id,user_id=int(user_id),arch_id=arch_id,commision=float(commision),
                          card=card,number=number,cvv=cvv,dt=dt,tm=tm)
        pm.save()

        context = {'plan_id':plan_id,'arch_id':arch_id,'msg':'Record added'}
        return render(request, 'myapp/user_plans_search.html',context)

    else:
        plan_id = int(request.GET.get('plan_id'))
        apd = architect_plans.objects.get(id=plan_id)
        arch_id = apd.arch_id
        commission = apd.amount * .02
        context = {'plan_id':plan_id,'arch_id':arch_id,'commision':commission,'msg':''}
        return render(request, 'myapp/user_sales_master_add.html',context)

from .models import user_rating

def user_plan_ratings_view(request):
    user_id = request.session['user_id']
    plan_id = request.GET.get('plan_id')
    pm_l = user_rating.objects.filter(plan_id=int(plan_id))

    scm_l = architect_plans.objects.all()
    ar_l = user_details.objects.all()
    context = {'user_list':ar_l,'ar_plan_list': scm_l, 'rating_list': pm_l, 'msg': ''}
    return render(request, 'myapp/user_plan_ratings_view.html', context)


def user_plan_ratings_view2(request):
    user_id = request.session['user_id']
    plan_id = request.GET.get('plan_id')
    pm_l = user_rating.objects.filter(plan_id=int(plan_id),user_id=int(user_id))

    scm_l = architect_plans.objects.all()
    ar_l = user_details.objects.all()
    context = {'user_list':ar_l,'ar_plan_list': scm_l, 'rating_list': pm_l, 'msg': ''}
    return render(request, 'myapp/user_plan_ratings_view.html', context)

def user_plan_ratings_add(request):
    if request.method == 'POST':
        plan_id = int(request.POST.get('plan_id'))
        user_id = request.session['user_id']


        rating = request.POST.get('rating')
        remarks = request.POST.get('remarks')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')


        pm = user_rating(plan_id=plan_id, user_id=int(user_id),dt=dt,tm=tm,rating=int(rating),remarks=remarks)
        pm.save()

        context = {'msg':'Record added'}
        return render(request, 'myapp/user_plans_search.html',context)

    else:
        plan_id = int(request.GET.get('plan_id'))
        context = {'plan_id':plan_id,'msg':''}
        return render(request, 'myapp/user_plan_ratings_add.html',context)


from .models import user_proposal

def user_architect_proposal_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        filepath = fs.save(u_file.name, u_file)

        requirments = request.POST.get('requirments')
        remark = 'no remarks'
        arch_id = int(request.POST.get('arch_id'))
        user_id = request.session['user_id']
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        pm = user_proposal(user_id=int(user_id),arch_id=arch_id,filepath=filepath,
                           requirments=requirments,remark=remark,dt=dt,tm=tm,status='ok' )
        pm.save()

        context = {'arch_id':arch_id,'msg':'Record added'}
        return render(request, 'myapp/user_architect_search.html',context)

    else:
        arch_id = int(request.GET.get('arch_id'))

        context = {'arch_id':arch_id,'msg':''}
        return render(request, 'myapp/user_architect_proposal_add.html',context)

def user_architect_proposal_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = user_proposal.objects.get(id=int(id))
    pm.delete()


    user_id = request.session['user_id']

    pm_l = user_proposal.objects.filter(user_id=int(user_id))

    ar_l = architect_details.objects.all()
    context ={'architect_list':ar_l,'proposal_list': pm_l,'msg':'Record deleted'}
    return render(request,'myapp/user_architect_proposal_view.html',context)

def user_architect_proposal_view(request):

    user_id = request.session['user_id']

    pm_l = user_proposal.objects.filter(user_id=int(user_id))

    ar_l = architect_details.objects.all()
    context ={'architect_list':ar_l,'proposal_list': pm_l,'msg':''}
    return render(request,'myapp/user_architect_proposal_view.html',context)

