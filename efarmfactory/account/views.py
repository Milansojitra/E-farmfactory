from django.shortcuts import render,redirect
from django.views.generic import View
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import generate_token
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
import threading
from django.contrib.auth import authenticate, login, logout
from .forms import UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth.decorators import login_required




class EmailThread(threading.Thread):

    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()



class registerView(View):
    def get(self,request):
        return render(request,'account/register.html')
    def post(self,request):

        context={
            'data':request.POST,
            'has_error': False
        }
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        password1=data.get('password1')
        if len(password)<6:
            messages.add_message(request,messages.ERROR,"Password length must be grater then 6")
            context['has_error']=True
        if password!=password1:
            messages.add_message(request,messages.ERROR,"Passwords does't match")
            context['has_error']=True
        if not validate_email(email):
            messages.error(request,"Email is not valid")
            context['has_error']=True

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            context['has_error']=True
        
        if User.objects.filter(email=email):
            messages.error(request,"email is already taken")
            context['has_error']=True
        if context['has_error']:
            return render(request,'account/register.html',context)
        
        user=User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.is_active=False
        user.first_name=username.split()[0]
        user.last_name=username.split()[-1]
        user.save()

        curr_site=get_current_site(request)
        email_subject="Activation mail"
        email_message=render_to_string('account/activate.html',
        {
            'user':user,
            'domain':curr_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        }
        )

        send_mail(
            'Subject here',
            'Here is the message.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
          )
        # email_message=EmailMessage(
        #     email_subject,
        #     email_message,
        #     to=[email],
        # )
        # email_message.send(fail_silently=False)


        messages.success(request,"Account has been created\ncheck your mail to activate account")
        return render(request,'account/register.html',context)




class activateAccount(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)

        except Exception  as i:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,"Account activate sucesfully!!")
            return redirect('login')
        return render('account/activation_fail.html',status=401)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            p_form.save()
            messages.success(request, 'Your account updated succussfully!!')
            return redirect('profile')
        
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=UserProfileUpdateForm(instance=request.user.profile)

   
    context={'u_form':u_form,
             'p_form':p_form,
             }
    return render(request, 'account/profile.html',context)


def demo(request):
    from django.core.mail import send_mail
    print('initial')
    send_mail(
        'Subject here',
        'Here is the message.',
        'efarmfacotry103305@example.com',
        ['milansojitra1019@gmail.com'],
        fail_silently=False,
    )
    print('complete')
    return render( 'wwrwf')