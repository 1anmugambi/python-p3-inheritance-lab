#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, info):
        self.knowledge.append(info)
        pass