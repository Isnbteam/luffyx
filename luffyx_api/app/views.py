from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from . import models

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
        depth = 2

class NewsView(views.APIView):

    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk:
            article = models.Article.objects.filter(pk=pk).first()
            ser = NewsSerializers(instance=article,many=False)
            response = JsonResponse(ser.data,safe=False)
        else:
            article_list = models.Article.objects.all()
            ser = NewsSerializers(instance=article_list, many=True)
            print(ser.data)
            response = JsonResponse(ser.data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'  # 允许的请求头
        return response

    def put(self,request,*args,**kwargs):
        article_id = request.GET.get('article_id')
        agree_num = request.GET.get('agree_num')
        agree_info = request.GET.get('agree_info')

        article_col_id = request.GET.get('article_id')
        collect_num = request.GET.get('collect_num')
        collect_msg = request.GET.get('collect_msg')
        collect = request.GET.get('collect')
        if collect_msg:
            # 证明是收藏
            user = models.Account.objects.filter(pk=1).first()
            collect_msg = models.Article.objects.filter(pk=article_col_id).update(collect_num=collect_num)
            models.Collection.objects.create(account=user)
            if collect_msg:
                if collect:
                    ret = {"msg":"收藏成功"}
                    response = JsonResponse(ret)
                else:
                    ret = {"msg":"取消收藏成功"}
                    response = JsonResponse(ret)
            else:
                ret = {"msg":"收藏失败"}
                response = JsonResponse(ret)
            response['Access-Control-Allow-Origin']= '*'
            response['Access-Control-Allow-Headers'] = '*'  # 允许的请求头
            return response

        else:
            agree_msg = models.Article.objects.filter(pk=article_id).update(agree_num=agree_num)
            if agree_msg:
                if agree_info:
                    ret = {"msg":"点赞成功"}
                    response=JsonResponse(ret)

                else:
                    ret = {"msg":"取消点赞成功"}
                    response = JsonResponse(ret)
            else:
                ret = {"msg":"点赞失败"}
                response = JsonResponse(ret)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = '*'  # 允许的请求头
            return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        return response


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        depth = 1

class CommentView(views.APIView):

    def get(self, request, *args, **kwargs):
        comment_list = models.Comment.objects.all()
        ser = CommentSerializers(instance=comment_list, many=True)
        response = JsonResponse(ser.data,safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'  # 允许的请求头
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'  # 允许的请求头
        response['Access-Control-Allow-Methods'] = '*'
        # return response
        return response













