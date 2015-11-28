#-*- coding:utf-8 -*-

import sys
import urllib
import urllib2
import re
import tool
import os

#抓取khan公开课类
class Spider:
	#页面初始化
    def __init__(self):
        self.siteURL = 'http://open.163.com/khan/'
        self.tool = tool.Tool()

    def getPage(self):
        try:
            url = self.siteURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"Fail",e.reason
                return None

	#获取索引页面所有课程信息
    def getContents(self):  
        page = self.getPage() 
        pattern = re.compile('<div class="g-cell1 g-card1">.*?<a href="(.*?)" .*?',re.S)
        items = re.findall(pattern,page)
        if items:
        	contents = []
        	for item in items:
        		contents.append(item)
        	return contents
        else:
        	print null
        	return None

    #获取课程具体详情页面
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read()

    #获取课程名称
    def getCourseName(self,page):
        pattern = re.compile('<div class="m-cdes">.*?<h2>(.*?)</h2>',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None
		
    #获取课程讲师
    def getTeacher(self,page):
        pattern = re.compile('<div class="m-cteacher">.*? ',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    #获取课程简介
    def getBrief(self,page):
        pattern = re.compile('<div class="m-cdes">.*?</h2>(.*?)<b>',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    #获取课程列表
    def getCourseList(self,page):
        pattern = re.compile(' <td class="u-ctitle">.*?(.*?)<a href=.*?>(.*?)</a>',re.S)
        list = re.findall(pattern,page)
        if list:
        	contents = []
        	for li in list:
        		contents.append([li[0],li[1]])
        	return contents 
        else:
        	return None

    #获取跟帖人数
    def getTieShow(self,page):
        pattern = re.compile('<div class="tie-titlebar">.*?<a href.*?>(.*?)</a>',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None        
           
    #保存信息
    def saveInfo(self):
        contents = self.getContents() 
        for item in contents:
            print "find",item
            #获取课程具体详情URL
            detailURL = item
            #获取课程具体详情页面代码
            detailPage = self.getDetailPage(detailURL)
            #获取课程名称
            name = self.getCourseName(detailPage)
            #获取课程简介
            brief = self.getBrief(detailPage)
            print brief 
            #保存课程名称
            if(name != None):
                f.write("CourseName:" + name + '\n')
            #保存课程介绍
            if(brief != None):
                f.write("CourseBrief:" + brief + '\n')
            # teacher = self.getTeacher(detailPage)
            #获取课程列表
            list = self.getCourseList(detailPage
            if list:
            	for li in list:
            		li[0] = self.tool.replace(li[0])
            		f.write(li[0] + li[1] + '\n')
            #获取跟帖人数
            tiePerson = self.getTieShow(detailPage)
            
            # #保存课程讲师
            # if(teacher != None):
            #     f.write("CourseTeacher:" + teacher + '\n')        
            f.write('\n')

reload(sys)
sys.setdefaultencoding('utf-8')
f = open("khan.txt","w+")
spider = Spider()
spider.saveInfo()        
