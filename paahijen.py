BEGIN_ST = 0
CONSO_ST = 1
WOVEL_ST = 2
NUMBER_ST = 3
MN_ST = 4

# current lipi, index in the symbol table array. Default is devnagari
CURR_TBL = 1
CURR_LIPI = 2
SAVED_LIPI = CURR_LIPI

# llt - language lookup table is no longer a simple array but its an array of tuples,
# first indicates the index in the symlt and second indicates the offset of lang.
llt = [[0,0],   #/* english */
    [0,1],    #/* marathi */
    [0,1],    #/* hindi   */
    [0,2],    #/* gujarathi */
    [1,1],    #/* kannada */
    [1,2],    #/* Telugu */
    [1,3],    #/* Malayalam */
    [0,3],    #/* Bengali */
    [1,4],    #/* Tamil */
    [0,4],    #/* Punjabi */
    [0,5]]    #/* Oriya */
          

out_buff_arr = []
last_st = BEGIN_ST
sym_list = None

sym_list_d = {   
    'ai' : "process_wovel('ai','matra2')", 
    'au' : "process_wovel('au', 'matra4')", 
    'aa' : "process_wovel('aa', 'kanaa')",
    'A' : "process_wovel('A', 'kanaa')",
    'a'  : "process_wovel('a', None)",
    'ee' : "process_wovel('ee', 'matra11')", 
    'E' : "process_wovel('E', 'matra11')", 
    'e'  : "process_wovel('e', 'matra1')",
    'ii' : "process_wovel('ii', 'vel2')", 
    'I' : "process_wovel('I', 'vel2')", 
    'i'  : "process_wovel('i', 'vel1')", 
    'oo' : "process_wovel('oo', 'matra33')", 
    'O' : "process_wovel('O', 'matra33')", 
    'o'  : "process_wovel('o', 'matra3')",
    'uu' : "process_wovel('uu', 'ukar2')", 
    'u'  : "process_wovel('u', 'ukar1')", 
    'U'  : "process_wovel('U', 'ukar2')", 
    'Ha' : "process_wovel('Ha', 'halant')", 
    'M'  : "process_wovel('M', 'anuswar')", 
    'AM' : "process_wovel('AM', 'chandra3')", 
    'AN' : "process_wovel('AN', 'chandra3')",
    'c'  : "process_conso('c')",
    'k'  : "process_conso('k')",
    'kh' : "process_conso('kh')",
    'g'  : "process_conso('g')",
    'gh' : "process_conso('gh')",
    'Ng' : "process_conso('Ng')",

    # ch chh j jh nY 
    'ch' : "process_conso('ch')",
    'chh': "process_conso('chh')",
    'j'  : "process_conso('j')",
    'jh' : "process_conso('jh')",
    'z'  : "process_conso('z')",
    'nY' : "process_conso('nY')",
    
    # T Th D Dh N 
    'T'  : "process_conso('T')",
    'Th' : "process_conso('Th')",
    'D'  : "process_conso('D')",
    'Dh' : "process_conso('Dh')",
    'N'  : "process_conso('N')",
    
    # t th d dh n 
    't'  : "process_conso('t')",
    'th' : "process_conso('th')",
    'd'  : "process_conso('d')",
    'dh' : "process_conso('dh')",
    'n'  : "process_conso('n')",
    
    # p ph b bh m 
    'p'  : "process_conso('p')",
    'ph' : "process_conso('ph')",
    'f'  : "process_conso('f')",
    'b'  : "process_conso('b')",
    'bh' : "process_conso('bh')",
    'm'  : "process_conso('m')",
    
    # y r l v sh 
    'y'  : "process_conso('y')",
    'r'  : "process_conso('r')",
    'l'  : "process_conso('l')",
    'v'  : "process_conso('v')",
    'w'  : "process_conso('w')",
    'sh' : "process_conso('sh')",
    
    # Sh s h L  
    'Sh' : "process_conso('Sh')",
    's'  : "process_conso('s')",
    'h'  : "process_conso('h')",
    'L'  : "process_conso('L')",
    'Z'  : "process_conso('Z')",

    # rushi cha ru 
    'RU' :  "process_wovel('RU', None )", 
    'R'  :  "process_conso('R')",
    'Nn'  :  "process_conso('Nn')",
    'ruu':  "process_ru('ru', 'ukar2')",
    'ru' :  "process_ru('ru', 'ukar1')",
    '0'  :  "process_number('0')",
    '1'  :  "process_number('1')",
    '2'  :  "process_number('2')",
    '3'  :  "process_number('3')",
    '4'  :  "process_number('4')",
    '5'  :  "process_number('5')",
    '6'  :  "process_number('6')",
    '7'  :  "process_number('7')",
    '8'  :  "process_number('8')",
    '9'  :  "process_number('9')",
    '_'  :  "process_halant('_')" }
  
