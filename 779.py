N, K = map(int, input().split(" "))

def kthGrammar(self, N: int, K: int):
    if N==0:
        return 0
    else:
        if K%2==0:
            return 0 if self.kthGrammar(N-1, (k+1)//2) else 1
        else:
            return 1 if slrf.kthGrammar(N-1, (k+1)//2) else 0
