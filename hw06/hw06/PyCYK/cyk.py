###############################################
# module: cyk.py
# YOUR NAME
# YOUR A-#
###############################################

class CYK(object):

    @staticmethod
    def is_in_cfl(test_string, cnfg):
        # Initialize D table
        D = [[set() for i in range(len(test_string))] for n in range(len(test_string))]
        # Base Case
        for i in range(len(test_string)):
            D[i][0] = (cnfg.fetch_lhs(test_string[i]))
        # Dynamic programming
        for l in range(1, len(test_string)):
            for s in range(0, len(test_string) - l):
                for k in range(0, l):
                    var1 = D[s][k]
                    var2 = D[s + k + 1][l - k - 1]
                    productions = [cnfg.fetch_lhs(i, j) for i in var1 for j in var2 if(len(cnfg.fetch_lhs(i,j)) > 0)]
                    for production in productions:
                        D[s][l].update(production)

        return 'S' in D[0][len(test_string) - 1]

