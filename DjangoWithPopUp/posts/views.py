from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from posts.forms import HomeForm
from posts.models import meeting
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'posts/index.html'
    
    def get(self, request):
        form = HomeForm()
        successMessage=""
        args = {'form': form, 'successMessage': successMessage}
        
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student_name = request.user
            instance.save()
            successMessage = "Thank you for registering a Meeting! Once it has taken place your lecturer will confirm that you attended and you will notified of this via email. If you do not recieve such a confirmation email please contact your lecturer directly to enquire about this."

            subject = "This is a test email"
            from_email=settings.EMAIL_HOST_USER
            to_email = [instance.lect_name.email]
            with open(settings.BASE_DIR + "/posts/templates/posts/confirm_email.txt") as f: email_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=email_message, from_email=from_email, to=to_email)
            html_template = get_template("posts/confirm_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            
            form = HomeForm()
        
        return render(request, self.template_name, {'form': form, 'lect': instance.lect_name, 'successMessage': successMessage})

class YesView(LoginRequiredMixin, TemplateView):
    template_name = 'posts/confirm_attendance.html'

    def get(self, request):
        form = modelformset_factory(meeting, fields=('student_name','m_date','m_time','descript','attended',), extra=0)
        formset = form(queryset=meeting.objects.filter(lect_name=request.user, attended=False))
        pastEntries = meeting.objects.filter(lect_name=request.user, attended=True)
        mickie = meeting.objects.filter(lect_name=request.user, attended=False)
        return render(request, self.template_name, {'formset' : formset, 'pastEntries' : pastEntries, 'mickie' : mickie})

    def post(self, request):
        form = modelformset_factory(meeting, fields=('student_name','m_date','m_time','descript','attended',), extra=0)
        formset = form(request.POST, queryset=meeting.objects.filter(lect_name=request.user, attended=False))
        pastEntries = meeting.objects.filter(lect_name=request.user, attended=True)
        mickie = meeting.objects.filter(lect_name=request.user, attended=False)
        if formset.is_valid():
           poop = formset.save()
           formset = form(queryset=meeting.objects.filter(lect_name=request.user, attended=False))
           pastEntries = meeting.objects.filter(lect_name=request.user, attended=True)
           mickie = meeting.objects.filter(lect_name=request.user, attended=False)
        return render(request, self.template_name, {'formset' : formset, 'pastEntries' : pastEntries, 'mickie' : mickie})

class EditView(LoginRequiredMixin, TemplateView):
    template_name = 'posts/edit_entries.html'

    def get(self, request):
        form = modelformset_factory(meeting, fields=('lect_name','m_date','m_time','descript',), extra=0)
        formset = form(queryset=meeting.objects.filter(student_name=request.user, attended=False))
        pastEntries = meeting.objects.filter(student_name=request.user, attended=True)
        return render(request, self.template_name, {'formset': formset, 'pastEntries' : pastEntries})
    
    def post(self, request):
        form = modelformset_factory(meeting, fields=('lect_name','m_date','m_time','descript',), extra=0)
        formset = form(request.POST, queryset=meeting.objects.filter(student_name=request.user, attended=False))
        pastEntries = meeting.objects.filter(student_name=request.user, attended=True)
        if formset.is_valid():
            instances = formset.save()
            formset = form(queryset=meeting.objects.filter(student_name=request.user, attended=False))
            pastEntries = meeting.objects.filter(lect_name=request.user, attended=True)
        return render(request, self.template_name, {'formset' : formset, 'pastEntries' : pastEntries})

#DECISIONS
#1) Should the lecturer be able to see all of their meetings or only the ones that the student has not attended.
#   These are not mutually exclusive if they are seperated into two tables!!!!!!!
#   Come up with a few ways of doing this for the testings
#
#2) Should explanation be available via an i button or via being seen on the screen.
#
#3) Should they be able to un-attend a student
#
#FOR TESTING: Ask them they're thoughts at the point when they are a novice user and at the point when they are an experienced user
