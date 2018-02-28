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


class CourseDetiailSerializer(serializers.ModelSerializer):
    oftenaskedquestion=serializers.SerializerMethodField()
    class Meta:
        model = models.CourseDetail
        fields = "__all__"
        depth = 1

    def get_oftenaskedquestion(self, obj):
        ret = []
        for i in models.OftenAskedQuestion.objects.all():
            if i.content_object==obj.course:
                print('ok')
                ret.append({'question':i.question,'answer':i.answer})
        return ret
class CourseChapterSerializer(serializers.ModelSerializer):
    coursesections=serializers.SerializerMethodField()
    class Meta:
        model = models.CourseChapter
        fields = "__all__"
        depth = 1

    def get_coursesections(self,obj):
        ret=[]
        for i in obj.coursesections.all():
            ret.append({'name':i.name,'video_time':i.video_time})
        return ret

class CourseView(views.APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            courses = models.CourseDetail.objects.get(course_id=pk)
            courses_obj = CourseDetiailSerializer(instance=courses)

            coursechapterList=models.CourseChapter.objects.filter(course_id=pk)
            coursechapter_obj=CourseChapterSerializer(instance=coursechapterList,many=True)

            ss=models.OftenAskedQuestion.objects.get

            ret = {
                'code': "1000",
                'courses': courses_obj.data,
                'name': models.Course.objects.get(id=pk).name,
                'level': models.Course.objects.get(id=pk).get_level_display(),
                'coursechapterList':coursechapter_obj.data

            }
        else:
            course_list = models.Course.objects.all()
            for i in course_list:
                i.level = i.get_level_display()
            obj = CourseSerializer(instance=course_list, many=True)
            ret = {
                'code': 1000,
                'courseList': obj.data,

            }
        response = Response(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response
