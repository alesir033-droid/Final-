#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
        
    import django
    django.setup()
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'አዲስ_ጠንካራ_ፓስወርድ123')
        print("=== Superuser 'admin' created successfully! ===")

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
