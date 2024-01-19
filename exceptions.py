
def f(extract_options:dict):
    #1
    if "process" in extract_options:
        print(extract_options["process"])

    # RAU: nu folosim try except pentru flow control
    # Anathema
    try:
        extract_options["process"]
    except:
        ????


    # 3 ftw
    print(extract_options.get("process", None))

