import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') # Change 'project' if your folder name is different

application = get_wsgi_application()

# This part runs exactly when Gunicorn boots up the live website
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', '1441')
        print("=== Live Superuser 'admin' created successfully! ===")
except Exception as e:
    print(f"Error creating superuser: {e}")
