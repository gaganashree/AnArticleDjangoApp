# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from basicarticle.models import *
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os, sys, json
# Create your views here.


class CreateArticle(View):

	def get(self,request):
		return render(request, 'create_article.html')
	
	@csrf_exempt
	def post(self,request):
		#data = json.loads(request.body.decode('utf-8'))
		title = request.POST.get("title")
		author = request.POST.get("author")
		content = request.POST.get("content")
		print title, author, content
		#data = json.loads(request.body)
		article = Article()
		article.title = title#data["title"]
		article.content = author#data["content"]
		article.author = content#data["author"]
		article.save()
		resp = {}
		resp ["msg"] = 'Article Created'
		resp["article_id"] = article.id
		return HttpResponse("Article Created Successfully", content_type="text/plain")
		#return JsonResponse(resp)
		
#/basicarticle/article	
class Articles(View):	
	@csrf_exempt
	def get(self,request):
		articles = Article.objects.all().order_by('-votes')
		all_articles = []
		for article in articles:
			each_art = {}
			each_art['id'] = article.id
			each_art['title'] = article.title
			each_art['content'] = article.content
			each_art['votes'] = article.votes
			each_art['author'] = article.author
			all_articles.append(each_art)
		resp = {'articles':all_articles}	
		return render(request, 'article.html', resp)
		#return JsonResponse(resp)

#/basicarticle/upvote
class UpvoteArticle(View):
	@csrf_exempt
	def post(self,request):
		article_id = request.POST.get("article_id")
		print request.POST
		try:
			a = Article.objects.get(id = article_id)
		except:
			return JsonResponse({'msg':'Article object not found'})
		else:
			a.votes += 1
			a.save()
		resp = {}
		resp['msg'] = "Upvoted Article: %s, with id:%d Successfully"%(a.title,a.id)
		#return redirect('Articles')
		return JsonResponse(resp)
		
	
		

