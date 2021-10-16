###############################################
# module: cyk.py
# YOUR NAME
# YOUR A-#
###############################################

class CYK(object):

    @staticmethod
    def is_in_cfl(test_string, cnfg):
        # print("Hello World!")
        # print(test_string)
        # print("printing cnfg")
        # print(cnfg)
        # print(f"Test String Length: {len(test_string)}")
        # Create Table
        D = [[set() for i in range(len(test_string))] for n in range(len(test_string))]
        # print(D)
        # Initialize the table, D[s,l] -> D[i, 0] x at s length of 1.
        for i in range(len(test_string)):
            D[i][0] = (cnfg.fetch_lhs(test_string[i]))
        # print(D)
        # print("Doing table stuff")
        for l in range(1, len(test_string)):
            for s in range(0, len(test_string) - l):
                for k in range(0, l):
                    # print("For my head: ")
                    # print(f"D[{s + 1}][{l + 1}] = D[{s + 1}][{k + 1}] X D[{s + k + 2}][{l - k}]")
                    # print("For my computer: ")
                    # print(f"D[{s}][{l}] = D[{s}][{k}] X D[{s + k + 1}][{l - k - 1}]")
                    var1 = D[s][k]
                    var2 = D[s + k + 1][l - k - 1]
                    # print(f"{var1} X {var2}")
                    productions = [cnfg.fetch_lhs(i, j) for i in var1 for j in var2 if(len(cnfg.fetch_lhs(i,j)) > 0)]
                    # for i in var1:
                    #     for j in var2:
                    #         if(len(cnfg.fetch_lhs(i, j)) > 0):
                    #             productions.append(cnfg.fetch_lhs(i, j))
                    # for()
                    # print(f"new productions: {productions}")
                    for production in productions:
                        D[s][l].update(production)
                    
        # print(f"D: {D}")
        return 'S' in D[0][len(test_string) - 1]


                
            # d[i][]

        pass

