S = input()
if S[0] == "0" or S[0] == "1":
    if S[1] == "0" or S[1] == "1" or S[1] == "2":
        if S[2] == "0" or S[2] == "1":
            if  S[3] == "0" or S[3] == "1" or S[3] == "2":
                print("AMBIGUOUS")
            else:
                print("MMYY")
        else:
            print("MMYY")
    else:
        if S[2] == "0" or S[2] == "1":
            if  S[3] == "0" or S[3] == "1" or S[3] == "2":
                print("YYMM")
            else:
                print("YYMM")
        else:
            print("NA")
else:
    if S[2] == "0" or S[2] == "1":
            if  S[3] == "0" or S[3] == "1" or S[3] == "2":
                print("YYMM")
            else:
                print("NA")
    else:
        print("Na")