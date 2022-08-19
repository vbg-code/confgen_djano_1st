from django.shortcuts import render

# Create your views here.

# def home_page(request):
#     return render(request, template_name = "home_page.html")

def home_page(request):

    if request.method == 'POST':
        snow_req_id = request.POST['snow_req_id']
        project_vrf = request.POST['project_vrf']
        new_wan_vlan_id = request.POST['new_wan_vlan_id']
        ip_new_wan = request.POST['ip_new_wan']

        list = ip_new_wan.split('.')

        list[-1] = str(int(list[-1]) + 1)
        wan_ip_rt1 = '.'.join(list)

        list[-1] = str(int(list[-1]) + 1)
        bgp_ip_rt1 = '.'.join(list)

        list[-1] = str(int(list[-1]) + 1)
        wan_ip_rt2 = '.'.join(list)

        list[-1] = str(int(list[-1]) + 1)
        bgp_ip_rt2 = '.'.join(list)

        context = {'snow_req_id': snow_req_id,
                   'project_vrf': project_vrf,
                   'new_wan_vlan_id': new_wan_vlan_id,
                   'ip_new_wan': ip_new_wan,
                   'wan_ip_rt1': wan_ip_rt1,
                   'bgp_ip_rt1': bgp_ip_rt1,
                   'wan_ip_rt2': wan_ip_rt2,
                   'bgp_ip_rt2': bgp_ip_rt2
                   }

        return render(request, "script_page.html", context)

    else:
        return render(request, "home_page.html")


def script_page(request):
    return render(request, "script_page.html")

