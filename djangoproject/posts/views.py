from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from posts.forms import HomeForm
from posts.models import meeting

class HomeView(TemplateView):
    template_name = 'posts/index.html'

    def get(self, request):
        form = HomeForm()
        entries=meeting.objects.all()
        args = {'form': form, 'entries': entries}

        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student_name = request.user
            instance.save()

            subject = "This is a test email"
            from_email=settings.EMAIL_HOST_USER
            to_email = [instance.lect_name.email]
            with open(settings.BASE_DIR + "/posts/templates/posts/confirm_email.txt") as f: email_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=email_message, from_email=from_email, to=to_email)
            html_template = get_template("posts/confirm_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            
            form = HomeForm()
        
        return render(request, self.template_name, {'form': form})


class YesView(TemplateView):
    template_name = 'posts/confirm_attendance.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

#MEETING
#only do write access through the server for security reasons
    #look into this security issue
