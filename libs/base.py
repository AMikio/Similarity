def sqrt(x):
    return x**.5

def mean(vec):
    return sum(vec)/len(vec)

def dotProd(vec1, vec2):
    return sum([x*y for x,y in zip(vec1,vec2)])

def vMod(vec):
    return sqrt(sum([x**2 for x in vec]))

def stdDev(vec):
    m = mean(vec)
    result = sum([(x - m)**2 for x in vec])
    result = sqrt(result/len(vec))
    return result

def coVar(vec1, vec2):
    m1 = mean(vec1)
    m2 = mean(vec2)
    result = sum([(x-m1)*(y-m2) for x, y in zip(vec1, vec2)])
    result = result/len(vec1)
    return result
    
def simCos(vec1, vec2):
    return dotProd(vec1, vec2)/(vMod(vec1)*vMod(vec2))

def pCor(vec1, vec2):
    covariance = coVar(vec1, vec2)
    std1 = stdDev(vec1)
    std2 = stdDev(vec2)
    return covariance/(std1*std2)
