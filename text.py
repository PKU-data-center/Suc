#-*- coding:utf-8 -*-

import sys
import urllib
import urllib2
import re
import tool
import os

#抓取顶你学堂类
class Spider:

    #页面初始化
    def __init__(self):
        self.siteURL = 'http://www.topu.com/kvideo.php'
        self.tool = tool.Tool()
        
    #获取索引页面的内容
    def getPage(self,pageIndex):
        try:
            url = self.siteURL + "?do=search&view=&classtype=&keyword=&renqi=&page=" + str(pageIndex)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"Fail",e.reason
                return None

    #获取索引页面所有课程信息
    def getContents(self,pageIndex):  
        page = self.getPage(pageIndex)  
        pattern = re.compile('<dt class="radiu_new"><a href="/mooc/(.*?)" .*?',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            str = item[0]+item[1]+item[2]+item[3]
            contents.append(str)
        return contents

    #获取课程具体详情页面
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('utf-8')

    #获取课程名称
    def getCourseName(self,page):
        pattern = re.compile('<a href="javascript:;" class="hover-col43 cover-title-width" title=.*?>(.*?)</a',re.S)
        result = re.search(pattern,page)
        return self.tool.replace(result.group(1))

    #获取课程讲师
    def getTeacher(self,page):
        pattern = re.compile('<div class="teacher-name-wrap">.*?<a href=.*?>(.*?)</a> ',re.S)
        result = re.search(pattern,page)
        return self.tool.replace(result.group(1))

    #获取课程简介
    def getBrief(self,page):
        pattern = re.compile('<div class="clear box course-description".*?>(.*?)<div class="aqb-feedback".*?',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else:
            return None

    #保存信息
    def saveInfo(self,pageIndex):
        #获取公开课首页信息
        contents = self.getContents(pageIndex) 
        for item in contents:
            print "find",item
            #获取课程具体详情URL
            detailURL = "http://www.topu.com/mooc/" + item
            #获取课程具体详情页面代码
            detailPage = self.getDetailPage(detailURL)
            #获取课程名称
            name = self.getCourseName(detailPage)
            teacher = self.getTeacher(detailPage)
            brief = self.getBrief(detailPage)
            #保存课程名称
            if(name != None):
                f.write("CourseName:" + name + '\n')
            #保存课程讲师
            if(teacher != None):
                f.write("CourseTeacher:" + teacher + '\n')
            #保存课程介绍
            if(brief != None):
                f.write("CourseBrief:" + brief + '\n')
            f.write('\n')
    #传入起止页码，获取课程信息
    def saveInfos(self,start,end):
        for i in range(start,end+1):
            print "Searching",i,"page"
            self.saveInfo(i)

reload(sys)
sys.setdefaultencoding('utf-8')
f = open("spider.txt","w+")
spider = Spider()
spider.saveInfos(1,25)        
