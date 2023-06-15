def G(x):
    if x in [1,2,3,4]:
        return 1
    else:
        return G(x-1)+G(x-2)+G(x-3)+G(x-4)
        
