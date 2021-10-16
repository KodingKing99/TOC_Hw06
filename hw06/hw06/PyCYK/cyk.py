###############################################
# module: cyk.py
# YOUR NAME
# YOUR A-#
###############################################

class CYK(object):

    @staticmethod
    def is_in_cfl(test_string, cnfg):
        print("Hello World!")
        print(test_string)
        print("printing cnfg")
        print(cnfg)
        print(f"Test String Length: {len(test_string)}")
        # Create Table
        D = [[0 for i in range(len(test_string))] for n in range(len(test_string))]
        print(D)
        # Initialize the table, D[s,l] -> D[i, 0] x at s length of 1.
        for i in range(len(test_string)):
            D[i][0] = (cnfg.fetch_lhs(test_string[i]))
        print(D)
        print("Doing table stuff")
        for l in range(1, len(test_string)):
            for s in range(0, len(test_string) - l):
                for k in range(0, l):
                    print(f"D[{s + 1}][{l + 1}] = D[{s + 1}][{k + 1}] X D[{s + k + 2}][{l - k}]")

                
            # d[i][]

        pass

