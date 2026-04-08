def is_student(user):
    return user.role == 'student'

def is_workplace_supervisor(user):
    return user.role == 'workplace_supervisor'

def is_academic_supervisor(user):
    return user.role == 'academic_supervisor'

def is_admin(user):
    return user.role == 'admin'