sym_list_a = {   'aa' : "process_wovel('aa', 'kanaa')",
    'ai' : "process_wovel('ai','matra2')", 
    'au' : "process_wovel('au', 'matra4')", 
    'a'  : "process_wovel('a', None)",
    'u'  : "process_wovel('u', 'ukar1')", 
    'U'  : "process_wovel('U', 'ukar1')", 
    'oo' : "process_wovel('oo', 'ukar2')", 
    'o'  : "process_wovel('o', 'matra3')",
    'Ha' : "process_wovel('Ha', 'halant')", 
    'M'  : "process_wovel('M', 'anuswar')", 
    'AM' : "process_wovel('AM', 'chandra3')", 
    'AN' : "process_wovel('AN', 'chandra3')",
    'A'  : "process_wovel('A', 'chandra1')",
    'O'  : "process_wovel('O', 'chandra2')",
    'e'  : "process_wovel('e', 'matra1')",
    'ee' : "process_wovel('ee', 'vel2')", 
    'i'  : "process_wovel('i', 'vel1')", 
    'c'  : "process_conso('c')",
    'k'  : "process_conso('k')",
    'kh' : "process_conso('kh')",
    'g'  : "process_conso('g')",
    'gh' : "process_conso('gh')",
    'Ng' : "process_conso('Ng')",

    # ch chh j jh nY
    'ch' : "process_conso('ch')",
    'chh': "process_conso('chh')",
    'j'  : "process_conso('j')",
    'jh' : "process_conso('jh')",
    'z'  : "process_conso('z')",
    'nY' : "process_conso('nY')",
    
    # T Th D Dh N
    'T'  : "process_conso('T')",
    'Th' : "process_conso('Th')",
    'D'  : "process_conso('D')",
    'Dh' : "process_conso('Dh')",
    'N'  : "process_conso('N')",
    
    # t th d dh n
    't'  : "process_conso('t')",
    'th' : "process_conso('th')",
    'd'  : "process_conso('d')",
    'dh' : "process_conso('dh')",
    'n'  : "process_conso('n')",
    
    # p ph b bh m
    'p'  : "process_conso('p')",
    'ph' : "process_conso('ph')",
    'f'  : "process_conso('f')",
    'b'  : "process_conso('b')",
    'bh' : "process_conso('bh')",
    'm'  : "process_conso('m')",
    
    # y r l v sh
    'y'  : "process_conso('y')",
    'r'  : "process_conso('r')",
    'l'  : "process_conso('l')",
    'v'  : "process_conso('v')",
    'w'  : "process_conso('w')",
    'sh' : "process_conso('sh')",
    
    # Sh s h L 
    'Sh' : "process_conso('Sh')",
    's'  : "process_conso('s')",
    'h'  : "process_conso('h')",
    'L'  : "process_conso('L')",

    # New letters 
    'F'  : "process_conso('F')", 
    'K'  : "process_conso('K')", 
    'Kh' : "process_conso('Kh')", 
    'G'  : "process_conso('G')", 
    'Z'  : "process_conso('Z')", 
    'Dd' : "process_conso('Dd')", 
    'DH' : "process_conso('DH')", 
    'Y'  : "process_conso('Y')", 

    # rushi cha ru
    'OM' :  "process_wovel('OM', None )", 
    'RU' :  "process_wovel('RU', None)", 
    'R'  :  "process_conso('R')",
    'Rlu':  "process_conso('Rlu')", 
    'roo':  "process_ru('ru', 'ukar2')",
    'ru' :  "process_ru('ru', 'ukar1')",
    '0'  :  "process_number('0')",
    '1'  :  "process_number('1')",
    '2'  :  "process_number('2')",
    '3'  :  "process_number('3')",
    '4'  :  "process_number('4')",
    '5'  :  "process_number('5')",
    '6'  :  "process_number('6')",
    '7'  :  "process_number('7')",
    '8'  :  "process_number('8')",
    '9'  :  "process_number('9')",
    '_'  :  "process_halant('_')" }
	
reg_table_a =r'({.*?})|(aa)|(ai)|(au)|(a)|(i)|(ee)|(e)|(u)|(U)|(oo)|(OM)|(o)|(Ha)|(M)|(AM)|(AN)|(A)|(O)|(kh)|(k)|(gh)|(g)|(Ng)|(chh)|(ch)|(c)|(jh)|(j)|(z)|(nY)|(Th)|(T)|(Dd)|(DH)|(Dh)|(D)|(N)|(th)|(t)|(dh)|(d)|(n)|(ph)|(p)|(f)|(bh)|(b)|(m)|(y)|(roo)|(ru)|(r)|(l)|(v)|(w)|(sh)|(Sh)|(s)|(h)|(L)|(RU)|(Rlu)|(R)|(F)|(Kh)|(K)|(G)|(Z)|(Y)|(0)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(_)|(\s+)|(\n)|(.)'
	
