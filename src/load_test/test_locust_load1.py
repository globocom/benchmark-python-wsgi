#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import Locust, TaskSet, task


class VirtuosoTasks(TaskSet):

#    def on_start(self):
#        self.client.post("/login", {
#            "username": "test_user",
#            "password": ""
#        })

    @task
    def get(self):
        self.client.get("/")

    @task(10)
    def post(self):
        self.client.post("/")

    @task
    def delete(self):
        self.client.delete("/")

    @task
    def get_after_delete(self):
        self.client.get("/")

class VirtuosoUser(Locust):
    task_set = VirtuosoTasks
    min_wait = 5000
    max_wait = 15000
