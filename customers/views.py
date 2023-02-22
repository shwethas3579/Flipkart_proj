import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from customers.models import Customer


@csrf_exempt
def createCustomer(request):
	body = request.body   # json object
	data = json.loads(body)  # dict object
	dob = data['dob']   # string dob
	dob_obj = datetime.datetime.strptime(dob, '%d-%m-%Y')  # datetime obj
	# Django ORM query to create a record in database
	Customer.objects.create(
		first_name=data['first_name'],
		last_name=data['last_name'],
		mobile=data['mobile'],
		email=data['email'],
		dob=dob_obj,
		address=data['address'],
		age=data['age']
	)
	# return HttpResponse("created successfully")
	response = {
		'message': 'created successfully',
		'status code': 200,
	}
	return JsonResponse(response)

def home(request):
	return HttpResponse("I am in customer app")

def get_customer(request):
	id = request.GET.get('id')
	# Django ORM query to get data
	try:
		obj = Customer.objects.get(id=id)
		# return HttpResponse("Name is Diwakar, and he is a developer")
		response = {
			'name': obj.first_name + obj.last_name,
			'age': obj.age,
			'email': obj.email,
			'mobile': obj.mobile
		}
		return JsonResponse(response, safe=False)
	except:
		return HttpResponse("Object does not exists")

@csrf_exempt
def delete_customer(request):
	id = request.GET.get('id')
	obj = Customer.objects.get(id=id)
	obj.delete()
	return HttpResponse("customer is deleted")

@csrf_exempt
def update_customer(request):
	id = request.GET.get('id')
	body = request.body   # json object
	data = json.loads(body)  # dict object
	obj = Customer.objects.get(id=id)
	obj.mobile = data['mobile']
	obj.address = data['address']
	obj.save()
	return HttpResponse("customer is updated")


# class Custopmer(APIView):
# 	serializer_class = CustomerSerializer
#
# 	def get(self,request):
# 		data = Customer.objects.get(id=5)
# 		serializer_obj = CustomerSerializer(data)
# 		serializer_obj.is_valid()
# 		serializer_obj.save()
# 		return JsonResponse(serilizer_obj)


class CustomerSerializer(models.modelserializerr):
	first_name = serializer.charfield

	class meta:
		model = Customer

	def validate(self,data):
		raise validationerror("")