reg_table_d =r'({.*?})|(aa)|(ai)|(au)|(a)|(ee)|(e)|(E)|(ii)|(i)|(I)|(oo)|(o)|(O)|(uu)|(u)|(U)|(Ha)|(M)|(AM)|(AN)|(A)|(kh)|(k)|(gh)|(g)|(Ng)|(chh)|(ch)|(c)|(jh)|(j)|(z)|(nY)|(Th)|(T)|(Dh)|(D)|(Nn)|(N)|(th)|(t)|(dh)|(d)|(n)|(ph)|(p)|(f)|(bh)|(b)|(m)|(y)|(ruu)|(ru)|(r)|(l)|(v)|(w)|(sh)|(Sh)|(s)|(h)|(L)|(RU)|(R)|(Z)|(0)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(_)|(\s+)|(\n)|(.)'
	
	
sym_tbl_a = {
    # Wovels
    'a'    :  ['a', u'\u0905', u'\u0A85', u'\u0985', u'\u0A05', u'\u0B05'], 
    'aa'   :  ['aa', u'\u0906', u'\u0A86', u'\u0986', u'\u0A06', u'\u0B06'],
    'i'    :  ['i', u'\u0907', u'\u0A87', u'\u0987', u'\u0A07', u'\u0B07'], 
    'ee'   :  ['ee', u'\u0908', u'\u0A88', u'\u0988', u'\u0A08', u'\u0B08'],
    'u'    :  ['u', u'\u0909', u'\u0A89', u'\u0989', u'\u0A09', u'\u0B09'], 
    'U'    :  ['U', u'\u0909', u'\u0A89', u'\u0989', u'\u0A09', u'\u0B09'],
    'oo'   :  ['oo', u'\u090A', u'\u0A8A', u'\u098A', u'\u0A0A', u'\u0B0A'], 
    'e'    :  ['e', u'\u090F', u'\u0A8F', u'\u098F', u'\u0A0F', u'\u0B0F'],
    'ai'   :  ['ai', u'\u0910', u'\u0A90', u'\u0990', u'\u0A10', u'\u0B10'], 
    'o'    :  ['o', u'\u0913', u'\u0A93', u'\u0993', u'\u0A13', u'\u0B13'],
    'au'   :  ['au', u'\u0914', u'\u0A94', u'\u0994', u'\u0A14', u'\u0B14'],

    # Anuswaar will be handled in a different way
    'M'    :  ['M', u'\u0902', u'\u0A82', u'\u0982', u'\u0A70', u'\u0B02'], 
    'AN'   :  ['AN', u'\u0901', u'\u0A81', u'\u0981', u'\u0A02', u'\u0B01'],
    'AM'   :  ['AM', u'\u0901', u'\u0A81', u'\u0981', u'\u0A02', u'\u0B01'], 
    'Ha'   :  ['Ha', u'\u0903', u'\u0A83', u'\u0983', u'\u0A03', u'\u0B03'],
    'A'    :  ['A', u'\u090D', u'\u0A8D', u'\u0986', u'\u0A06', u'\u0B06'], 
    'O'    :  ['O', u'\u0911', u'\u0A91', u'\u0993', u'\u0A13', u'\u0B13'],

    'complete'  :  [ 'a', '', '', '', '', ''],
    'kanaa'  :  ['aa', u'\u093E', u'\u0ABE', u'\u09BE', u'\u0A3E', u'\u0B3E'], 
    'vel1'   :  ['i', u'\u093F', u'\u0ABF', u'\u09BF', u'\u0A3F', u'\u0B3F'],
    'vel2'   :  ['ee', u'\u0940', u'\u0AC0', u'\u09C0', u'\u0A40', u'\u0B40'], 
    'ukar1'  :  ['u', u'\u0941', u'\u0AC1', u'\u09C1', u'\u0A41', u'\u0B41'],
    'ukar2'  :  ['oo', u'\u0942', u'\u0AC2', u'\u09C2', u'\u0A42', u'\u0B42'], 
    'rukar'  :  ['ru', u'\u0943', u'\u0AC3', u'\u09C3', u'\u0A30\u0041', u'\u0B43'],
    'chandra1' :  ['A', u'\u0945', u'\u0AC5', u'\u09BE', u'\u0A4B', u'\u0B4B'], 
    'chandra2' :  ['O', u'\u0949', u'\u0AC9', u'\u09CB', u'\u0A3E', u'\u0B3E'],
    'chandra3' :  ['AM', u'\u0901', u'\u0A81', u'\u0981', u'\u0A02', u'\u0B01'], 
    'matra1' :  ['e', u'\u0947', u'\u0AC7', u'\u09C7', u'\u0A47', u'\u0B47'],
    'matra2' :  ['ai', u'\u0948', u'\u0AC8', u'\u09C8', u'\u0A48', u'\u0B48'], 
    'matra3' :  ['o', u'\u094B', u'\u0ACB', u'\u09CB', u'\u0A4B', u'\u0B4B'],
    'matra4' :  ['au', u'\u094C', u'\u0ACC', u'\u09CC', u'\u0A4C', u'\u0B4C'], 
    'anuswar' : ['M', u'\u0902', u'\u0A82', u'\u0982', u'\u0A70', u'\u0B02'],
    'halant' :  ['Ha', u'\u094D', u'\u0ACD', u'\u09CD', u'\u0A71', u'\u0B4D'],

    # k kh g gh Ng
    'c'    :  ['c', u'\u0915', u'\u0A95', u'\u0995', u'\u0A15', u'\u0B15'], 
    'k'    :  ['k', u'\u0915', u'\u0A95', u'\u0995', u'\u0A15', u'\u0B15'],
    'kh'   :  ['kh', u'\u0916', u'\u0A96', u'\u0996', u'\u0A16', u'\u0B16'], 
    'g'    :  ['g', u'\u0917', u'\u0A97', u'\u0997', u'\u0A17', u'\u0B17'],
    'gh'   :  ['gh', u'\u0918', u'\u0A98', u'\u0998', u'\u0A18', u'\u0B18'], 
    'Ng'   :  ['Ng', u'\u0919', u'\u0A99', u'\u0999', u'\u0A19', u'\u0B19'],

    # ch chh j jh nY
    'ch'   :  ['ch', u'\u091A', u'\u0A9A', u'\u099A', u'\u0A1A', u'\u0B1A'], 
    'chh'  :  ['chh', u'\u091B', u'\u0A9B', u'\u099B', u'\u0A1B', u'\u0B1B'],
    'j'    :  ['j', u'\u091C', u'\u0A9C', u'\u099C', u'\u0A1C', u'\u0B1C'], 
    'jh'   :  ['jh', u'\u091D', u'\u0A9D', u'\u099D', u'\u0A1D', u'\u0B1D'],
    'z'    :  ['z', u'\u091D', u'\u0A9D', u'\u099D', u'\u0A1D', u'\u0B1D'], 
    'nY'   :  ['nY', u'\u091E', u'\u0A9E', u'\u099E', u'\u0A1E', u'\u0B1E'],
    
    # T Th D Dh N
    'T'    :  ['T', u'\u091F', u'\u0A9F', u'\u099F', u'\u0A1F', u'\u0B1F'], 
    'Th'   :  ['Th', u'\u0920', u'\u0AA0', u'\u09A0', u'\u0A20', u'\u0B20'],
    'D'    :  ['D', u'\u0921', u'\u0AA1', u'\u09A1', u'\u0A21', u'\u0B21'], 
    'Dh'   :  ['Dh', u'\u0922', u'\u0AA2', u'\u09A2', u'\u0A22', u'\u0B22'],
    'N'    :  ['N', u'\u0923', u'\u0AA3', u'\u09A3', u'\u0A23', u'\u0B23'],
    
    # t th d dh n
    't'    :  ['t', u'\u0924', u'\u0AA4', u'\u09A4', u'\u0A24', u'\u0B24'], 
    'th'   :  ['th', u'\u0925', u'\u0AA5', u'\u09A5', u'\u0A25', u'\u0B25'],
    'd'    :  ['d', u'\u0926', u'\u0AA6', u'\u09A6', u'\u0A26', u'\u0B26'], 
    'dh'   :  ['dh', u'\u0927', u'\u0AA7', u'\u09A7', u'\u0A27', u'\u0B27'],
    'n'    :  ['n', u'\u0928', u'\u0AA8', u'\u09A8', u'\u0A28', u'\u0B28'],
    
    # p ph b bh m
    'p'    :  ['p', u'\u092A', u'\u0AAA', u'\u09AA', u'\u0A2A', u'\u0B2A'], 
    'ph'   :  ['ph', u'\u092B', u'\u0AAB', u'\u09AB', u'\u0A2B', u'\u0B2B'],
    'f'    :  ['f', u'\u092B', u'\u0AAB', u'\u09AB', u'\u0A2B', u'\u0B2B'], 
    'b'    :  ['b', u'\u092C', u'\u0AAC', u'\u09AC', u'\u0A2C', u'\u0B2C'],
    'bh'   :  ['bh', u'\u092D', u'\u0AAD', u'\u09AD', u'\u0A2D', u'\u0B2D'], 
    'm'    :  ['m', u'\u092E', u'\u0AAE', u'\u09AE', u'\u0A2E', u'\u0B2E'],
    
    # y r l v sh
    'y'    :  ['y', u'\u092F', u'\u0AAF', u'\u09AF', u'\u0A2F', u'\u0B2F'], 
    'r'    :  ['r', u'\u0930', u'\u0AB0', u'\u09B0', u'\u0A30', u'\u0B30'],
    'l'    :  ['l', u'\u0932', u'\u0AB2', u'\u09B2', u'\u0A32', u'\u0B32'], 
    'v'    :  ['v', u'\u0935', u'\u0AB5', u'\u09AC', u'\u0A35', u'\u0B35'],
    'w'    :  ['w', u'\u0935', u'\u0AB5', u'\u09AC', u'\u0A35', u'\u0B71'], 
    'sh'   :  ['sh', u'\u0936', u'\u0AB6', u'\u09B6', u'\u0A36', u'\u0B36'],
    
    # Sh s h L 
    'Sh'   :  ['Sh', u'\u0937', u'\u0AB7', u'\u09B7', u'\u0A36', u'\u0B37'], 
    's'    :  ['s', u'\u0938', u'\u0AB8', u'\u09B8', u'\u0A38', u'\u0B38'],
    'h'    :  ['h', u'\u0939', u'\u0AB9', u'\u09B9', u'\u0A39', u'\u0B39'], 
    'L'    :  ['L', u'\u0933', u'\u0AB3', u'\u09B2', u'\u0A33', u'\u0B33'],

    # rushi cha ru
    'RU'   :  ['RU', u'\u0960', u'\u0AE0', u'\u09E0', u'\u0A5C\u0A41', u'\u0B60'], 
    'Rlu'  :  ['Rlu', u'\u0961', u'\u0AE1', u'\u09E1', u'\u200D', u'\u0B61'],
    # handle rlu of krlupti
    
    # Om
    'OM'   :  ['OM', u'\u0950', u'\u0AD0', u'\u004F\u004D', u'\u0A74', u'\u004F\u004D'],

    
    # Half r has different unicode. If we use 
    # normal r + halant, it becomes rafar
    'R'    :  ['R', u'\u0931', u'\u0AB0,' u'\u09B0\u200D', u'\u0A5C', u'\u0B30'], 
    
    'F'    : ['F', u'\u095E', u'\u0AAB', u'\u09AB', u'\u0A5E', u'\u0B2B'], 
    'K'    : ['K', u'\u0958', u'\u0A95', u'\u0995', u'\u0A15', u'\u0B15'],
    'Kh'   : ['Kh', u'\u0959', u'\u0A96', u'\u0996', u'\u0A59', u'\u0B16'], 
    'G'    : ['G', u'\u095A', u'\u0A97', u'\u0997', u'\u0A5A', u'\u0B17'],
    'Z'    : ['Dd', u'\u095B', u'\u0A9C', u'\u099C', u'\u0A5B', u'\u0B1C'], 
    'Dd'   : ['Dd', u'\u095C', u'\u0AA1', u'\u09DC', u'\u0A21', u'\u0B5C'],
    'DH'   : ['DH', u'\u095D', u'\u0AA2', u'\u09DD', u'\u0A22', u'\u0B5D'], 
    'Y'    : ['Y', u'\u095F', u'\u0AAF', u'\u09DF', u'\u0A2F', u'\u0B5F'],
    # Numbers
    '0'    :  ['0', u'\u0966', u'\u0AE6', u'\u09E6', u'\u0A66', u'\u0B66'], 
    '1'    :  ['1', u'\u0967', u'\u0AE7', u'\u09E7', u'\u0A67', u'\u0B67'],
    '2'    :  ['2', u'\u0968', u'\u0AE8', u'\u09E8', u'\u0A68', u'\u0B68'], 
    '3'    :  ['3', u'\u0969', u'\u0AE9', u'\u09E9', u'\u0A69', u'\u0B69'],
    '4'    :  ['4', u'\u096A', u'\u0AEA', u'\u09EA', u'\u0A6A', u'\u0B6A'], 
    '5'    :  ['5', u'\u096B', u'\u0AEB', u'\u09EB', u'\u0A6B', u'\u0B6B'],
    '6'    :  ['6', u'\u096C', u'\u0AEC', u'\u09EC', u'\u0A6C', u'\u0B6C'], 
    '7'    :  ['7', u'\u096D', u'\u0AED', u'\u09ED', u'\u0A6D', u'\u0B6D'],
    '8'    :  ['8', u'\u096E', u'\u0AEE', u'\u09EE', u'\u0A6E', u'\u0B6E'], 
    '9'    :  ['9', u'\u096F', u'\u0AEF', u'\u09EF', u'\u0A6F', u'\u0B6F'] }

