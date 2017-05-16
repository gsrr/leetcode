def ComputePrefixFunction(needle):
       Pi = [0 for i in range(len(needle))]
       m = len(needle)
       Pi[0] = 0
       k = 0
       for q in range(1, m):
           while k > 0 and needle[k] != needle[q]:
               k = Pi[k - 1]
           if needle[k] == needle[q]:
               k = k + 1
           Pi[q] = k
       return Pi

print ComputePrefixFunction("abcdabab")
