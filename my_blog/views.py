from django.shortcuts import render
from airtable import Airtable
import os
# Create your views here.
AT = Airtable('appDpdZWtRgNqFRW7','blog','keyxFd1DgOAHee1jv')

def home_page(request):
	user_query = str(request.GET.get('search_post', ''))
	search_result = AT.get_all(formula=("FIND('" + user_query.lower() + "', LOWER({Post_name}))"))
	all_results = AT.get_all()
	stuff_for_frontend = {'search_result': search_result, 'all_results': all_results}
	return render(request, "blog/blog_stuff.html", stuff_for_frontend)
	
def pages(request, post_id):
	detail_result = AT.get(post_id)
	all_results = AT.get_all()
	stuff_for_frontend1 = {'detail_result1': detail_result, 'all_results': all_results}
	return render(request, "blog/pages.html", stuff_for_frontend1)