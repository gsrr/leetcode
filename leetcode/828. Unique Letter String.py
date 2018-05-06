import collections


def ans1(S):
    base = 10 ** 9 + 7
    cnt = 0
    for i in xrange(len(S)):
        hist = collections.defaultdict(int)
        unique = 0
        for j in xrange(i + 1, len(S) + 1):
            if hist.has_key(S[j - 1]):
                if hist[S[j - 1]] == 1:
                    unique -= 1
            else:
                unique += 1
            cnt += unique
            cnt = cnt % base
            hist[S[j - 1]] = True
    return cnt
    
import collections

def repeat(chist, c):
    arr = chist[c]
    if len(arr) == 1:
        return 2 * (arr[0] - 0 + 1)

    return 2 * (arr[-1] - arr[-2]) + 1 * (arr[-2] - 0 + 1)


def ans2(S):
    if len(S) == 0:
        return 0

    base = 10 ** 9 + 7
    carr = [0] * len(S)
    carr[0] = 1
    chist = collections.defaultdict(list)
    chist[S[0]].append(0)
    for i in xrange(1, len(S)):
        if chist.has_key(S[i]) == False:
            carr[i] = carr[i - 1] + i + 1
        else:
            carr[i] = carr[i - 1] + i + 1 - repeat(chist, S[i])
        carr[i] = carr[i] % base
        chist[S[i]].append(i)
    
    cnt = 0
    for i in xrange(len(carr)):
        cnt += carr[i]
        cnt = cnt % base
    return cnt
        

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        return ans2(S)    


s = Solution()
ex = "AAA"
print s.uniqueLetterString(ex)
ex = "ABC"
print s.uniqueLetterString(ex)
ex = "ABA"
print s.uniqueLetterString(ex)
ex = "MJYMRNGBCJUBGLTXGEJPICIKALQHJYWISCTXWFMAAAWNZIACGDWCXGYFPUZRQTAQOHJDBDMEOYZWRSREFEFHIXQVDRVRYNIFLMGSDDRIHHZLTWWHYYDBHZOBHMWYPGONRMYZVSPMFVMSTKMIZVJYDTDSFGCWEOMAECKRZLLZVCGQZGPJNUWCNQRDEDQCNEMIGRHISNNQOZQDVGEFINCTWIPMZVRPURGIQRUJTEOQDEVAGDIMXZTIXRHLPTGBFWKMGUFWJPEAOSZPIAHPYPQHGHCYVARQLTIQPCPNPOUEFXYXDMQATGCRJTOKADWCWUIGAVNANEBFXQCFTDVDRWZRETCFPMSIYMAPCTUGZNVWULWHREFLMFQZUIXJSXWCTGSOZYOJRBDOLSFEKORWXEFVLPKIKUEBJHUBLPUXCIGLMVSYSIWQCDXVXCLNXLFRVDYCDLTUTSOYXQRUGJNSXJUHPPQTCESCIIJIFSGMXBYWLPTWILLPRBAHIGRTWAFRTUQGPPAWCPTEROBWIQCJPVUAAUVYBVQWJFBVXAHRMFDGIBTWUJBNRGQMTLRLOXUKVRZIPPVXZCBJEKYHKCGGDYMVCZYNZDJVQURXNFAJMCLRRAXBYXFRRPKVCRYITAUMKVAOZULXWPTSFVJSYLLLVOSYLUMFJFPRVMPUDRMCWLIINEQNNJQRFFFOAPGRFUCXUSXHCVBBLANUNVSVMFZHAAXRZTCNUCDPIUHNODOMEEGLTOLYVAOQQPQJHUQLAFSJIGNMRNFFAFVNGWAMFVEUNCFVMVNXXWXDXOSNOHFWYBXDFMWNALQNBXAEVRRMYOAXZRNJHYWYFVSTNDSEWNLLHRTWSVXENKSCBIVIJFQNYSAMCKZOYFNAPUOTMDEXZKKRPMPPTTFICZERDNDSSUVEOMPQKEMTBWBODRHWSFPBMKAFPWYEDPCOWRUNTVYMXTYYEJQTAJKCJAKGHTDWMUYGECJNCXZCXEZGECRXONNSZMQM"
print s.uniqueLetterString(ex)
