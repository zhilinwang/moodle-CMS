#!/usr/bin/env python2.7
#coding=utf-8
class MediaWrapper:
    media={
        'text':'{"id":"%d","mood":"%s","type":"%s","content":"%s"}',
        'pic':'{"id":"%d","mood":"%s","type":"%s","url":"%s"}',
        'vedio':'{"id":"%d","mood":"%s","type":"%s","url":"%s"}'
    }
    def template(self,t):
        return self.media[t]
        
