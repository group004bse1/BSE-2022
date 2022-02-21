def compute_grade():
    try:
        v = float(input("what is your score?"))
        if v > 1.0:
            print("invalid score")
        elif v < 0.0:
            print("oops score is below range")
        elif v >= 0.9:
            print("A")
        elif v >= 0.8:
            print("B")
        elif v >= 0.7:
            print("C")
        elif v >= 0.6:
            print("D")
        elif v < 0.6:
            print("F")
    except:
        print("bad score")
compute_grade()