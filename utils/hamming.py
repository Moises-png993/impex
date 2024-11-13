# hamming.py

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    distance = sum(1 for x, y in zip(str1, str2) if x != y)
    return distance

def find_most_similar(input_string):
    strings_list = [
        "SSNNNSNNNNNSS", "SSSNNNNNNNNSS", "SSSNNNSNNNNSS", "SSNNNNNNNNNSS",
        "NNNNNNNSSNNSS", "NNNNNNNSNNNSS", "NNNNSNNNNNNSS", "NNSNNSNNNNNSS",
        "NNSNNNNNNNNSS", "NNNNNSNNNNNSS", "NNNNNNNNNNNSS", "NNNNNNNSSNNLS",
        "NNNNNNNSNNNLS", "NNNNNNNNNSNLL", "NNNNNSNNNNNLS", "NNSNNNNNNNNLL",
        "NNNNNNNNNNNLL", "NNSSNNNNNNNLM", "NNSNNNNNNNNLS", "NNNSNNNNNNNLM",
        "NNNNNNNNNNNLS", "NNNNNNNSNNNTS", "NNNNNNNNNNSTS", "NNNNNNNNNNNTS",
        "NNNNNNNNNNNTL", "NNNNNNNNNNNLO", "NNNNNNNNNNNTO", "NNNNNNNNNNNOO",
        "NNNNNNNNNNNSO"
    ]   
    min_distance = float('inf')
    most_similar_string = ""

    for s in strings_list:
        distance = hamming_distance(input_string, s)
        if distance < min_distance:
            min_distance = distance
            most_similar_string = s

    return most_similar_string
