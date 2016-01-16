# -*- coding:utf-8 -*-

from simpletor import application
from demo import services
import ast

@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.render_json({'hello': 'world'})


@application.RequestMapping("/serviceList/myServiceList")
class MyServiceListHandler(application.RequestHandler):
    def post(self):
        params = ast.literal_eval(self.request.body)
        print(params)
        page = params.get('currentpage')
        if page is None:
            page = 1
        size = params.get('maxresult')
        print(page, size)
        self.render_json(services.getMyMtServcieList(int(page), int(size)))

@application.RequestMapping("/mtType/mtTypeListByUser/(.*)")
class MyMtTypesHandler(application.RequestHandler):
    def get(self, user_id):
        print(user_id)
        self.render_json(services.getMyMtTypes())

@application.RequestMapping("/meeting/mtInfo/([0-9a-z-]+)/xx")
class MtInfoTest(application.RequestHandler):
    def get(self, mt_id):
        print(mt_id)
        self.render_json({mt_id: mt_id})

@application.RequestMapping("/meeting/mtInfo/(.*)")
class MtInfo(application.RequestHandler):
    def get(self, mt_id):
        print(mt_id)
        self.render_json(services.getMtById(mt_id))

