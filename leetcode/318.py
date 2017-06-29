

import itertools

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def factor(n):
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            ret.append(cnt)
            ops = n / cnt
            if cnt != 1 and ops != cnt:
                ret.append(ops)
        cnt += 1
    return ret

def binsearch(nums, n, l, h):  # nums is sorted array
    if h < l:
        return False
    mid = (l + h)/ 2
    if n < nums[mid]:
        return binsearch(nums, n , l, mid - 1)
    elif n > nums[mid]:
        return binsearch(nums, n , mid + 1, h)
    else:
        return True
    

def linsearch(nums, b):  # nums is sorted array
    for j in xrange(len(nums)):
        if b > nums[j]:
            continue
        elif b < nums[j]:
            return (j, False)
        else:
            return (j, True)
    return (len(nums), False)

def list2dic(nums):
    dic = {}
    for i in nums:
        if dic.has_key(i) == False:
            dic[i] = 0
        dic[i] = dic[i] + 1
    return dic

def list2dic_bool(nums):
    return { item:True for item in nums }

def bfs(a, index, hist):
    q = [index]  # init
    while len(q) != 0:
        i = q.pop(0)
        # do operation
        if hist[i] == 1:
            continue
        hist[i] = 1

        # post
        for j in xrange(len(a[i])):
            if a[i][j] == 1 and i != j:
                q.append(j)


def iter_combination(table, n):
    return itertools.combinations(table, n)

def iter_permutations(table, n):
    return itertools.permutations(table, n)

def dist(a,b):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    return x_diff * x_diff + y_diff * y_diff

def boomerangs(tup):
    if dist(tup[0], tup[1]) == dist(tup[0], tup[2]):
        return True
    else:
        return False

def isPalindrome(x):
    if x < 0:
        return False
    px = 0
    tmp = x
    while tmp != 0:
        r = tmp % 10
        tmp = tmp / 10
        px = (px * 10) + r
    return px == x


def alphaset(s):
    num = 0
    for w in set(s):
        num += (1 << (ord(w) - ord('a')))
    return num

def ans(x):
    x.sort(lambda a,b: cmp(len(a), len(b)), reverse = True)
    xcand = []
    rmax = 0
    for i in xrange(len(x)):
        cset = alphaset(x[i])
        find = False
        j = 0
        while j < len(xcand) and find == False:
            iset = xcand[j][0] & cset
            if iset == 0:
                find = True
                tmax = len(xcand[j][1]) * len(x[i])
                if tmax > rmax:
                    rmax = tmax
            j += 1

        if find == False:
            xcand.append((alphaset(x[i]),x[i] ))
    return rmax
