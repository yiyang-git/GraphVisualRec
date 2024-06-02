from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""

@method_decorator(login_required, name='dispatch')
class RecommendationData(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['user'] = self.request.user
        return context

@method_decorator(login_required, name='dispatch')
class QlikDashboard(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "content_layout": "compact",
            }
        )
        context['user'] = self.request.user
        app_id = "L%3A%5Csysteme%5Cdocuments%5CQlik%5CSense%5CApps%5Cservice%20sites.qvf"
        sheet_name = self.request.GET.get('sheet_name')
        sheet_ids = {
            'SiteKPI': 'f5b653fe-a1d9-4aaf-b29b-e364667a6d83',
            'GlobalSiteData': '9f0d9f5e-c15d-415b-aae6-2a5fccc7ec21',
            'EmployeeInfo': '8831078b-2a49-41c6-ae8a-5673661dfb83',
            'SiteIDCard': '7cb11d18-a93c-4b83-9ff5-f93d1e5b42de',
            'SiteGIS': '378c3467-95dc-467b-8355-59b15da81025',
            'ProductPlatform': '7d266d40-4f00-41e9-9365-2e5366f07a65',
            'FacilityDistributionMap': '7cb11d18-a93c-4b83-9ff5-f93d1e5b42de',
            'SupplierGIS': 'bc64f10f-e259-401b-b9b4-be89c1ed30c1',
            'ProjectIDCard': 'a9faebaa-bd12-4fb9-906e-ee6c49bc4eae'
        }
        sheet_id = sheet_ids.get(sheet_name, '9f0d9f5e-c15d-415b-aae6-2a5fccc7ec21')
        lang = "zh-CN"
        theme = "horizon"
        opt = "ctxmenu,currsel"
        iframe_src = f"http://localhost:4848/single/?appid={app_id}&sheet={sheet_id}&lang={lang}&theme={theme}&opt={opt}"
        context['iframe_src'] = iframe_src
        context['active_tab'] = sheet_name
        # context['user'] = request.user
        TemplateHelper.map_context(context)
        return context

