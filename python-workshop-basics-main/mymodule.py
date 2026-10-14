def keys_values(keys, values):
    d = {}
    for k in keys:
       d[k] = values[keys.index(k)]
       if len(values) != len(keys):
           print("Error: Lists must have the same length.")
    return d