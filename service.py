#!user/bin/python3
import tornado.web #tornado的基础web框架
import tornado.ioloop #核心io循环模块
#RequestHandler：封装对请求处理的所有信息和处理方法
#get/post/..：封装对应的请求方式

#定义处理类型
class IndexHandler(tornado.web.RequestHandler):
    #添加一个处理get请求方式的方法
    def get(self):
        #向响应中添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一')

if __name__ == '__main__':
    #创建一个应用对象
    app = tornado.web.Application([(r'/',IndexHandler)])
    #绑定一个监听端口
    app.listen(8888)
    #启动web程序，开始监听端口的连接
    # current()返回当前线程的IOLoop实例对象,start()启动IOLoop实力对象的IO循环，开启监听
    tornado.ioloop.IOLoop.current().start()
    #httpserver监听端口
    #tornado.httpserver.HTTPServer(app)
    #httpserver.listen(port)
    #httpserver实现多进程操作
    #tornado.httpserver.HTTPServer(app)
    #httpserver.bind(port)
    #httpserver.start(0 / None / < 0 / num)