'''
 * @FileDescription: functions for api views
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''
def check_key(request, response, set=False):
    if set or request.headers['Key'] == 'Admin':
        response['Key'] = 'Admin'
    else:
        response['Key'] = 'Visitor'


def set_key(request, response, next=True, set=False):
    if set or (next and 'Key' in request.headers):
        check_key(request,response,set)
    else:
        response['Key'] = 'Visitor'
    response['Access-Control-Expose-Headers'] = "key,set-cookie"
    return response