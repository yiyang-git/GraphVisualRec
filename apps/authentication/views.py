from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from django.utils import timezone
from django.shortcuts import render, HttpResponse, redirect
from .models import UserForm,DataUsage, DashboardUsage, UserFeedback, LoginFrequency
from .forms import UserForm_form,JobFunctionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from . import neo4jConnection
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to auth/urls.py file for more pages.
"""


class AuthView1(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context



class LogOut(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        # Update the context or set layout if needed
        context = self.get_context_data(**kwargs)
        messages.success(request, '你已成功注销')
        return redirect('auth-login-basic')  # 重定向到主页或其他页面

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )
        return context

class AuthView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update({
            "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['email'] = ''
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  # 登录用户
                return redirect('index')  # 重定向到主页或其他适当的页面
            else:
                messages.error(request, '密码错误')
        except UserForm.DoesNotExist:
            messages.error(request, '用户不存在')

        context = self.get_context_data(**kwargs)
        context['email']= email
        context['user']= request.user
        return self.render_to_response(context)

class RegisterView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = UserForm_form()  # 初始化表单
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = UserForm_form(request.POST)
        if form.is_valid():
            print('表单valided')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            post = form.cleaned_data['post']
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            department = form.cleaned_data['department']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            education = form.cleaned_data['education']
            workenvironment = form.cleaned_data['workenvironment']
            techSkillLevel = form.cleaned_data['techSkillLevel']
            equipmentSkillLevel = form.cleaned_data['equipmentSkillLevel']
            experience_years = form.cleaned_data['experience_years']
            print('数据ok')
            # with neo4jConnection.Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="12345678") as conn:
            #     conn.query("""
            #     MERGE (dept:Department {name: $department})
            #     MERGE (pos:Position {post: $post})
            #     CREATE (user:User {
            #         name: $name,
            #         city: $city,
            #         age: $age,
            #         gender: $gender,
            #         experience_years: $experience_years,
            #         education: $education,
            #         equipmentSkillLevel: $equipmentSkillLevel,
            #         techSkillLevel: $techSkillLevel,
            #         workenvironment: $workenvironment,
            #         count_footprint: $count_footprint,
            #         count_maintenance: $count_maintenance,
            #         count_manufacturing: $count_manufacturing,
            #         count_examine: $count_examine,
            #         count_welding_image: $count_welding_image,
            #         count_surface_image: $count_surface_image,
            #         count_welding_data: $count_welding_data,
            #         count_supplier: $count_supplier,
            #         count_manufacturing_CNC: $count_manufacturing_CNC,
            #         count_global_view: $count_global_view,
            #         count_global_map: $count_global_map,
            #         count_site_info: $count_site_info,
            #         count_employee: $count_employee,
            #         count_country: $count_country,
            #         count_contract: $count_contract,
            #         count_rawdata: $count_rawdata,
            #         login_count: $login_count
            #     })
            #     MERGE (user)-[:属于]->(dept)
            #     MERGE (user)-[:担任]->(pos)
            #     """, parameters={
            #         'post': post,
            #         'name': name,
            #         'city': city,
            #         'department': department,
            #         'age': age,
            #         'gender': gender,
            #         'experience_years': experience_years,
            #         'education': education,
            #         'equipmentSkillLevel': equipmentSkillLevel,
            #         'techSkillLevel': techSkillLevel,
            #         'workenvironment': workenvironment,
            #         'count_footprint': 0,
            #         'count_maintenance': 0,
            #         'count_manufacturing': 0,
            #         'count_examine': 0,
            #         'count_welding_image': 0,
            #         'count_surface_image': 0,
            #         'count_welding_data': 0,
            #         'count_supplier': 0,
            #         'count_manufacturing_CNC': 0,
            #         'count_global_view': 0,
            #         'count_global_map': 0,
            #         'count_site_info': 0,
            #         'count_employee': 0,
            #         'count_country': 0,
            #         'count_contract': 0,
            #         'count_rawdata': 0,
            #         'login_count': 0
            #     })
            #     conn.close()

            extra_fields = {
                'post': post,
                'name': name,
                'city': city,
                'department': department,
                'age': age,
                'gender': gender,
                'education': education,
                'workenvironment': workenvironment,
                'techSkillLevel': techSkillLevel,
                'equipmentSkillLevel': equipmentSkillLevel,
                'experience_years': experience_years,
            }

            user = UserForm.objects.create_user(email=email, password=password, **extra_fields)
            DataUsage.objects.create(user=user)
            DashboardUsage.objects.create(user=user)
            UserFeedback.objects.create(user=user)
            LoginFrequency.objects.create(user=user)

            messages.error(request, '注册成功！')
            return redirect('auth-login-basic')
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form  # 保留表单数据和错误信息
            messages.error(request, form.errors)
            return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class AccountSet(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        user = self.request.user
        context['user'] = user
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        if request.method == 'POST':
            user.name = request.POST.get('username')
            user.age = request.POST.get('age')
            user.gender = int(request.POST.get('gender'))
            user.post = request.POST.get('post')
            user.location = request.POST.get('location')
            user.education = request.POST.get('education')
            user.department = request.POST.get('department')
            user.workenvironment = request.POST.get('workenvironment')
            user.techSkillLevel = request.POST.get('techSkillLevel')
            user.equipmentSkillLevel = request.POST.get('equipmentSkillLevel')
            user.experience_years = request.POST.get('experience_years')
            user.save()
            return redirect('auth_account_settings')
        context = self.get_context_data(**kwargs)
        context['user'] = user
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
class DatausageStatistics(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        user = self.request.user
        context['user'] = user
        dashboard_usage = {
            'count_global_view': user.dashboard_usages.first().count_global_view if user.dashboard_usages.exists() else 0,
            'count_global_map': user.dashboard_usages.first().count_global_map if user.dashboard_usages.exists() else 0,
            'count_site_info': user.dashboard_usages.first().count_site_info if user.dashboard_usages.exists() else 0,
            'count_employee': user.dashboard_usages.first().count_employee if user.dashboard_usages.exists() else 0,
            'count_country': user.dashboard_usages.first().count_country if user.dashboard_usages.exists() else 0,
            'count_contract': user.dashboard_usages.first().count_contract if user.dashboard_usages.exists() else 0,
            'count_projectIDCard': user.dashboard_usages.first().count_projectIDCard if user.dashboard_usages.exists() else 0,
            'count_facilities': user.dashboard_usages.first().count_facilities if user.dashboard_usages.exists() else 0,
            'count_supplierGIS': user.dashboard_usages.first().count_supplierGIS if user.dashboard_usages.exists() else 0,
        }
        data_usage = {
            'count_footprint': user.data_usages.first().count_footprint if user.data_usages.exists() else 0,
            'count_maintenance': user.data_usages.first().count_maintenance if user.data_usages.exists() else 0,
            'count_manufacturing': user.data_usages.first().count_manufacturing if user.data_usages.exists() else 0,
            'count_manufacturing_CNC': user.data_usages.first().count_manufacturing_CNC if user.data_usages.exists() else 0,
            'count_examine': user.data_usages.first().count_examine if user.data_usages.exists() else 0,
            'count_welding_image': user.data_usages.first().count_welding_image if user.data_usages.exists() else 0,
            'count_surface_image': user.data_usages.first().count_surface_image if user.data_usages.exists() else 0,
            'count_welding_data': user.data_usages.first().count_welding_data if user.data_usages.exists() else 0,
            'count_supplier': user.data_usages.first().count_supplier if user.data_usages.exists() else 0,
        }
        context['dashboard_usage'] = dashboard_usage
        context['data_usage'] = data_usage
        return context




@method_decorator(login_required, name='dispatch')
class UserFeedbackView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        user = self.request.user
        context['user'] = user
        feedback = UserFeedback.objects.get(user_id=self.request.user.id)
        context['feedback'] = feedback
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        feedback = UserFeedback.objects.get(user_id=request.user.id)
        new_data_satisfaction = int(request.POST.get('dataSatisfaction', 0))
        new_visu_satisfaction = int(request.POST.get('visuSatisfaction', 0))
        new_user_satisfaction = int(request.POST.get('userSatisfaction', 0))
        feedback.datasatisfaction = max(new_data_satisfaction, 0)
        feedback.visusatisfaction = max(new_visu_satisfaction, 0)
        feedback.usersatisfaction = max(new_user_satisfaction, 0)
        feedback.dataPreference = int(request.POST.get('dataPreference'))
        feedback.dashPreference = int(request.POST.get('dashPreference'))
        feedback.visuPreference = int(request.POST.get('visuPreference'))

        new_comment = request.POST.get('comment', '')
        if feedback.comment and feedback.comment != ' ':
            feedback.comment += f"; {new_comment}"
        else:
            feedback.comment = new_comment
        feedback.save()
        context = self.get_context_data(**kwargs)
        context['user'] = user
        context['feedback'] = feedback
        return self.render_to_response(context)
