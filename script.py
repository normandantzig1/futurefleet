from futureFleet.models import Comic, Blog  # Import the model classes we just wrote.

Comic.objects.all()

from django.utils import timezone

c = Comic(comic_title_text="Welcome Aboard", comic_pub_date=timezone.now(),
comic_location="/home/tapplebaum/Desktop/django/djangoFutureFleet/mysite/futureFleet/static/futureFleet/images1.jpg", comic_explanation_text="this is the first comic" )
