
from locust import  HttpLocust, TaskSet, task


# HttpLocust 这个类的作用是用来发送http请求的
# TaskSet   这个类是定义用户行为的，相当于loadrunnerhttp协议的脚本，jmeter里面的http请求一样，要去干嘛的
# task   这个task是一个装饰器，它用来把一个函数，装饰成一个任务，也可以指定他们的先后执行顺序


class JrTest(TaskSet):
    # 自己定义的类，继承TaskSet，也就是这个类是实现咱们要去请求什么的
    @task(1)  # 用task装饰器把这个函数装饰成一个咱们要执行的性能任务
    def index(self):  # 这个函数里面定义的是咱们要具体做的操作
        self.client.get('/')  # 请求这个url里面的哪个路径，如果是接口的话，就是哪个接口

    @task(2)
    def login(self):  # 登录
        self.client.post('/login', {'username': '13058019302', 'password': '123456'})
        # 发送post请求，第一个是路径，第二个这个接口的入参，账号和密码

class JrTestIndexUser(HttpLocust):
    # 这个类继承了HttpLocust，代表每个并发里面的每个用户
    task_set = JrTest  # 这个是每个用户都去干什么，指定了BestTest这个类，它就会每个用户去运行besttest这个类里面的方法
