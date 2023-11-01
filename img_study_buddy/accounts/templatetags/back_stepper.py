from django import template

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
        case _:
            return 0