sym_tbl_d = {
    # Wovels
    'a'    :  ['a', u'\u0C85', u'\u0C05', u'\u0D05', u'\u0B85'],
    'aa'   :  ['aa',u'\u0C86', u'\u0C06', u'\u0D06', u'\u0B86'],
    'ee'   :  ['ee',u'\u0C8F', u'\u0C0F', u'\u0D0F', u'\u0B8F'],
    'E'   :  ['E',u'\u0C8F', u'\u0C0F', u'\u0D0F', u'\u0B8F'],
    'e'    :  ['e',u'\u0C8E', u'\u0C0E', u'\u0D0E', u'\u0B8E'],
    'ii'   :  ['ii',u'\u0C88', u'\u0C08', u'\u0D08', u'\u0B8D'],
    'I'   :  ['I',u'\u0C88', u'\u0C08', u'\u0D08', u'\u0B8D'],
    'i'    :  ['i',u'\u0C87', u'\u0C07', u'\u0D07', u'\u0B87'],
    'oo'   :  ['oo',u'\u0C93', u'\u0C13', u'\u0D13', u'\u0B93'],
    'O'   :  ['O',u'\u0C93', u'\u0C13', u'\u0D13', u'\u0B93'],
    'o'    :  ['o',u'\u0C92', u'\u0C12', u'\u0D12', u'\u0B92'],
    'uu'    :  ['uu',u'\u0C8A', u'\u0C0A', u'\u0D0A', u'\u0B8A'],
    'u'    :  ['u',u'\u0C89', u'\u0C09', u'\u0D09', u'\u0B89'],
    'U'    :  ['U',u'\u0C8A', u'\u0C0A', u'\u0D0A', u'\u0B8A'],
    'ai'   :  ['ai',u'\u0C90', u'\u0C10', u'\u0D10', u'\u0B90'],
    'au'   :  ['au',u'\u0C94', u'\u0C14', u'\u0D14', u'\u0B94'],

    # Anuswaar will be handled in a different way
    'M'    :  ['M',u'\u0C82', u'\u0C02', u'\u0D02', u'\u0B82'],
    'AN'   :  ['AN',u'\u0C82', u'\u0C01', u'\u0D02', u'\u0B82'],
    'AM'   :  ['AM',u'\u0C82', u'\u0C01', u'\u0D02', u'\u0B82'],
    'A'   :  ['A',u'\u0C86', u'\u0C06', u'\u0D06', u'\u0B86'],
    'Ha'   :  ['Ha',u'\u0C83', u'\u0C03', u'\u0D03', u'\u0B83'],

    # Kanaa/Matra/Velantee etc.
    'complete'  :  [ 'a', '', '', '', ''],
    'kanaa'  :  ['aa',u'\u0CBE', u'\u0C3E', u'\u0D3E', u'\u0BBE'],
    'vel1'   :  ['i', u'\u0CBF', u'\u0C3F', u'\u0D3F', u'\u0BBF'],
    'vel2'   :  ['ii',u'\u0CC0', u'\u0C40', u'\u0D40', u'\u0BC0'],
    'ukar1'  :  ['u',u'\u0CC1', u'\u0C41', u'\u0D41', u'\u0BC1'],
    'ukar2'  :  ['uu',u'\u0CC2', u'\u0C42', u'\u0D42', u'\u0BC2'],
    'rukar'  :  ['ru', u'\u0CC3', u'\u0C43', u'\u0D43', u'\u0BB0\u0BC1'],
    'chandra3' :  ['AM',u'\u0C82', u'\u0C01', u'\u0D02', u'\u0B82'],
    'matra1' :  ['e', u'\u0CC6', u'\u0C46', u'\u0D46', u'\u0BC6'],
    'matra11':  ['ee', u'\u0CC7', u'\u0C47', u'\u0D47', u'\u0BC7'],
    'matra2' :  ['ai', u'\u0CC8', u'\u0C48', u'\u0D48', u'\u0BC8'],
    'matra3' :  ['o', u'\u0CCA', u'\u0C4A', u'\u0D4A', u'\u0BCA'],
    'matra33' :  ['oo', u'\u0CCB', u'\u0C4B', u'\u0D4B', u'\u0BCB'],
    'matra4' :  ['au',u'\u0CCC', u'\u0C4C', u'\u0D4C', u'\u0BCC'],
    'anuswar' : ['M', u'\u0C82', u'\u0C02', u'\u0D02', u'\u0B82'],
    'halant' :  ['Ha',u'\u0CCD', u'\u0C4D', u'\u0D4D', u'\u0BCD'],

    # k kh g gh Ng
    'c'    :  ['c', u'\u0C95', u'\u0C15', u'\u0D15', u'\u0B95'],
    'k'    :  ['k', u'\u0C95', u'\u0C15', u'\u0D15', u'\u0B95'],
    'kh'   :  ['kh', u'\u0C96', u'\u0C16', u'\u0D16', u'\u0B95'],
    'g'    :  ['g', u'\u0C97', u'\u0C17', u'\u0D17', u'\u0B95'],
    'gh'   :  ['gh', u'\u0C98', u'\u0C18', u'\u0D18', u'\u0B95'],
    'Ng'   :  ['Ng', u'\u0C99', u'\u0C19', u'\u0D19', u'\u0B99'],

    # ch chh j jh nY
    'ch'   :  ['ch', u'\u0C9A', u'\u0C1A', u'\u0D1A', u'\u0B9A'],
    'chh'  :  ['chh', u'\u0C9B', u'\u0C1B', u'\u0D1B', u'\u0B9A'],
    'j'    :  ['j', u'\u0C9C', u'\u0C1C', u'\u0D1C', u'\u0B9C'],
    'jh'   :  ['jh', u'\u0C9D', u'\u0C1D', u'\u0D1D', u'\u0B9C'],
    'z'    :  ['z', u'\u0C9D', u'\u0C1D', u'\u0D1D', u'\u0BB4'],
    'nY'   :  ['nY', u'\u0C9E', u'\u0C1E', u'\u0D1E', u'\u0B9E'],
    
    # T Th D Dh N
    'T'    :  ['T', u'\u0C9F', u'\u0C1F', u'\u0D1F', u'\u0B9F'],
    'Th'   :  ['Th', u'\u0CA0', u'\u0C20', u'\u0D20', u'\u0B9F'],
    'D'    :  ['D', u'\u0CA1', u'\u0C21', u'\u0D21', u'\u0B9F'],
    'Dh'   :  ['Dh', u'\u0CA2', u'\u0C22', u'\u0D22', u'\u0B9F'],
    'N'    :  ['N', u'\u0CA3', u'\u0C23', u'\u0D23', u'\u0BA8'],
    
    # t th d dh n
    't'    :  ['t', u'\u0CA4', u'\u0C24', u'\u0D24', u'\u0BA4'],
    'th'   :  ['th', u'\u0CA5', u'\u0C25', u'\u0D25', u'\u0BA4'],
    'd'    :  ['d', u'\u0CA6', u'\u0C26', u'\u0D26', u'\u0BA4'],
    'dh'   :  ['dh', u'\u0CA7', u'\u0C27', u'\u0D27', u'\u0BA4'],
    'n'    :  ['n', u'\u0CA8', u'\u0C28', u'\u0D28', u'\u0BA9'],
    
    # p ph b bh m
    'p'    :  ['p', u'\u0CAA', u'\u0C2A', u'\u0D2A', u'\u0BAA'],
    'ph'   :  ['ph', u'\u0CAB', u'\u0C2B', u'\u0D2B', u'\u0BAA'],
    'f'    :  ['f', u'\u0CAB', u'\u0C2B', u'\u0D2B', u'\u0BAA'],
    'b'    :  ['b', u'\u0CAC', u'\u0C2C', u'\u0D2C', u'\u0BAA'],
    'bh'   :  ['bh', u'\u0CAD', u'\u0C2D', u'\u0D2D', u'\u0BAA'],
    'm'    :  ['m', u'\u0CAE', u'\u0C2E', u'\u0D2E', u'\u0BAE'],
    
    # y r l v sh
    'y'    :  ['y', u'\u0CAF', u'\u0C2F', u'\u0D2F', u'\u0BAF'],
    'r'    :  ['r',u'\u0CB0', u'\u0C30', u'\u0D30', u'\u0BB0'],
    'l'    :  ['l',u'\u0CB2', u'\u0C32', u'\u0D32', u'\u0BB2'],
    'v'    :  ['v',u'\u0CB5', u'\u0C35', u'\u0D35', u'\u0BB5'],
    'w'    :  ['w',u'\u0CB5', u'\u0C35', u'\u0D35', u'\u0BB5'],
    'sh'   :  ['sh',u'\u0CB6', u'\u0C36', u'\u0D36', u'\u0BB7'],
    
    # Sh s h L 
    'Sh'   :  ['Sh',u'\u0CB7', u'\u0C37', u'\u0D37', u'\u0BB7'],
    's'    :  ['s',u'\u0CB8', u'\u0C38', u'\u0D38', u'\u0BB8'],
    'h'    :  ['h',u'\u0CB9', u'\u0C39', u'\u0D39', u'\u0BB9'],
    'L'    :  ['L',u'\u0CB3', u'\u0C33', u'\u0D33', u'\u0BB3'],
    'Z'    :  ['Z',u'\u0C9D', u'\u0C1D', u'\u0D34', u'\u0BB4'],

    # rushi cha ru
    'RU'   :  ['RU',u'\u0CE0', u'\u0C60', u'\u0D60', u'\u0BB1\u0BC1'],
    # handle rlu of krlupti
    
    # Half r has different unicode. If we use 
    # normal r + halant, it becomes rafar
    'R'    :  ['R',u'\u0CB1', u'\u0C31', u'\u0D31', u'\u0BB1'],

    ## Tamil loong Nn
    'Nn'    :  ['Nn',u'\u0CA3', u'\u0C23', u'\u0D23', u'\u0BA3'],
    
    # Numbers
    '0'    :  ['0',u'\u0CE6', u'\u0C66', u'\u0D66', u'\u0030'],
    '1'    :  ['1',u'\u0CE7', u'\u0C67', u'\u0D67', u'\u0031'],
    '2'    :  ['2',u'\u0CE8', u'\u0C68', u'\u0D68', u'\u0032'],
    '3'    :  ['3',u'\u0CE9', u'\u0C69', u'\u0D69', u'\u0033'],
    '4'    :  ['4',u'\u0CEA', u'\u0C6A', u'\u0D6A', u'\u0034'],
    '5'    :  ['5',u'\u0CEB', u'\u0C6B', u'\u0D6B', u'\u0035'],
    '6'    :  ['6',u'\u0CEC', u'\u0C6C', u'\u0D6C', u'\u0036'],
    '7'    :  ['7',u'\u0CED', u'\u0C6D', u'\u0D6D', u'\u0037'],
    '8'    :  ['8',u'\u0CEE', u'\u0C6E', u'\u0D6E', u'\u0038'],
    '9'    :  ['9',u'\u0CEF', u'\u0C6F', u'\u0D6F', u'\u0039'] }
	

