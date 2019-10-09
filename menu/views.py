from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
 
from menu.serializers import OrderModelSerializer
from .models import OrderModel


class OrderListView(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        queryset = OrderModel.objects.all()
        query1 = self.request.GET.get('q')
        query2 = self.request.GET.get('id')
        if query1 is not None:
            queryset = queryset.filter(Q(thai_choice__icontains=query1)
                                       | Q(russian_choice__icontains=query1)
                                       | Q(french_choice__icontains=query1))
        elif query2 is not None:
            queryset = queryset.filter(Q(pk__iexact=query2))
        return queryset


class OrderUpdateDestroyDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = OrderModel.objects.all()

    def put(self, request, pk, *args, **kwargs):
        if request.method == "PUT":
            get_order = OrderModel.objects.get(id=pk)
            get_order.delete()
            new_data = self.request.data
            form1 = new_data.getlist('thai_choice')
            form2 = new_data.getlist('russian_choice')
            form3 = new_data.getlist('french_choice')
            updated_order = OrderModel(id=pk, thai_choice=form1, russian_choice=form2, french_choice=form3)
            updated_order.save()
        return Response("Order has been updated!", status=status.HTTP_201_CREATED,)


class OrderCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )
    serializer_class = OrderModelSerializer

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            form = request.POST
            form1 = form.getlist('thai_choice')
            form2 = form.getlist('russian_choice')
            form3 = form.getlist('french_choice')
            model = OrderModel(thai_choice=form1, russian_choice=form2, french_choice=form3)
            model.save()
        return Response("Order has been created!", status=status.HTTP_201_CREATED,)

