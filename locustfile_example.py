# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task

class GetHomePageTask(TaskSet):
    @task()
    def get_home_page(self):
        '''
        Gets /
        '''
        self.client.get("/")
    
    @task()
    def get_another_page(self):
        '''
         Post /
        '''
        response=self.client.post("/post", {"username":"password"})
 class GetAnotherTask(TaskSet):
    @task()
    def get_my_page(self):
        '''
        Calling sub domains
        '''
        self.client.get("/About")
        
        
class WebsiteUser(HttpLocust):
    task_set = GetHomePageTask
    min_wait = 0
    max_wait = 0
