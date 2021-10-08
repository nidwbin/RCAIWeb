'''
 * @FileDescription: functions for api views
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''
import datetime
import hashlib


class Authority:
    deadline = {}
    visitor = 'Visitor'

    @staticmethod
    def __gen_key__(now_time, delay=15):
        deadline = now_time + datetime.timedelta(minutes=delay)
        key = hashlib.sha256(str(now_time).encode('utf-8')).hexdigest()
        return deadline, key

    def __check_pass__(self, now_time, request):
        send_key = request.headers['key']
        return send_key in self.deadline and now_time <= self.deadline[send_key]

    def __set_key__(self, deadline, key, response):
        if key != self.visitor:
            self.deadline[key] = deadline
        response['key'] = key

    def __check_key__(self, request, response, keep=True, put=False):
        now_time = datetime.datetime.now()
        if put or (keep and 'key' in request.headers and self.__check_pass__(now_time, request)):
            deadline, key = self.__gen_key__(now_time)
            self.__set_key__(deadline, key, response)
        else:
            if self.deadline:
                self.deadline.clear()
            self.__set_key__(now_time, self.visitor, response)

    def get_response(self, request, response, keep=True, put=False):
        self.__check_key__(request, response, keep, put)
        response['Access-Control-Expose-Headers'] = "key,set-cookie"
        return response