def init_state():
    global last_st
    last_st = BEGIN_ST


def init_all():

    global sym_tbl, sym_list, out_buff_arr

    init_state()

    out_buff_arr = []
    if CURR_TBL == 0:
        sym_tbl = sym_tbl_a
        sym_list = sym_list_a
    else:  
        sym_tbl = sym_tbl_d
        sym_list = sym_list_d

def process_wovel(w, sign):

    global last_st, out_buff_arr
    if last_st == BEGIN_ST or last_st == WOVEL_ST:
        out_buff_arr.append(sym_tbl[w][CURR_LIPI])
    elif ( last_st == CONSO_ST or last_st == MN_ST ) and sign is not None:
        out_buff_arr.append(sym_tbl[sign][CURR_LIPI])
    last_st = WOVEL_ST

def process_conso(w):
    global last_st, out_buff_arr
    if last_st == CONSO_ST:
        if not (CURR_TBL == 0 and CURR_LIPI == 4):
            out_buff_arr.append(sym_tbl['halant'][CURR_LIPI])
    out_buff_arr.append(sym_tbl[w][CURR_LIPI])
    last_st = CONSO_ST

def process_ru(w, ukar):
    global last_st, out_buff_arr
    if last_st == CONSO_ST:
        if CURR_LIPI == 4 and CURR_TBL == 1: # tamil
            out_buff_arr.append(u'\u0BCD')
            out_buff_arr.append(sym_tbl['r'][CURR_LIPI])
            out_buff_arr.append(sym_tbl[ukar][CURR_LIPI])
        elif CURR_LIPI == 4 and CURR_TBL == 0: # punjabi
            out_buff_arr.append(u'\u0A4D')
            out_buff_arr.append(sym_tbl['r'][CURR_LIPI])
            out_buff_arr.append(sym_tbl[ukar][CURR_LIPI])
        else: 
			  out_buff_arr.append(sym_tbl['rukar'][CURR_LIPI])
    else:
        out_buff_arr.append(sym_tbl['r'][CURR_LIPI])
        out_buff_arr.append(sym_tbl[ukar][CURR_LIPI])
        
    last_st = MN_ST

