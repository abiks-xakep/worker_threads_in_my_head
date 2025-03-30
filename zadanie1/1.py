answer = input("tempis20+?").strip().lower()
temperature1 = answer == "da"
if temperature1:
    answer = input("osadki?").strip().lower()
    is_rainy = answer == "da"
    if is_rainy:
        print("futbolka/shorts/dojdevik")
    else:
        print("futbolka/shorts")
else:
    answer = input("tempbolshe8?").strip().lower()
    temp8 = answer == "da"
    if temp8:
        answer = input("osadki?").strip().lower()
        is_rainy2 = answer == "da"
        if is_rainy2:
            answer = input("Silnye?").strip().lower()
            is_raining_heavely = answer == "da"
            if is_raining_heavely:
                print("pal'to, rezin sapogi, zont")
            else:
                print("pal'to & dojdevik")
        else:
            print("pal'to")
    else:
        print("puhovik")
input("\n нажми на кнопку и получишь смс (ENTER)")
