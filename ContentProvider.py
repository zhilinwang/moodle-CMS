#/usr/bin/env python2.7
#coding=utf-8
import json
import random
import threading
from mediaWrapper import MediaWrapper
import logging
logger=logging.getLogger(__name__)
mw=MediaWrapper()
class ContentProvider:
    def __init__(self):
        if len(TextMedia.jokes)<=0 :
            TextMedia.load()
    def content(self,scores,**profiles):
        return TextMedia.Test(scores)

class TextMedia:
    jokes=[]
    instance=None
    def __init__(self):
        pass
    @staticmethod
    def load():
        fh=open('/root/moodevaluator/main/server/content-provider/xiaohua_Joke.txt','r')
        lines=fh.readlines()
        for line in lines:
            TextMedia.jokes.append(line)
        fh.close()
    @staticmethod
    def Test(scores):
        logger.info("Call test method")
        logger.info("joke length:%d" % len(TextMedia.jokes))
        t_score=sum(scores)
        joke_str=TextMedia.jokes[random.randint(0,len(TextMedia.jokes))]
        joke=json.loads(joke_str)
        content=joke['content'].strip()
        if t_score >0: 
            mood='happy' 
        if t_score<0: 
            mood='sad'
        if t_score ==0:
            mood='unknown'
        return json.loads(mw.template('text') % (random.randint(0,len(TextMedia.jokes)),mood,'text',content),strict=False)
        

class PicMedia:
    pass

class VedioMedia:
    pass


