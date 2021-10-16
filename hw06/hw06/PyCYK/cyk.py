###############################################
# module: cyk.py
# Nick Sorenson
# A02287085
###############################################

class CYK(object):

    @staticmethod
    def is_in_cfl(test_string, cnfg, debug=False):
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
        if(debug):
            for tables in D:
                for productions in tables:
                    print(f'|{productions}|')
                print('\n')
        return 'S' in D[0][len(test_string) - 1]