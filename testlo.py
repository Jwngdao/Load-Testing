from locust import HttpLocust, TaskSet, task, SequentialTaskSet,HttpUser,constant,clients

class MyReqRes(SequentialTaskSet):
    @task
    def get_users(self):
        res=self.client.get('/')
        print('Get Methos Status is',res.status_code)
    @task
    def get_post_status(self):
        res=self.client.post('/?status=success')
        print('Post Methos Status is', res.status_code)
class MyReqTest(HttpUser):
    wait_time= constant(1)
    host='https://bmsuat.trsc.nic.in/bms/'

    tasks = [MyReqRes]


