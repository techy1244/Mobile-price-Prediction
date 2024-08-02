from django.shortcuts import render
from django.contrib.auth.models import User
from . import data
from .mtrain import Train
# Create your views here.

class MobileApp:
    # its connection on home page of application
    def index(req):
        return render(req,'index.html')
    
    def about(req):
        return render(req,'about.html')
    
    
    
class ReLog():
    # User Register and Login code
    def login(req):
        if req.method == "POST":
            uemail = req.POST['uemail']
            upass = req.POST['upass']
            if uemail == '' or upass == '':
                return render(req,'login.html',{'msg':'invalid'})
            else:
                user = User.objects.filter(email=uemail,password = upass).exists()
                if user:
                    return render(req,'uhome.html')
                else:
                    return render(req,'login.html',{'msg':'ivalid'})
        return render(req,'login.html')
    
    def register(req):
        if req.method == "POST":
            uname = req.POST['uname']
            uemail = req.POST['uemail']
            upass = req.POST['upass']
            cpass = req.POST['cpass']
            try:
                if upass == cpass:
                    User.objects.create(username=uname,email=uemail,password=upass)
                    return render(req,'login.html')
            except:
                return render(req,'register.html',{'msg':'invalid'})
        return render(req,'register.html')
    
    def checkmail(req):
        if req.method == 'POST':
            uemail = req.POST['uemail']
            us = User.objects.filter(email = uemail).exists()
            print(us)
            if us:
                req.session['email']=uemail
                return render(req,'forgoot.html',{'da':'valid'})
        return render(req,'forgoot.html',{'da':'invalid'})
    
    def changepass(req):
        if req.method == 'POST':
            upass = req.POST['upass']
            cpass = req.POST['cpass']
            if upass == cpass:
                ps = User.objects.get(email=req.session['email'])
                ps.password = upass
                ps.save()
                return render(req,'login.html',{'mmm':'valid'})
        return render(req,'forgoot.html',{'da':'valid'})
    
    
class UserHome:
    # its after login user will view this page
    def uhome(req):
        return render(req,'uhome.html')
    
    def view(req):
        df = data.readD()
        print(df.head())
        dat = df.to_html()
        return render(req,'view.html',{'dat':dat})
    
    def train(req):
        if req.method == 'POST':
            module = req.POST['algo']
            if module == '0':
                return render(req,'train.html',{'msg':'invalid'})
            elif module == '1':
                data = Train.rf_train()
                return render(req,'train.html',{'dat1':data,'algor':'RandomForestClassifier'})
            elif module == '2':
                data = Train.lr_train()
                return render(req,'train.html',{'dat1':data,'algor':'LogisticRegression'})
            elif module == '3':
                data = Train.hy_train()
                return render(req,'train.html',{'dat1':data,'algor':'Hybrid Module'})
        return render(req,'train.html')
    
    def pred(req):
        mod = Train.hy_trai()
        col = Train.x_trr()
        col1 = col.columns
        if req.method == 'POST':
            dic = req.POST.dict()
            del dic['csrfmiddlewaretoken']
            print(dic)
            inp = []
            for i in dic.keys():
                inp.append(float(dic[i]))
            print(inp)
            result = mod.predict([inp])
            if result == 0:
                msg = 'low cost'
            elif result == 1:
                msg = 'medium cost'
            elif result == 2:
                msg = 'high  cost'
            else:
                msg = 'very high cost'
            return render(req,'pred.html',{'col':col1[:10],'col1':col1[10:20],'msg':msg})
        return render(req,'pred.html',{'col':col1[:10],'col1':col1[10:20]})