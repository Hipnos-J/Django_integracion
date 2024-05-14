from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    # Recuperar todas las tareas y subtareas
    tareas = Tarea.objects.all()
    sub_tareas = SubTarea.objects.all()

    # Convertir a formato deseado (por ejemplo, lista de diccionarios)
    tareas_data = [{'id': tarea.id, 'descripcion': tarea.descripcion} for tarea in tareas]
    sub_tareas_data = [{'id': sub_tarea.id, 'descripcion': sub_tarea.descripcion, 'tarea_id': sub_tarea.tarea_id} for sub_tarea in sub_tareas]

    return {'tareas': tareas_data, 'subtareas': sub_tareas_data}

def crear_nueva_tarea(descripcion):
    # Crear nueva tarea
    nueva_tarea = Tarea(descripcion=descripcion)
    nueva_tarea.save()

    # Recuperar y devolver todas las tareas y subtareas
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(descripcion, tarea_id):
    # Crear nueva subtarea asociada a la tarea especificada
    nueva_sub_tarea = SubTarea(descripcion=descripcion, tarea_id=tarea_id)
    nueva_sub_tarea.save()

    # Recuperar y devolver todas las tareas y subtareas
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    # Eliminar tarea por ID
    Tarea.objects.filter(id=tarea_id).delete()

    # Recuperar y devolver todas las tareas y subtareas
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id):
    # Eliminar subtarea por ID
    SubTarea.objects.filter(id=sub_tarea_id).delete()

    # Recuperar y devolver todas las tareas y subtareas
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(data):
    # Imprimir en pantalla las tareas y subtareas de forma ordenada
    for tarea in data['tareas']:
        print(f"[{tarea['id']}] {tarea['descripcion']}")
        for sub_tarea in data['subtareas']:
            if sub_tarea['tarea_id'] == tarea['id']:
                print(f"\t[{sub_tarea['id']}] {sub_tarea['descripcion']}")
