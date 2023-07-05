from django import template

register = template.Library()

@register.filter(name='back_stepper')
def back_stepper(stored_number,step_by):
    return int(stored_number-step_by)

@register.filter(name='forward_stepper')
def back_stepper(stored_number,step_by):
    return int(stored_number+step_by)


