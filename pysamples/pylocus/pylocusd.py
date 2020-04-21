#!/usr/bin/env python3

"""
https://github.com/mdjdot/Python-100-Days/blob/master/Day91-100/96.软件测试和自动化测试.md
https://www.locust.io/
https://docs.locust.io/en/latest/installation.html
"""

from locust import HttpLocust, TaskSet, task
class UserBehavior(TaskSet):
    @task
    def baidu_index(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 30000
    max_wait = 60000

"""
locust -f pylocusd.py --host=https://www.dotcore.xyz.com
http://localhost:8089/

"""
    