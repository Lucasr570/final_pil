#Rest imports
from tkinter.messagebox import RETRY
from urllib import response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Models imports
from apps.notas.models import Notas

#Serializers imports
from apps.notas.api.serializers import NotasSerializer

#Helpers
from apps.notas.helpers.notaError import hayNota

# Create your views here.
class NotasApiView(APIView):
   
   def  get(self, request):
       """Retorna un listado con todos los heroes almacenados en la base"""
  
       notas = Notas.objects.all()
       notas_serializer = NotasSerializer(notas, many=True)
       
       return Response(
           data=notas_serializer.data,
           status=status.HTTP_200_OK,
        ) 
        
class CreateNotasApiView(APIView):
    
    def  post(self, request):
        '''Crea un nuevo registro/nota'''
        
        serializer = NotasSerializer(data=request.data, many=True)
        
        if serializer.is_valid():
            serializer.save()        
        
            data = {
                'message': 'La nota fue creada correctamente'
            }
            return Response(
                data = data,
                status = status.HTTP_201_CREATED
            )
            
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
 
class NotasDetailApiView(APIView):
    
    def get(self, request, pk):
        """Nos devuele informacion de una nota en particular"""
        
        try:
            notas = Notas.objects.get(pk=pk)
            notas_serializer = NotasSerializer(notas)
        
            return Response(
            data=notas_serializer.data,
            status=status.HTTP_200_OK,
            )
        except:
            data = {
                    'message': 'Nota no encontrada'
                }
        
            return Response(
                    data=data,
                    status=status.HTTP_400_BAD_REQUEST,
                )
             
    
    def put(self, request, pk):
        """Modifica informacion de una nota en particular"""
        
        notas = hayNota(pk)
        
        if hayNota(pk)[0]:
            notas_serializer = NotasSerializer(notas[1], data=request.data)
                
            if notas_serializer.is_valid():
                notas_serializer.save()       
                
                data = {
                        'message': 'La nota fue modificada correctamente'
                }
                
                return Response(
                        data=data,
                        status=status.HTTP_200_OK,
                ) 
                
        return Response(
            data=notas_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )    
    
    def delete(self, request, pk):
        """Elimina un registro"""
        
        notas = Notas.objects.get(pk=pk)
        notas.delete()
        
        data = {
                'message': 'La nota fue eliminada correctamente'
            }
       
        return Response(
                data=data,
                status=status.HTTP_200_OK,
            ) 
