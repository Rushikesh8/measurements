from accounts.models import UserProfile

def create_userprofile(*args,**kwargs) -> UserProfile:
    return UserProfile.objects.create(*args,**kwargs)

def get_userprofile(*args,**kwargs) -> UserProfile:
    return UserProfile.objects.get(*args,**kwargs)