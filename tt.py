def g(s,s1):
    if s>=s1:
        print("ENTERED G()")
        s+=1

def f(s, s1):
    if s >= s1:

        print("---------------------------ENTERED FIRST CONDITION------------------------",s,
              "-------------------------------------------------------------------------------------------------------")

        s -= 1


    else:
        print("---------------------------------TERMINATED------------------", "X",
              "-------------------------------------------------------------------------------------------------------")

        return -1
    #g(s, s1)
    print("NOT TERMINATED")

    f(s, s1)
    print("PASSED FIRST RECURSIVE CALL")
    f(s, s1)
    print("PASS SECOND RECURISIVE CALL")
    #g(s, s1)
    #f(s,s1)
    #print("PASSED THIRD RECURISIVE CALL")




f(9, 3)


