#!coding=utf-8
import json
from locust import HttpLocust,TaskSet,task

#定义用户行为类
class Userbehavior(TaskSet):
    header = {'User-Agent': 'callmec/3.6.0 (iPhone; iOS 13.1.2; Scale/2.00)', 'c-br': 'iPhone 7','c-lng': '106.491219', \
                        'c-sv': '13.1.2', 'c-cv': '3.6.0', 'c-lat': '29.621786', 'c-ct': '2', 'c-ch': '667.000000','c-sr': '0', 'Accept-Language': 'zh-Hans-CN;q=1', \
                        'c-iv': '3.6.0', 'c-cw': '375.000000', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate','c-nw': '4G', \
                        'c-im': '4A0E5A73-665E-495B-9E93-6BA72FFC7154', 'c-st': '1', 'Content-Type': 'application/json'}
    #当每个模拟用户开始执行TaskSet类时，on_start函数被调用
    def on_start(self):
        self.login()

    def login(self):
        data = '{"clientId":"b7d0d62ea801c0056e41dc4c3dc9e706","loginType":1,"password":"WgeliiPxirTeoOSMy2grSve5SYfMPzORlSLbSb6DM2BTiPFYEsF2dwCFnyO\/zK3POWk2S1Q\/NlH8ElIHWhmqFUTKWDjqPcgFWQmCyk8WBHOrVYJ\/H+z4k9sP1RkKBGhLzRF5tca7SHGj9IG2f13my\/x9m0iQAUbb2ebDxR4yOB0=",\
                "imei":"4A0E5A73-665E-495B-9E93-6BA72FFC7154","currLongitude":"106.491235","source":1000012,"currLatitude":"29.621850","mac":"02:00:00:00:00:00","loginName":"15703034351"}'
        response_data = self.client.post('/api/membership/login',data=data,headers=self.header)
        res = response_data.content
        res = json.loads(res)
        print(res)
        dt = res['data']
        self.header['token'] = dt['token']
        print(self.header['token'])

    @task(1) #@task操作符声明该方法是一个事务.可选的权重参数，用于说明任务执行的比率
    def test_findRecommendLine(self): #一个用户行为
        #查询推荐线路
        data = '{"eLatitude":"29.557204","eLongitude":"106.577034","endArea":"重庆市-重庆市-渝中区","sLatitude":"29.62190200000001",\
                "sLongitude":"106.4912350000001","startArea":"重庆市-重庆市-渝北区","version":"2.0"}'
        response_data = self.client.get('/api/trip/findRecommendLine',data=data,headers=self.header)
        print(response_data.status_code)
        print(response_data)

#Locust类代表一个用户(一个准备出动的蝗虫)。Locust会为每一个模拟用户生成一个locust类实例。同时会有一些locust类属性被定义。
class Websiteuser(HttpLocust):
    task_set = Userbehavior #该属性定义一个用户行为类
    max_wait = 1500 #该属性表示一个模拟用户将会在每个任务执行时的等待执行的时间间隔(ms)
    min_wait = 1000
    #wait_time = between(1,1.500)
    #weight = 3 该属性属性表示数量权重
    host = 'http://shuitupaycallbackpre.callme.work' #命令行中是需要通过--host来指定的,如果host属性在文件中被声明，则在命令行中则不需要再次声明

