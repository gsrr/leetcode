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
    if token == "add":
        idx += 1
        v1 = eval2(tokens, dic) 
        v2 = eval2(tokens, dic)
        idx += 1
        return v1 + v2
    elif token == "mult":
        idx += 1
        v1 = eval2(tokens, dic) 
        v2 = eval2(tokens, dic)
        idx += 1
        return v1 * v2
    elif token == "let":
        tdic = copy.deepcopy(dic)
        idx += 1
        v1 = tokens[idx]
        while v1 != "(":
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
        return eval2(tokens, dic)
    elif token == ")":
        idx += 1
        return eval2(tokens, dic)
    else:
        idx += 1
        return str2int(token, dic)

def ans_1(expression):
    global idx
    idx = 0
    ret = 0
    tokens = get_tokens(expression)
    return eval2(tokens, {})


def is_int(token):
    try:
        int(token)
        return True
    except:
        return False

class Context:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.state = StartState()
        
    def get_token(self):
        return self.tokens[self.idx]
    
    def do(self, dic):
        return self.state.do(self, dic)
    
class State:
    def do(self, cxt, dic):
        pass

class StartState(State):
    def do(self, cxt, dic):
        token = cxt.get_token()
        if token == "(":
            cxt.idx += 1
        elif token == "add":
            cxt.state = AddState()
            cxt.idx += 1
        elif token == "mult":
            cxt.state = MultState()
            cxt.idx += 1
        elif token == "let":
            cxt.state = LetState()
            cxt.idx += 1
        elif token == ")":
            cxt.idx += 1
            return None
        elif is_int(token) == True:
            cxt.idx += 1
            return int(token)
        else:
            cxt.idx += 1
            return dic[token]
        return cxt.do(dic)
    
class AddState(State):
    def do(self, cxt, dic):
        token = cxt.get_token()
        cxt.state = StartState()
        v1 = cxt.do(dic)
        cxt.state = StartState()
        v2 = cxt.do(dic)
        cxt.idx += 1
        return v1 + v2

class MultState(State):
    def do(self, cxt, dic):
        token = cxt.get_token()
        cxt.state = StartState()
        v1 = cxt.do(dic)
        cxt.state = StartState()
        v2 = cxt.do(dic)
        cxt.idx += 1
        return v1 * v2

class LetState(State):
    def do(self, cxt, dic):
        tdic = copy.deepcopy(dic)
        while True:
            token = cxt.get_token()
            if token == "(":
                cxt.state = StartState()
                val = cxt.do(tdic)
                cxt.idx += 1
                return val
            if token == ")":
                pass
            v1 = token
            cxt.idx += 1
            cxt.state = StartState()
            v2 = cxt.do(tdic)
            if v2 == None:
                if is_int(v1) == True:
                    return int(v1)
                return tdic[v1]
            tdic[v1] = int(v2)
            
        
        
def ans_2(expression):
    tokens = get_tokens(expression)
    cxt = Context(tokens)
    dic = {}
    return cxt.do(dic)
    
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        return ans_2(expression)        
