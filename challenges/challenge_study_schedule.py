def study_schedule(permanence_period, target_time):
    # Retorne a quantidade de estudantes presentes para uma entrada específica;
    # Retorne None se em permanence_period houver alguma entrada inválida;
    # Retorne None se target_time recebe um valor vazio;
    if target_time is None:
        return None
    best_time = 0
    for start, end in permanence_period:
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        if start <= target_time <= end:
            best_time += 1

    return best_time
