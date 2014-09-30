def ExOh(str):
    o_count=str.count("o")
    h_count=str.count("x")
    if o_count==h_count:
        return "true"
    else:
        return "false"
