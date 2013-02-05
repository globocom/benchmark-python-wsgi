#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import Locust, TaskSet, task

class WebsiteTasks(TaskSet):
    def on_start(self):
        pass
        #        self.client.post("/login", {
        #            "username": "test_user",
        #            "password": ""
        #        })

    @task
    def index(self):
        self.client.get("/")

#    @task
#    def about(self):
#        self.client.get("/about/")

class WebsiteUser(Locust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
