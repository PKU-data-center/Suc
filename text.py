#-*- coding:utf-8 -*-

import urllib
import urllib2
import re
import tool
import os

#抓取网易公开课类
class Spider:

    #页面初始化,获取首页内容
    def _init_(self):
        self.siteURL = 'http://open.163.com'
        url = self.siteURL
        request = urllib2.request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gb2312')

    #获取首页所有课程信息
    def getContents(self):    
        pattern = re.compile('<a.*?href="http://open.163.com/(.*?)".*?>(.*?)</a>')
        detailPages = re.findall(pattern,self)
        contents = []
        for detailPage in detailPages:
            contents.append(detailPage[0])
        return detailPage

    #获取课程具体详情页面
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('gb2312')

    #获取课程介绍
    def getBrief(self,infoURL):
        pattern = re.compile('<p>课程介绍</p><p>(.*?)</p>')
        result = re.search(pattern,infoURL)
        return result.group(1)

    # #获取课程列表
    # def getBrief(infoURL):
    #     pattern = re.compile('')
    #     result = re.search(pattern,infoURL)
    #     return result.group(1)

    # #获取跟帖
    # def getBrief(infoURL):
    #     pattern = re.compile('')
    #     result = re.search(pattern,infoURL)
    #     return result.group(1)

    # #获取讲师介绍
    # def getBrief(infoURL):
    #     pattern = re.compile('')
    #     result = re.search(pattern,infoURL)
    #     return result.group(1)

    #保存课程名称
    def saveCourseName(self,content):
        fileName = "spider.txt"
        f = open(fileName,"w+")
        f.write(content.encode('utf-8'))

    #保存课程简介
    def saveCourseBrief(self,content):
        fileName = "spider.txt"
        f = open(fileName,"w+")
        f.write(content.encode('utf-8'))

    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        #判断路径是否存在
        #存在 True
        #不存在 False
        isExists = os.path.isExists(path)
        #判断结果
        if not isExists:
            #如果不存在则创建目录
            print "新建",path,"的文件夹"
            #os.makedirs(path)
            return True
        else:
            #如果目录存在则不创建，并提示目录已存在
            print "名为",path,"的文件夹已经创建成功"
            return False

    #保存信息
    def savePageInfo(self):
        #获取网易公开课首页信息
        contents = self.getContents()
        for item in contents:
            print "发现",item[1],"的一个网址：",itme[0]
            #获取课程具体详情URL
            detailURL = item[0]
            #获取课程具体详情页面代码
            detailPage = self.getDetailPage(detailURL)
            #获取课程介绍
            brief = self.getBrief(detailPage)

            self.mkdir("spider.txt")
            #保存课程名称
            saveCourseName(item[1])
            #保存课程介绍
            saveCourseBrief(brief)
spider = Spider()
spider.savePageInfo()        
