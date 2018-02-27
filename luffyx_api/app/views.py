from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views
from rest_framework import serializers

from app import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"
        depth = 1
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = "__all__"
        depth = 1
    def get_level_display(self,obj):
        return self.level
class CourseView(views.APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            courses=models.CourseDetail.objects.get(course_id=pk)
            obj = CoursesSerializer(instance=courses)

            ret = {
                'code': "1000",
                'courses': obj.data,
                'name':models.Course.objects.get(id=pk).name,
                'level':models.Course.objects.get(id=pk).level
            }
        else:
            course_list = models.Course.objects.all()
            obj = CourseSerializer(instance=course_list, many=True)
            ret = {
                'code': 1000,
                'courseList': obj.data
            }
        response = Response(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response
