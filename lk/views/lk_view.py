from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import generic
from quiz.models.quiz_result_student import QuizResult
from users.models import User, Profiles, Friendship
from ..forms import lk_form
from users.forms import RenameForm
from django.core.mail import send_mail, EmailMessage
from instrumenst.pdf.pdf_creater import create_pdf_at_html


class LkView(generic.View):
    """ Личный кабинет как видет его пользователь """

    def get(self, requests):
        if requests.user.is_authenticated:
            self.user = User.objects.get(username=requests.user)
            self.date = QuizResult.objects.filter(student=requests.user)
            self.profile = Friendship.objects.filter(user_name_id=User.objects.get(username=self.user))
            form_image_add = lk_form.AlbomsImageForm()
            return render(requests, 'lk/personal_account/lk.html',
                          {"user_bio": self.user,
                           "profile": self.profile,
                           "context": self.date, 'form_image_add': form_image_add})
        return redirect('login')

    def post(self, requests):
        # form_image_add = lk_form.AlbomsImageForm(requests.POST or None, requests.FILES or None)
        files_image = requests.FILES.getlist('images')
        self.user = User.objects.get(username=requests.user)
        self.date = QuizResult.objects.filter(student=requests.user)
        self.profile = Friendship.objects.filter(user_name_id=User.objects.get(username=self.user))
        if files_image:
            for file in files_image:
                date = lk_form.AlbomsImage.objects.create(profile_albomsimage=requests.user.profiles, image=file)
            date.save()
            return render(requests, 'lk/personal_account/lk.html',
                          {"user_bio": self.user, 'files_image': files_image, "profile": self.profile, })
        files_image_add = lk_form.AlbomsImageForm()
        return render(requests, 'lk/personal_account/lk.html',
                      {"user_bio": self.user, 'form_image_add': files_image_add, "profile": self.profile})


class LKDetailView(generic.View):
    def get(self, request, user_name):
        self.user = User.objects.get(username=user_name)
        self.date = QuizResult.objects.filter(student=user_name)
        self.profile = Friendship.objects.filter(user_name_id=User.objects.get(username=user_name))
        self.user_request = request.user
        self.profile_request = Friendship.objects.filter(user_name=self.user_request)
        form_image_add = lk_form.AlbomsImageForm()
        if Profiles.objects.get(user__username=user_name).id in list(
                map(lambda x: x[0], self.profile_request.values_list('profile_friendshiop'))):
            form_add_friend = 'del'
        else:
            form_add_friend = 'add'
        return render(request, 'lk/personal_account/lk_for_look.html',
                      {"user_bio": self.user,
                       "profile": self.profile,
                       "context": self.date,
                       "form_image_add": form_image_add,
                       "form_add_friend": form_add_friend,
                       'user_name': user_name})

    def post(self, requests, user_name):
        form_image_add = lk_form.AlbomsImageForm(requests.POST or None, requests.FILES or None)
        files_image = requests.FILES.getlist('images')
        self.user = User.objects.get(username=requests.user)
        self.date = QuizResult.objects.filter(student=requests.user)
        if files_image:
            for file in files_image:
                date = lk_form.AlbomsImage.objects.create(profile_albomsimage=requests.user.profiles, image=file)
            date.save()
            return render(requests, 'lk/personal_account/lk_for_look.html',
                          {"user_bio": self.user, 'files_image': files_image})
        if 'add_friend' in requests.POST or 'del_friend' in requests.POST:
            if 'add_friend' in requests.POST:
                new_friend = Friendship.objects.create(user_name=User.objects.get(pk=requests.user.id),
                                                       profile_friendshiop=Profiles.objects.get(
                                                           user__username=user_name))
                new_friend.save()
                print('добавляем друга в базу дданных', requests.POST['add_friend'])
                return redirect('home')
            else:
                del_friend = Friendship.objects.get(user_name=User.objects.get(pk=requests.user.id),
                                                    profile_friendshiop=Profiles.objects.get(user__username=user_name))
                del_friend.delete()
                print(f'удаляем друга из базы данных {del_friend}')
                return redirect('home')
        files_image_add = lk_form.AlbomsImageForm()
        return render(requests, 'lk/personal_account/lk_for_look.html',
                      {"user_bio": self.user, 'form_image_add': files_image_add, 'form_add_friend': "0"})


class LkDetailQuizView(generic.View):
    def get(self, request, user_name, number):
        self.user = User.objects.get(username=user_name)
        self.date = QuizResult.objects.get(id=number)
        return render(request, 'lk/personal_account/lk_detail_quiz.html',
                      {"user_bio": self.user, "context": self.date})

    """ отправка писем через EmailMessage а так  же созданиие через функцию create_pdf_at_html пдф фалов"""
    def post(self, request, user_name, number):
        if request.method == 'POST':
            from apps import settings
            self.data=QuizResult.objects.get(id=number)
            msg = render_to_string('lk/personal_account/lk_detail_quiz.html', {'user_name': user_name, 'number': number, 'user_bio': request.user, 'context': self.data})
            file_path = str(create_pdf_at_html(f'1234', request.user))
            mail = EmailMessage(subject='subject team',body=msg,from_email=settings.EMAIL_HOST_USER,to=[request.user.email])
            mail.content_subtype = 'html'
            mail.attach_file(file_path)
            email_res = mail.send()
            return redirect('home')



class LkViewEdit(generic.View):
    def get(self, requests, user_name):
        form_edit = lk_form.EditLkForm()
        form_edit_user = RenameForm()
        form_image_add = lk_form.AlbomsImageForm()
        self.user = User.objects.get(username=requests.user)
        return render(requests, 'lk/personal_account/lk_for_look_edit_form.html', {"user_bio": self.user,
                                                                                   'form_edit_lk': form_edit,
                                                                                   'form_edit_user': form_edit_user})

    def post(self, requests, user_name):
        if requests.method == "POST":
            form_edit = lk_form.EditLkForm(requests.POST, requests.FILES)
            form_edit_user = RenameForm(requests.POST)
            form_image_add = lk_form.AlbomsImageForm()
            if form_edit.is_valid() and form_edit_user.is_valid():  # and form_edit_user.is_valid():
                user = User.objects.get(username=requests.user)
                user.first_name = form_edit_user.cleaned_data['first_name']
                user.last_name = form_edit_user.cleaned_data['last_name']
                user.email = form_edit_user.cleaned_data['email']
                profile_user = Profiles.objects.get(user=requests.user)
                if requests.FILES:
                    profile_user.image_profile = form_edit.cleaned_data['image_profile']
                profile_user.birthday = form_edit.cleaned_data['birthday']
                profile_user.city = form_edit.cleaned_data['city']
                profile_user.location = form_edit.cleaned_data['location']
                profile_user.about = form_edit.cleaned_data['about']
                profile_user.zodiac = form_edit.cleaned_data['zodiac']
                profile_user.socionics_type = form_edit.cleaned_data['socionics_type']
                user.save()
                profile_user.save()
                return redirect('home')
        return render(requests, 'lk/personal_account/lk_for_look_edit_form.html',
                      {'form_edit_lk': form_edit, "user_bio": requests.user})
