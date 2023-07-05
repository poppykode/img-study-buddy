import json
from django.shortcuts import get_object_or_404
from accounts.models import User
def has_session(request,session_key):
    if session_key in request.session:
        return True
    return False

def delete_sessions(request,keys):
    for key in keys:
        if key in request.session:
            del request.session[key]

def delete_a_file(request,session_key,fs,form_number):
    file_name = ''
    if has_session(request,session_key):
        if form_number==1:
            file_name = deserialise_(request.session[session_key])['profile_picture_name']
    if fs.exists(file_name):
        fs.delete(file_name)


def deserialise_(obj):
    return json.loads(obj)

def serialise_(obj):
    return json.dumps(obj)

def complete_registration(request,keys):
    delete_sessions(request,keys)
    is_coach_accepted =True
    user_=request.user
    if user_.is_coach:
        is_coach_accepted = False
    user = get_object_or_404(User,id=request.user.id)
    user.is_registration_complete = True
    user.is_coach_accepted = is_coach_accepted
    user.save()


