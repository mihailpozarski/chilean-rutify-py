@staticmethod
def valid_rut_value(value):
        valid_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "k", "K", ".", "-"]
        return str(value) in valid_values

@staticmethod
def get_verifier(raw_rut):
    rut = normalize_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return None

    sum = 0
    mul = 2

    for i in reversed(rut):
        sum += int(i) * mul
        mul = 2 if mul == 7 else mul + 1

    res = sum % 11

    return translate_verifier_result(res)

@staticmethod
def translate_verifier_result(result):
    if result == 1:
        return "K"
    elif result == 0:
        return "0"
    else:
        return str(11 - result)

@staticmethod
def valid_rut_verifier(raw_rut):
    rut = normalize_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return False

    r = rut[:-1]
    return get_verifier(r) == rut[-1]

@staticmethod
def normalize_rut(raw_rut):
    rut = stringify_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return None

    rut = rut.replace(".", "").replace("-", "")
    return rut.upper()

@staticmethod
def dash_only_rut(raw_rut):
    rut = normalize_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return None

    return f"{rut[:-1]}-{rut[-1]}"

@staticmethod
def classic_rut(raw_rut):
    rut = normalize_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return None

    verifier = rut[-1]
    temp_rut = rut[:-1]
    init_rut = ""

    while len(temp_rut) > 3:
        init_rut = f".{temp_rut[-3:]}{init_rut}"
        temp_rut = temp_rut[:-3]

    return f"{temp_rut}{init_rut}-{verifier}"

@staticmethod
def format_rut(raw_rut, format="classic"):
    rut = stringify_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return None

    if format == "normalized":
        return normalize_rut(rut)
    elif format == "dash_only":
        return dash_only_rut(rut)
    elif format == "classic":
        return classic_rut(rut)

@staticmethod
def valid_rut(raw_rut):
    rut = normalize_rut(raw_rut)
    if not rut or not valid_rut_values(rut):
        return False

    return valid_rut_verifier(rut)

@staticmethod
def valid_rut_values(raw_rut):
    rut = stringify_rut(raw_rut)
    if not rut:
        return False

    return all(valid_rut_value(i) for i in rut)

@staticmethod
def stringify_rut(raw_rut):
    if raw_rut is None or not isinstance(raw_rut, (str, int)):
        return None

    return str(raw_rut)