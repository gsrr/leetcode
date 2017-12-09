import copy
from StringIO import StringIO
import tokenize

idx = 0

def str2int(val, dic):
    try:
        return int(val)
    except:
        return int(dic[val])

def get_tokens(exp):
    tokens = []
    ttokens = tokenize.generate_tokens(StringIO(exp).readline)
    sign = 1
    for toknum, tokval, _, _, _  in ttokens:
        if toknum == tokenize.ENDMARKER:
            break
        if toknum == tokenize.NUMBER:
            tokens.append(str(sign * int(tokval)))
            sign = 1
        elif toknum == tokenize.OP:
            if tokval == "-":
                sign = -1
            else:
                tokens.append(tokval)
        else:
            #print tokenize.tok_name[toknum], tokval
            tokens.append(tokval)
    return tokens

def eval2(tokens, dic):
    global idx
    if idx >= len(tokens):
        return 0

    token = tokens[idx]
    tdic = copy.deepcopy(dic)
    if token == "add":
        idx += 1
        v1 = eval2(tokens, tdic) 
        v2 = eval2(tokens, tdic)
        idx += 1
        return v1 + v2
    elif token == "mult":
        idx += 1
        v1 = eval2(tokens, tdic) 
        v2 = eval2(tokens, tdic)
        idx += 1
        return v1 * v2
    elif token == "let":
        idx += 1
        v1 = tokens[idx]
        while v1 != "(" and v1 != ")":
            if tokens[idx + 1] == ")":
                idx += 1
                return str2int(v1, tdic)
            idx += 1
            v2 = eval2(tokens, tdic)
            tdic[v1] = v2
            #print "let", v1, v2, tdic
            v1 = tokens[idx]
        return eval2(tokens, tdic)
    elif token == "(":
        idx += 1
        return eval2(tokens, tdic)
    elif token == ")":
        idx += 1
        return eval2(tokens, tdic)
    else:
        idx += 1
        return str2int(token, tdic)
        
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        global idx
        idx = 0
        ret = 0
        tokens = get_tokens(expression)
        #print tokens
        while idx < len(tokens):
            ret += eval2(tokens, {})
        return ret
