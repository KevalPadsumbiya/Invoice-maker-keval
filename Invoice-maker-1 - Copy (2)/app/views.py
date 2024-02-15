from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import requests
import os

import json
from django.views.decorators.csrf import csrf_exempt
from blank_django.settings import BASE_DIR

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

import datetime
#Opens up page as PDF
class ViewPDF(View):


	def get(self, request, *args, **kwargs):

		data = {
			"party_name" : "" + request.GET['party_name'],
			"address" : "" + request.GET['address'],
			# "tel" : "" + request.GET['tel'],
			"gstno" : "" + request.GET['gstno'],
			"date" : "" + request.GET['date'],
			# "pan_no" : "" + request.GET['pan_no'],
			# "invoice_type" : "" + request.GET['invoice_type'],
			"invoice_no" : "" + request.GET['invoice_no'],
			# "transport_mode" : "" + request.GET['transport_mode'],
			# "invoice_date" : "" + request.GET['invoice_date'],
			# "truck_no" : "" + request.GET['truck_no'],
			# "reverse_charge" : "" + request.GET['reverse_charge'],
			# "lr_no" : "" + request.GET['lr_no'],
			# "state_1" : "" + request.GET['state_1'],
			# "code_1" : "" + request.GET['code_1'],
			# "e_way_bill_1" : "" + request.GET['e_way_bill_1'],
			# "name_left" : "" + request.GET['name_left'],
			# "name_right" : "" + request.GET['name_right'],
			# "add_left" : "" + request.GET['add_left'],
			# "add_right" : "" + request.GET['add_right'],
			# "gst_left" : "" + request.GET['gst_left'],
			# "gst_right" : "" + request.GET['gst_right'],
			# "state_left" : "" + request.GET['state_left'],
			# "code_left" : "" + request.GET['code_left'],
			# "state_right" : "" + request.GET['state_right'],
			# "code_right" : "" + request.GET['code_right'],
			# "e_way_bill_left" : "" + request.GET['e_way_bill_left'],
			# "e_way_bill_right" : "" + request.GET['e_way_bill_right'],
			# "qty_type" : "" + request.GET['qty_type'],
			# "sr_no" : "" + request.GET['sr_no'],
			# "pr_desc" : "" + request.GET['pr_desc'],
			# "hsn_code" : "" + request.GET['hsn_code'],
			# "grade" : "" + request.GET['grade'],
			"qty" : request.GET['qty'],
			"rate" : request.GET['rate'],
			"total" : request.GET['total'],
			# "total1" : request.GET['total1'],
			"CGST" : request.GET['CGST'],
			"SGST" : request.GET['SGST'],
			# "IGST" : request.GET['IGST'],
			"sgst" : request.GET['sgst'],
			"cgst" : request.GET['cgst'],
			# "igst" : request.GET['igst'],
			"round_off" : request.GET['round_off'],
			# "grand_total" : request.GET['grand_total'],
			"grand_total_in_words" : "" + request.GET['grand_total_in_words'],
			# "acc_no" : "" + request.GET['acc_no'],
			# "ifsc_code" : "" + request.GET['ifsc_code'],
		}

		
		data['date']=datetime.datetime.strptime(data['date'], "%Y-%m-%d").strftime("%d / %m / %Y")
		data['font_url'] =  "/app/PTSans-Regular.ttf"
		pdf = render_to_pdf('app/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

class CreateResume(View):
	def post(self, request, *args, **kwargs):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		print(data)
		pdf = render_to_pdf('app/resume_template.html', {})
		return HttpResponse(pdf, content_type='application/pdf')

def index(request):
	context = {}
	print("base dir: ",BASE_DIR + '/PTSans-Regular.ttf')
	files = [ f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR,f)) ]
	print("files in base dir: ", files)
	return render(request, 'app/index.html', context)