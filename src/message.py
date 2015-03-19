# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'


class message:
    def __init__(self, token_priority, message_data, t_destination, t_source):
        self.priority_list = token_priority
        self.data = message_data
        self.destination = t_destination
        self.source = t_source