def process_number(w):
    global last_st, out_buff_arr
    last_st = NUMBER_ST
    out_buff_arr.append(sym_tbl[w][CURR_LIPI])

def process_halant(w): 
    global last_st, out_buff_arr
    out_buff_arr.append(sym_tbl['halant'][CURR_LIPI])
    out_buff_arr.append(u'\u200C')
    last_st = BEGIN_ST

def process_ws(w):
    ### Handle Tamile speciality ... 
    global last_st, out_buff_arr
    if CURR_LIPI == 4 and CURR_TBL == 1 and last_st == CONSO_ST:
        out_buff_arr.append(u'\u0BCD')

    ##a = ord(w)
    out_buff_arr.append(w)
    init_state()

def process_mysym(msym): 
    global last_st, out_buff_arr
    if msym[0] == '{' and len(msym) > 1: ## handle { }
        process_ws(msym[1:-1])
        return

    if sym_list.has_key(msym):
        eval(sym_list[msym])
        return

    process_ws(msym) 

def parse_text(text, utf16):
    import re

    if CURR_TBL == 0:
        r = re.compile(reg_table_a, (re.S|re.U)) 
    else: 
        r = re.compile(reg_table_d, (re.S|re.U)) 

    input = [a.group(0) for a in re.finditer(r,text)]

    init_all()

    if not input:
        return ''

    for a in input:
        process_mysym(a) 

    ### following is incomplete
    arr = flatten(out_buff_arr)

    #arr = map(tounicode,arr)
    
    result = u''.join(arr) 

    result = result.encode('utf-8')
    return result
    """
    if not utf16:
        arr = [("%04x" % y) for y in arr]
    else  
        out_buff_arr.pack("U*")"""
 

