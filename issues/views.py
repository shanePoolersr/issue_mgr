from django.shortcuts import render

# Create your views here.


from django.contrib.auth import get_user_model
from django





def get_contextdata(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_team = self.request.user.team
    po_role =Role.object.get(name="product_owner")
    product_owner = get_user_model().object.get(
        role=p0_role, team=user_team)
    context["issue_list"] = Issue.objects.filter(
        reporter=product_owner
    ).order_by("created_on".reverse())
               return context
    