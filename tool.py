#-*- coding:utf-8 -*-
import re
 
#����ҳ���ǩ��
class Tool:
    #ȥ��img��ǩ,1-7λ�ո�,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #ɾ�������ӱ�ǩ
    removeAddr = re.compile('<a.*?>|</a>')
    #�ѻ��еı�ǩ��Ϊ\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #������Ʊ�<td>�滻Ϊ\t
    replaceTD= re.compile('<td>')
    #�����з���˫���з��滻Ϊ\n
    replaceBR = re.compile('<br><br>|<br>')
    #�������ǩ�޳�
    removeExtraTag = re.compile('<.*?>')
    #�����п���ɾ��
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()��ǰ���������ɾ��
        return x.strip()