### utility functions 


def flatten(a):
    a_ = [] 
    if not isinstance(a,list):
        return a
    for x in a:
        if isinstance(x,list):
            x = flatten(x)
            for y in x:
                a_.append(y)
        else:
            a_.append(x)    
        
    return a_

def tounicode(x):
    if type(x) == int:
        x = unichr(x)
    else: 
        x = str(x)

    return x
    
# AMG : 02232008 Added a parameter, utf16, default is set to 0, so the API is
# not affected otherwise, SMS app, will set this value and call get_result
#
def get_result(text, lang, utf16 = 0):
     
    global CURR_LIPI, CURR_TBL
    l_ = llt[lang]
    CURR_LIPI =  l_[1]
    if not CURR_LIPI:
        return 'Language unknown!'

    CURR_TBL =  l_[0]
    if CURR_TBL is None :
        return 'Language unknown!'


    result = parse_text(text,utf16)
    return result


print get_result("{{<br/>}}K Kh G Y F abhijeet gaaDageeL kShatreeya paDHaaee {cathedral and} baaZaar haZaaroM khwaaishe aisee plAn bANk", 1)
print get_result("{<br/>} aaMdhrajyotii swaatii raMgasaaee saaee suman telugu vikipidiiyaa eenaaDu", 5)
print get_result("{<br/>} aaMdhrajyotii swaatii raMgasaaee saaee suman telugu vikipidiiyaa eenaaDu", 1, 1)
print get_result("{Abhijit} maraaThee bolato.", 1, 1)
#  p result
#end
#print flatten([1,2,3]) 
#print flatten([1,2,[3,[4,[5,6]]],5])
#print eval("flatten([[[1]]])")
