#Models imports
from apps.notas.models import Notas

def hayNota(pk):
    try:
        notas = Notas.objects.get(id=pk)
        return True, notas 
    except:
        return False