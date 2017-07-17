class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
           if lo == hi:
               return [nums[lo]]
           return [ops[i](a, b)
                   for i in xrange(lo, hi)
                   for a in build(lo, i)
                   for b in build(i + 1, hi)]
        return build(0, len(ops))
