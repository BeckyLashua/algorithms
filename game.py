import math

def game_topdown(N):    
    cache = {}
    def helper(n, cache):
        if cache.get(n) != None:
            return cache[n]
        for i in (range(1, n)):
            if n % i == 0:
                if not helper(n-i, cache):
                    if i % 2 == 0:
                        print(i)
                    #cache[n] = True
                    return True
        #cache[n] = False
        return False
    
    return helper(N, cache)
  
     

print(game_topdown(50))