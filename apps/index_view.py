from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name="dispatch")
class DashboardView(TemplateView):
    template_name = 'quotation_list.html'

# {% extends 'adminlte/base.html' %}
# {% block content %}
# {% load mathfilters %}
# <div class="row">
#     <div class="col-md-12">
#         <style>
#   h2 {
#     font-size: 24px;
#     font-weight: bold;
#     color: #333;
#     margin-bottom: 20px;
#     border-bottom: 2px solid #ccc;
#     padding-bottom: 10px;
#   }
# </style>
#
# <h2>Quotation {{ quotation.pk }}</h2>
#
#         <div class="box">
#             <div class="box-body">
#                 <table class="table">
#                     <tr>
#                         <td>Dealer:</td>
#                         <td>{{ quotation.dealer.name }}</td>
#                     </tr>
#                     <tr>
#                         <td>District:</td>
#                         <td>{{ quotation.district.name }}</td>
#                     </tr>
#                     <tr>
#                         <td>Created By:</td>
#                         <td>{{ quotation.created_by }}</td>
#                     </tr>
#                     <tr>
#                         <td>Created At:</td>
#                         <td>{{ quotation.created_at }}</td>
#                     </tr>
#                     <tr>
#                         <td>Total Price:</td>
#                         <td>{{ quotation.quotationline_set.all|mul:'price*quantity'|floatformat:2 }}</td>
#                     </tr>
#                 </table>
#             </div>
#         </div>
#     </div>
# </div>
#
# <div class="row">
#     <div class="col-md-12">
#         <h2>Product Details</h2>
#         <div class="box">
#             <div class="box-body">
#                 <table class="table">
#                     <thead>
#                         <tr>
#                             <th>Product</th>
#                             <th>Price</th>
#                             <th>Quantity</th>
#                             <th>Total</th>
#                         </tr>
#                     </thead>
#                     <tbody>
#                         {% for line in quotation.quotationline_set.all %}
#                         <tr>
#                             <td>{{ line.product }}</td>
#                             <td>{{ line.price }}</td>
#                             <td>{{ line.quantity }}</td>
#                             <td>{{ line.quantity|mul:line.price|floatformat:2 }}</td>
#                         </tr>
#                         {% endfor %}
#                         <tr>
#                             <td colspan="3" align="right"><strong>Sub Total:</strong></td>
#                             <td>{{ quotation.quotationline_set.all|mul:'price*quantity'|add:0|floatformat:2 }}</td>
#                         </tr>
#                     </tbody>
#                 </table>
#             </div>
#         </div>
#     </div>
# </div>
#
#
# {% endblock %}
