import os
import shutil
from django.http import HttpResponse
from .permissions import admin_or_staff_required

@admin_or_staff_required
def fazer_backup(request):
    origem = os.path.join(os.getcwd(), 'db.sqlite3')
    destino = os.path.join(os.getcwd(), 'temp', 'backup.sqlite')

    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copyfile(origem, destino)

    with open(destino, 'rb') as backup_file:
        response = HttpResponse(backup_file.read(), content_type='application/x-sqlite3')
        response['Content-Disposition'] = 'attachment; filename=backup.sqlite'
        return response
