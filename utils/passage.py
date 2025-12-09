from passageidentity import Passage
from django.conf import settings
from core.authUser.models import User

psg = Passage(
    app_id=settings.PASSAGE_APP_ID,
    api_key=settings.PASSAGE_API_KEY,
)

def authenticate_passage(request):
    try:
        p_user = psg.authenticate_request(request)

        if not p_user:
            return None

        passage_id = p_user.id
        email = p_user.email

        user, created = User.objects.get_or_create(
            passage_user_id=passage_id,
            defaults={"email": email},
        )

        return user

    except Exception:
        return None
