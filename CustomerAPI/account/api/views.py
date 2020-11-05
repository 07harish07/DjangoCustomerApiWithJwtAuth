from rest_framework import generics, permissions, response, status
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from account.api.serializers import CustomerSerializer
from account.models import Customer
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from account.api.serializers import UserSerializer, RegisterSerializer, LogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["post"])
@permission_classes([permissions.AllowAny])
def registration(request):
	serializer = RegisterSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	user = serializer.save()
	refresh = RefreshToken.for_user(user)
	res = {
		"refresh": str(refresh),
		"access": str(refresh.access_token),
	}
	return Response(res, status=status.HTTP_201_CREATED)

@api_view(['GET'])
# @csrf_exempt
def UserListView(request):
	try:
		user = User.objects.all()
		serializer = UserSerializer(user, many=True)
		return Response(serializer.data)
	except User.DoesNotExist:
		return Response({'Response':'Customer Not exist'})


# Views for Customer Personal Details
@api_view(['GET'])
# @csrf_exempt
def CustomerListView(request):
	try:
		customers = Customer.objects.all()
		serializer = CustomerSerializer(customers, many=True)
		return Response(serializer.data)
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})
		
@api_view(['GET'])
# @csrf_exempt
def CustomerDetailView(request, id):
	try:
		customers = Customer.objects.get(id=id)
		serializer = CustomerSerializer(customers, many=False)
		return Response(serializer.data)
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})

@api_view(['POST'])
# @csrf_exempt
def CustomerCreateView(request):
	
	serializer = CustomerSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
# @csrf_exempt
def CustomerUpdateView(request, id):
	try:
		customer = Customer.objects.get(id=id)
		serializer = CustomerSerializer(instance=customer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})


@api_view(['DELETE'])
# @csrf_exempt
def CustomerDeleteView(request, id):
	try:
		customer = Customer.objects.get(id=id)
		customer.delete()

		return Response('Item Successfully Deleted!')
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})



class LogoutAPIView(generics.GenericAPIView):
	serializer_class = LogoutSerializer

	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({'Response':'You are loggedout Successfully'}, status=status.HTTP_204_NO_CONTENT)


