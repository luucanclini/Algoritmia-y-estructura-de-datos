from math import isclose

def resta(nro1, nro2):
    if type(nro1) not in {float,int}:
        raise Exception("Argumento 1 mal")
    # Idem el segundo argumento queda de deber
    return nro1 - nro2

#-------------------------------
# Programo los test unitarios:
if __name__ == "__main__":
    print("Test 1: resta(10, 7) da 3?:", end="")
    if resta(10,7) == 3: print("Ok")
    else: print("Mal")

    print("Test 2: resta(23, 90) da -67: ", end="")
    if resta(23,90) == -67: print("ok")
    else: print("Mal")

    print("Test 3: resta(10.0, 7.0) da 3.0?: ", end="")
    if isclose(resta(10.0,7.0), 3.0): print("Ok")
    else: print("Mal")

    print("Test 4: resta(5, 3) da 2:")
    assert resta(5,3) == 2

    
