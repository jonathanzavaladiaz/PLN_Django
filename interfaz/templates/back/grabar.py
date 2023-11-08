import os
from django.http import JsonResponse

def procesar_audio(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']

        # Guardar el archivo en el sistema de archivos
        archivo_path = os.path.join('media', 'audio', audio_file.name)
        with open(archivo_path, 'wb') as file:
            for chunk in audio_file.chunks():
                file.write(chunk)

        # Aquí puedes hacer lo que necesites con el archivo de audio
        # Por ejemplo, procesar el audio, analizarlo, etc.

        return JsonResponse({'mensaje': 'Archivo de audio procesado exitosamente.'})

    return JsonResponse({'error': 'Se esperaba un archivo de audio en la solicitud POST.'}, status=400)
