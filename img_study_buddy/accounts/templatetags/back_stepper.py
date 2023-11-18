from django import template
import datetime as dt

register = template.Library()

@register.filter(name='back_stepper')
def back_stepper(stored_number,step_by):
    return int(stored_number-step_by)

@register.filter(name='forward_stepper')
def back_stepper(stored_number,step_by):
    return int(stored_number+step_by)

@register.filter(name='count_mgs')
def count_mgs(stored_list):
    return len(stored_list)

@register.filter(name='summations')
def summations(stored_list,option):
    date_today = dt.date.today()
    match option:
        case 'total_users':
            return len(stored_list)
        case 'total_active_user':
            return len(stored_list.filter(is_active = True))
        case 'total_inactive_user':
            return len(stored_list.filter(is_active = False))
        case 'total_candidates':
            return len(stored_list.filter(is_candidate=True))
        case 'total_candidates_active':
            return len(stored_list.filter(is_candidate=True).filter(is_active = True))
        case 'total_candidates_inactive':
            return len(stored_list.filter(is_candidate=True).filter(is_active = False))
        case 'total_coaches':
            return len(stored_list.filter(is_coach=True))
        case 'total_coaches_active':
            return len(stored_list.filter(is_coach=True).filter(is_active = True))
        case 'total_coaches_inactive':
            return len(stored_list.filter(is_coach=True).filter(is_active = False))
        case 'accepted':
            return len(stored_list.filter(is_coach=True).filter(account_status = 'accepted'))
        case 'rejected':
            return len(stored_list.filter(is_coach=True).filter(account_status = 'rejected'))
        case 'pending':
            return len(stored_list.filter(is_coach=True).filter(account_status = 'pending'))
        case 'accepted_meeting':
            return len(stored_list.filter(was_meeting_accepted = True))
        case 'unattended':
            return len(stored_list.filter(was_meeting_accepted = None).filter(was_meeting_rejected=None).filter(was_meeting_attended=None).filter(was_meeting_cancelled=None))
        case 'total_meetings':
            return len(stored_list)
        case 'cancelled_meetings':
            return len(stored_list.filter(was_meeting_accepted = True).filter(was_meeting_cancelled=True))
        case 'rejected_meetings':
            return len(stored_list.filter(was_meeting_rejected=True))
        case 'attended_meetings':
            return len(stored_list.filter(was_meeting_accepted = True).filter(was_meeting_attended = True).filter(date__lt=date_today))
        case _:
            return 0