cases = [
    [["ahdfkeooglkocgaahca","cjcnekogeekcdjndcbalajlkkpkameogadnooeco","pecoenfndnpmilfnanndaigodeknddhagjbpgpil","lnoclbhpellakbofkbjcbgc","indoafcjbjggpnnbkoombcedbcadohchjooggokegpgae","jmaeiamehk","nbiadhogogkdbhddobkboj","gncjlnpfapmmmgddejcegpi","bcfolfplbihbjppnoancnabmdbbjeniiaoiocmmjokkoegejghm","olmbdiemggamcchooikemdalcimdklhhllbpebplefpjj","cimgacihg","gjppkeaakcdkdfn","pdbfnhonglepijkaonejcdhce","okpaecdnlnl","iak","hiffchaalcpgikclcboehdjlhckanppnbjboidmjna","lbagjalkjdjdchkkmhllmicennamhohnpcoaijmhhpnbghg","gm","cffalejkmddbfaddkoakjnbelhohgjojhpcejpnjdikg","mbmenceobpcnopgpnfpkcihakbpnbaceiagnabiancndfim","gilaehpohoplbiapbpgidhiadgjhmkdfgifbepbjg","lealfoedklphfngfkabaocidfbnoomckkcnmkgcmkfloeinnidp","keckjahekiibnflgcnmpccffnbjdgdmcghbdacl","ffmfebpbbchlccbipcohhjiloblpkbh","ifpcpmohmoicchkbooelnfifgpjop","ahbknicdfhoaejlmbfgghkbehebojjekocc","cnbdflflbhmkpdnog","kkcojbjhnigebg","kaplhnnpahpenchemfkilm","ifjgdgffnnmogkbid","fmmhphhhbagjmcpgl","ginbpphjckmmbdcmbilomopmoekoebefngbaebboheghg","dgogj","jpbdioikbjcfjjhpdkmpbfjkgaepidnhjgoi","mfdhcngpdipefecbgaambahoeibkogppegjgbjokhlb","hbeacjed","hffmlffekc","lgamffcbbhidhhdpdjinoafkokhjagmdoobbpfeihggbbjiepa","bcojpalo","lnbccpceinip","ieihfokdmendmpbme","clgjgfamgibigkdeoedjogodjcnpcegbnhblgmoe","hnopnddaenekecjdaolgdcblpeadabjlkhegbejhpjcpg","aikpnjfpiflfjgdefgmeamojonecpbldaglepdfmmimb","cgkidedilhidelncihocchhknj","dmmebialbabibknafjkmmbaojmaeceflcoofeph","dmjajoapkhedlkhdlpoipgnfbckkopfhmkohkaidmmhfhopfaob","ecc","odjpjkliajafkmpgghlijdglgijpdhhhggehcaphia","hjccenngnippigpldehhgcfi","fpkiacjkdpgfmefplinjlfeka","pdpmhd","kemibdngd","inneplfamginonohlkc","ncpgdobiacfhanaigfiaojicbhimdjokonffnlgmb","jhaj","fciecoologieigmofacha","fifgm","mnmjkgmoppchejplobahhci","onhfmbiadkahjdnenbpb","iamibcjflikaoaooaapa","dhabelaamdgipildoklm","ndgpnc","ebejklakcckkcifcognccccmlbkgbc","fgadjeeaofdejebijeakpeilaakg","fgbabfhfkhmfkjcejkjgpfhkb","bjapbbejcfioafdmgjnlnklplohkmdbckbinneedleign","ljponiihopobmbfcama","mjgeafmihjedpcelmboooiomlhppmdjkbgdhphegmjjpnjcn","gjccaa","moldoebkhbopcjnka","lcjdkageabgjcoekmcngakhnolddeppjeffljnmojimc","cndhpedcjkeoj","bjaf","fmaiakpobidadacagdjciolgpcmdpaolhfifgpfnmjdlamphkoe","npgchhocjnmlgknocnggplpoalfbnebbnoijccmcf","fjicahfmoilagj","jigfnn","baoajdpplncicibplgphonlknbhfhnodcpcfnkoongn","iopjdocleepdmjiankcghhdilbn","ggnlmdcgahocagddf","kgjp","fgmegonchlgjaiomnhigmkdaphnbgldfomofgo","fjmjjfddami","pfjgoobapciblccododngkmmagfcoenjadkknajgegpmebl","lpgdknikhihpniofiajlmcedjdoobhjnedmbcgmdl","accfinmceehhfcepalceebjbbkheljmblfkpnaccdgognnkgol","pknlaphodmbmebaoohjm","imibhaho","cfaobakedkdmginfaipdmppbljbagade","ajlnflopllcbdnlhmdnngghhiinpccgbmpeiplee","oempnimiildekbojhoikfohepojdp","jfle","nbehigoaiajiehkefallcpogghafakbajcjcinopdkaoo","pfmmijhekakjmgoedpccecfkbhfndhgmlimjk","aijdecjlpckgcjecnffmhkg","bnpmammfi","gndieolenmhacknjc","kdjnfabldmoadggpocdlebpfcpincgojoi","blmgkmibbgckjgigkfomemaifdonlefjakgmmbeglhfmpilcho","afedfcpmlpbkkdkejenomfkablfemcblhfa","chhaldd","ghdbamcpbfkjlhd","hodbeifkopnmlefcofdoncgbpflkppkkdohlgkhidnffa","bjmcomefkeccjaijmccaigohioonhecbjgflfdaahbfipbcb","illaogplgknphedcmbckd","flccfnmnmgmhfigjpjajchhmmcdgojfaomn","milokaffgkpon","kdnppipoccjkgjhid","nagggnbljadacjabgmdlgblfpchoooeminlcdcjik","ogfhnegamebnlophjgnlohdfjjcmjpmnjjcicaboddjeimp","ppnpbcocbooikgcnldpadgfhojkjmgepciooci","babidndefmgjpfleadobfphbeafpannpgid","jppjheidmiihpefgnheadohfcplgjkkmkdnhelaklloangc","hidlkikmehgcajmngejogijpndaephkbjfemi","elnaeckmdjloaggbecaijilcpcgm","hfeopocboifjidfljmnffgbgomjnmohpjppppnfbo","efnanongblbebfagohocdhf","dkimpmlcbdgmnnbnocnnndehfijodogpeg","egfdnmkjemjfebhbpkhgkjjbhohgnbliaei","fjhincpp","fmgaelbieilfcokedged","ph","fpggfhmlmhlbhokfmchi","fi","hihcpgnbnhpialnmckegjhodjajlelacjoe","ekcbjdplhmflgmgaapnjiidjgjg","ggnkjeae","aadbikfahldinmkiohfehbkjlocjiddilinglaog"]]
]
test(cases,10)

