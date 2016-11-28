/* 
 * Changelog : 
    - 6th September 2010 i
      - Performed following manual renaming to reduce the code size. 
        Managed to get rid of good 2/3K. Not bad. 
/obr = out_buffer_arr
/pw = process_wovel, pc = process_conso , pn = process_number, pr = process_ru, ph = process_halant, ps = process_ws 
/BS = BEGIN_ST , CS = CONSO_ST, WS = WOVEL_ST, NS = NUMBER_ST, MS = MN_ST 
/ptw = parse_text_wrapper
/l_s = last_st, is = init_state, i_a = init_all
*/
var BS = 0;
var CS = 1;
var WS = 2;
var NS = 3;
var MS = 4;

// current lipi, index in the symbol table array. Default is devnagari
//CT = CURR_TBL, CL = CURR_LIPI
var CT = 0;
var CL = 4;

// llt - language lookup table is no longer a simple array but its an array of tuples,
// first indicates the index in the symlt and second indicates the offset of lang.
var llt = [ [0,0],   /* english */
            [0,1],   /* marathi */
            [0,1],   /* hindi   */
            [0,2],   /* gujarathi */
            [1,1],    /* kannada */
            [1,2],    /* Telugu */
            [1,3],    /* Malayalam */
            [0,3],    /* Bangla */
            [1,4],    /* Tamil */
            [0,4],    /* Punjabi */
            [0,5]     /* Oriya */
          ];

var obr = [];


var l_s = BS;


function is() {
  l_s = BS;
}
  
function i_a() {
  is();
  if(CT == 0) { 
    sym_tbl = sym_tbl_a;
    sym_list = sym_list_a;
  } else { 
    sym_tbl = sym_tbl_d;
    sym_list = sym_list_d;
  } 
}

function pw(w, sign) {

  if ((l_s == BS) || (l_s == WS)) {
    obr.push(sym_tbl[w][CL])
  } else if (((l_s == CS) || (l_s == MS )) &&  sign) {
    if (sign == 'vel1') {
      obr.push(sym_tbl[sign][CL])
    } else {
      obr.push(sym_tbl[sign][CL])
    } 
  }
  
  l_s = WS;

}

function pc(w) {
  if (l_s == CS) {
    if (CL == 4 && CT == 0) { 
    } else {
      obr.push(sym_tbl['halant'][CL]);
    }
  } 
  obr.push(sym_tbl[w][CL]);
  l_s = CS;

}

function pr(w, ukar) {
  if (l_s == CS) {
    if(CL == 4 && CT == 1 && l_s == CS) { 
      obr.push('\u0BCD');
      obr.push(sym_tbl['r'][CL]);
      obr.push(sym_tbl[ukar][CL]);
    } else if(CL == 4 && CT == 0 && l_s == CS){ 
      obr.push('\u0A4D');
      obr.push(sym_tbl['r'][CL]);
      obr.push(sym_tbl[ukar][CL]);
    } else { 
      obr.push(sym_tbl['rukar'][CL]);
    } 
  } else {
    obr.push(sym_tbl['r'][CL]);
    obr.push(sym_tbl[ukar][CL]);
    
    }
  l_s = MS; 
}

function pn(w) {
  l_s = NS;
  obr.push(sym_tbl[w][CL]);
}

function ph(w) {
  obr.push(sym_tbl['halant'][CL]);
  obr.push('\u200C');
  l_s = BS;
}

function ps(w) {
  if(CL == 4 && CT == 1 && l_s == CS) { 
    obr.push('\u0BCD')
  } 
  obr.push(w);
  l_s = BS;
}

var sym_list = sym_list_a;
// TODO : separate sym_lists 
var sym_list_d = {   
    'ai' : "pw('ai','matra2')", 
    'au' : "pw('au', 'matra4')", 
    'aa' : "pw('aa', 'kanaa')",
    'A' :  "pw('A', 'kanaa')",
    'a'  : "pw('a', null)",
    'ee' : "pw('ee', 'matra11')", 
    'E' :  "pw('E', 'matra11')", 
    'e'  : "pw('e', 'matra1')",
    'ii' : "pw('ii', 'vel2')", 
    'I' :  "pw('I', 'vel2')", 
    'i'  : "pw('i', 'vel1')", 
    'oo' : "pw('oo', 'matra33')", 
    'O'  : "pw('O', 'matra33')", 
    'o'  : "pw('o', 'matra3')",
    'uu' : "pw('uu', 'ukar2')", 
    'u'  : "pw('u', 'ukar1')", 
    'U'  : "pw('U', 'ukar2')", 
    'Ha' : "pw('Ha', 'halant')", 
    'M'  : "pw('M', 'anuswar')", 
    'AM' : "pw('AM', 'chandra3')", 
    'AN' : "pw('AN', 'chandra3')",
    'c'  : "pc('c')",
    'k'  : "pc('k')",
    'kh' : "pc('kh')",
    'g'  : "pc('g')",
    'gh' : "pc('gh')",
    'Ng' : "pc('Ng')",

    // ch chh j jh nY @@@@@@
    'ch' : "pc('ch')",
    'chh': "pc('chh')",
    'j'  : "pc('j')",
    'jh' : "pc('jh')",
    'z'  : "pc('z')",
    'nY' : "pc('nY')",
    
    // T Th D Dh N @@@@@@
    'T'  : "pc('T')",
    'Th' : "pc('Th')",
    'D'  : "pc('D')",
    'Dh' : "pc('Dh')",
    'N'  : "pc('N')",
    
    // t th d dh n @@@@@@
    't'  : "pc('t')",
    'th' : "pc('th')",
    'd'  : "pc('d')",
    'dh' : "pc('dh')",
    'n'  : "pc('n')",
    
    // p ph b bh m @@@@@@
    'p'  : "pc('p')",
    'ph' : "pc('ph')",
    'f'  : "pc('f')",
    'b'  : "pc('b')",
    'bh' : "pc('bh')",
    'm'  : "pc('m')",
    
    // y r l v sh @@@@@@
    'y'  : "pc('y')",
    'r'  : "pc('r')",
    'l'  : "pc('l')",
    'v'  : "pc('v')",
    'w'  : "pc('w')",
    'sh' : "pc('sh')",
    
    // Sh s h L  @@@@@@
    'Sh' : "pc('Sh')",
    's'  : "pc('s')",
    'h'  : "pc('h')",
    'L'  : "pc('L')",
    'Z'  : "pc('Z')",


    // rushi cha ru @@@@@@
    'RU' :  "pw('RU', null)", 
    'R'  :  "pc('R')",
    'Nn' :  "pc('Nn')",
    'ruu':  "pr('ru', 'ukar2')",
    'rU':   "pr('ru', 'ukar2')",
    'ru' :  "pr('ru', 'ukar1')",
    '0'  :  "pn('0')",
    '1'  :  "pn('1')",
    '2'  :  "pn('2')",
    '3'  :  "pn('3')",
    '4'  :  "pn('4')",
    '5'  :  "pn('5')",
    '6'  :  "pn('6')",
    '7'  :  "pn('7')",
    '8'  :  "pn('8')",
    '9'  :  "pn('9')",
    '_'  :  "ph('_')"};
  
var sym_list_a = {   'aa' : "pw('aa', 'kanaa')",
    'ai' : "pw('ai','matra2')", 
    'au' : "pw('au', 'matra4')", 
    'a'  : "pw('a', null)",
    'u'  : "pw('u', 'ukar1')", 
    'U'  : "pw('U', 'ukar1')", 
    'oo' : "pw('oo', 'ukar2')", 
    'o'  : "pw('o', 'matra3')",
    'Ha' : "pw('Ha', 'halant')", 
    'M'  : "pw('M', 'anuswar')", 
    'AM' : "pw('AM', 'chandra3')", 
    'AN' : "pw('AN', 'chandra3')",
    'A'  : "pw('A', 'chandra1')",
    'O'  : "pw('O', 'chandra2')",
    'e'  : "pw('e', 'matra1')",
    'ee' : "pw('ee', 'vel2')", 
    'i'  : "pw('i', 'vel1')", 
    'c'  : "pc('c')",
    'k'  : "pc('k')",
    'kh' : "pc('kh')",
    'g'  : "pc('g')",
    'gh' : "pc('gh')",
    'Ng' : "pc('Ng')",

    // ch chh j jh nY
    'ch' : "pc('ch')",
    'chh': "pc('chh')",
    'j'  : "pc('j')",
    'jh' : "pc('jh')",
    'z'  : "pc('z')",
    'nY' : "pc('nY')",
    
    // T Th D Dh N
    'T'  : "pc('T')",
    'Th' : "pc('Th')",
    'D'  : "pc('D')",
    'Dh' : "pc('Dh')",
    'N'  : "pc('N')",
    
    // t th d dh n
    't'  : "pc('t')",
    'th' : "pc('th')",
    'd'  : "pc('d')",
    'dh' : "pc('dh')",
    'n'  : "pc('n')",
    
    // p ph b bh m
    'p'  : "pc('p')",
    'ph' : "pc('ph')",
    'f'  : "pc('f')",
    'b'  : "pc('b')",
    'bh' : "pc('bh')",
    'm'  : "pc('m')",
    
    // y r l v sh
    'y'  : "pc('y')",
    'r'  : "pc('r')",
    'l'  : "pc('l')",
    'v'  : "pc('v')",
    'w'  : "pc('w')",
    'sh' : "pc('sh')",
    
    // Sh s h L 
    'Sh' : "pc('Sh')",
    's'  : "pc('s')",
    'h'  : "pc('h')",
    'L'  : "pc('L')",

    // New letters 
    'F'  : "pc('F')", 
    'K'  : "pc('K')", 
    'Kh' : "pc('Kh')", 
    'G'  : "pc('G')", 
    'Z'  : "pc('Z')", 
    'Dd' : "pc('Dd')", 
    'DH' : "pc('DH')", 
    'Y'  : "pc('Y')", 

    // rushi cha ru
    'OM' :  "pw('OM', null)",
    'RU' :  "pw('RU', null)", 
    'R'  :  "pc('R')",
    'Rlu':  "pc('Rlu')", 
    'roo':  "pr('ru', 'ukar2')",
    'ru' :  "pr('ru', 'ukar1')",
    '0'  :  "pn('0')",
    '1'  :  "pn('1')",
    '2'  :  "pn('2')",
    '3'  :  "pn('3')",
    '4'  :  "pn('4')",
    '5'  :  "pn('5')",
    '6'  :  "pn('6')",
    '7'  :  "pn('7')",
    '8'  :  "pn('8')",
    '9'  :  "pn('9')", 
    '_'  :  "ph('_')"};

var reg_table_a ='(\{[\\w\\W]*?\})|(aa)|(ai)|(au)|(a)|(i)|(ee)|(e)|(u)|(U)|(oo)|(OM)|(o)|(Ha)|(M)|(AM)|(AN)|(A)|(O)|(kh)|(k)|(gh)|(g)|(Ng)|(chh)|(ch)|(c)|(jh)|(j)|(z)|(nY)|(Th)|(T)|(Dd)|(DH)|(Dh)|(D)|(N)|(th)|(t)|(dh)|(d)|(n)|(ph)|(p)|(f)|(bh)|(b)|(m)|(y)|(roo)|(ru)|(r)|(l)|(v)|(w)|(sh)|(Sh)|(s)|(h)|(L)|(RU)|(Rlu)|(R)|(F)|(Kh)|(K)|(G)|(Z)|(Y)|(0)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(_)|(\s+)|(\n)|(.)';

var reg_table_d ='(\{[\\w\\W]*?\})|(aa)|(ai)|(au)|(a)|(ee)|(e)|(E)|(ii)|(i)|(I)|(oo)|(o)|(O)|(uu)|(u)|(U)|(Ha)|(M)|(AM)|(AN)|(A)|(kh)|(k)|(gh)|(g)|(Ng)|(chh)|(ch)|(c)|(jh)|(j)|(z)|(nY)|(Th)|(T)|(Dh)|(D)|(Nn)|(N)|(th)|(t)|(dh)|(d)|(n)|(ph)|(p)|(f)|(bh)|(b)|(m)|(y)|(ruu)|(ru)|(r)|(l)|(v)|(w)|(sh)|(Sh)|(s)|(h)|(L)|(RU)|(R)|(Z)|(0)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(_)|(\s+)|(\n)|(.)';


var sym_tbl_a = {
        // Wovels
        'a'    :  ['a', '\u0905', '\u0A85', '\u0985', '\u0A05', '\u0B05'], 
        'aa'   :  ['aa', '\u0906', '\u0A86', '\u0986', '\u0A06', '\u0B06'],
        'i'    :  ['i', '\u0907', '\u0A87', '\u0987', '\u0A07', '\u0B07'], 
        'ee'   :  ['ee', '\u0908', '\u0A88', '\u0988', '\u0A08', '\u0B08'],
        'u'    :  ['u', '\u0909', '\u0A89', '\u0989', '\u0A09', '\u0B09'], 
        'U'    :  ['U', '\u0909', '\u0A89', '\u0989', '\u0A09', '\u0B09'],
        'oo'   :  ['oo', '\u090A', '\u0A8A', '\u098A', '\u0A0A', '\u0B0A'], 
        'e'    :  ['e', '\u090F', '\u0A8F', '\u098F', '\u0A0F', '\u0B0F'],
        'ai'   :  ['ai', '\u0910', '\u0A90', '\u0990', '\u0A10', '\u0B10'], 
        'o'    :  ['o', '\u0913', '\u0A93', '\u0993', '\u0A13', '\u0B13'],
        'au'   :  ['au', '\u0914', '\u0A94', '\u0994', '\u0A14', '\u0B14'],

        // Anuswaar will be handled in a different way
        'M'    :  ['M', '\u0902', '\u0A82', '\u0982', '\u0A70', '\u0B02'], 
        'AN'   :  ['AN', '\u0901', '\u0A81', '\u0981', '\u0A02', '\u0B01'],
        'AM'   :  ['AM', '\u0901', '\u0A81', '\u0981', '\u0A02', '\u0B01'], 
        'Ha'   :  ['Ha', '\u0903', '\u0A83', '\u0983', '\u0A03', '\u0B03'],
        'A'    :  ['A', '\u090D', '\u0A8D', '\u0986', '\u0A06', '\u0B06'], 
        'O'    :  ['O', '\u0911', '\u0A91', '\u0993', '\u0A13', '\u0B13'],

        // Kanaa/Matra/Velantee etc.
        'complete'  :  [ 'a', '', '', '', ''],
        'kanaa'  :  ['aa', '\u093E', '\u0ABE', '\u09BE', '\u0A3E', '\u0B3E'], 
        'vel1'   :  ['i', '\u093F', '\u0ABF', '\u09BF', '\u0A3F', '\u0B3F'],
        'vel2'   :  ['ee', '\u0940', '\u0AC0', '\u09C0', '\u0A40', '\u0B40'], 
        'ukar1'  :  ['u', '\u0941', '\u0AC1', '\u09C1', '\u0A41', '\u0B41'],
        'ukar2'  :  ['oo', '\u0942', '\u0AC2', '\u09C2', '\u0A42', '\u0B42'], 
        'rukar'  :  ['ru', '\u0943', '\u0AC3', '\u09C3', '\u0A30&#x0A41', '\u0B43'], //check 
        'chandra1' :  ['A', '\u0945', '\u0AC5', '\u09BE', '\u0A4B', '\u0B4B'], 
        'chandra2' :  ['O', '\u0949', '\u0AC9', '\u09CB', '\u0A3E', '\u0B3E'],
        'chandra3' :  ['AM', '\u0901', '\u0A81', '\u0981', '\u0A02', '\u0B01'], 
        'matra1' :  ['e', '\u0947', '\u0AC7', '\u09C7', '\u0A47', '\u0B47'],
        'matra2' :  ['ai', '\u0948', '\u0AC8', '\u09C8', '\u0A48', '\u0B48'], 
        'matra3' :  ['o', '\u094B', '\u0ACB', '\u09CB', '\u0A4B', '\u0B4B'],
        'matra4' :  ['au', '\u094C', '\u0ACC', '\u09CC', '\u0A4C', '\u0B4C'], 
        'anuswar' : ['M', '\u0902', '\u0A82', '\u0982', '\u0A70', '\u0B02'],
        'halant' :  ['_', '\u094D', '\u0ACD', '\u09CD', '\u0A71', '\u0B4D'],

        // k kh g gh Ng
        'c'    :  ['c', '\u0915', '\u0A95', '\u0995', '&#x0A115;', '\u0B15'], 
        'k'    :  ['k', '\u0915', '\u0A95', '\u0995', '\u0A15', '\u0B15'],
        'kh'   :  ['kh', '\u0916', '\u0A96', '\u0997', '\u0A16', '\u0B16'], 
        'g'    :  ['g', '\u0917', '\u0A97', '\u0997', '\u0A17', '\u0B17'],
        'gh'   :  ['gh', '\u0918', '\u0A98', '\u0998', '\u0A18', '\u0B18'], 
        'Ng'   :  ['Ng', '\u0919', '\u0A99', '\u0999', '\u0A19', '\u0B19'],

        // ch chh j jh nY
        'ch'   :  ['ch', '\u091A', '\u0A9A', '\u099A', '\u0A1A', '\u0B1A'], 
        'chh'  :  ['chh', '\u091B', '\u0A9B', '\u099B', '\u0A1B', '\u0B1B'],
        'j'    :  ['j', '\u091C', '\u0A9C', '\u099C', '\u0A1C', '\u0B1C'], 
        'jh'   :  ['jh', '\u091D', '\u0A9D', '\u099D', '\u0A1D', '\u0B1D'],
        'z'    :  ['z', '\u091D', '\u0A9D', '\u099D', '\u0A1D', '\u0B1D'], 
        'nY'   :  ['nY', '\u091E', '\u0A9E', '\u099E', '\u0A1E', '\u0B1E'],
        
        // T Th D Dh N
        'T'    :  ['T', '\u091F', '\u0A9F', '\u099F', '\u0A1F', '\u0B1F'], 
        'Th'   :  ['Th', '\u0920', '\u0AA0', '\u09A0', '\u0A20', '\u0B20'],
        'D'    :  ['D', '\u0921', '\u0AA1', '\u09A2', '\u0A21', '\u0B21'], 
        'Dh'   :  ['Dh', '\u0922', '\u0AA2', '\u09A2', '\u0A22', '\u0B22'],
        'N'    :  ['N', '\u0923', '\u0AA3', '\u09A3', '\u0A23', '\u0B23'],
        
        // t th d dh n
        't'    :  ['t', '\u0924', '\u0AA4', '\u09A4', '\u0A24', '\u0B24'], 
        'th'   :  ['th', '\u0925', '\u0AA5', '\u09A5', '\u0A25', '\u0B25'],
        'd'    :  ['d', '\u0926', '\u0AA6', '\u09A6', '\u0A26', '\u0B26'], 
        'dh'   :  ['dh', '\u0927', '\u0AA7', '\u09A7', '\u0A27', '\u0B27'],
        'n'    :  ['n', '\u0928', '\u0AA8', '\u09A8', '\u0A28', '\u0B28'],
        
        // p ph b bh m
        'p'    :  ['p', '\u092A', '\u0AAA', '\u09AA', '\u0A2A', '\u0B2A'], 
        'ph'   :  ['ph', '\u092B', '\u0AAB', '\u09AB', '\u0A2B', '\u0B2B'],
        'f'    :  ['f', '\u092B', '\u0AAB', '\u09AB', '\u0A2B', '\u0B2B'], 
        'b'    :  ['b', '\u092C', '\u0AAC', '\u09AC', '\u0A2C', '\u0B2C'],
        'bh'   :  ['bh', '\u092D', '\u0AAD', '\u09AD', '\u0A2D', '\u0B2D'], 
        'm'    :  ['m', '\u092E', '\u0AAE', '\u09AE', '\u0A2E', '\u0B2E'],
        
        // y r l v sh
        'y'    :  ['y', '\u092F', '\u0AAF', '\u09AF', '\u0A2F', '\u0B2F'], 
        'r'    :  ['r', '\u0930', '\u0AB0', '\u09B0', '\u0A30', '\u0B30'],
        'l'    :  ['l', '\u0932', '\u0AB2', '\u09B2', '\u0A32', '\u0B32'], 
        'v'    :  ['v', '\u0935', '\u0AB5', '\u09AC', '\u0A35', '\u0B35'],
        'w'    :  ['w', '\u0935', '\u0AB5', '\u09AC', '\u0A35', '\u0B71'], 
        'sh'   :  ['sh', '\u0936', '\u0AB6', '\u09B6', '\u0A36', '\u0B36'],
        
        // Sh s h L 
        'Sh'   :  ['Sh', '\u0937', '\u0AB7', '\u09B7', '\u0A36', '\u0B37'], 
        's'    :  ['s', '\u0938', '\u0AB8', '\u09B8', '\u0A38', '\u0B38'],
        'h'    :  ['h', '\u0939', '\u0AB9', '\u09B9', '\u0A39', '\u0B39'], 
        'L'    :  ['L', '\u0933', '\u0AB3', '\u09B2', '\u0A33', '\u0B33'],

        // rushi cha ru
        'RU'   :  ['RU', '\u0960', '\u0AE0', '\u09E0', '\u0A5C\u0A41', '\u0B60'],
        'Rlu'  :  ['Rlu', '\u0961', '\u0AE1', '\u09E1', , '\u0B61'],
        // handle rlu of krlupti
        
        // OM
        'OM'   :  ['OM', '\u0950', '\u0AD0', 'OM', '\u0A74','OM'],
        
        // Half r has different unicode. If we use 
        // normal r + halant, it becomes rafar
        'R'    :  ['R', '\u0931', '\u0AB0', '\u09B0\u200D', '\u0A5C', '\u0B30'],
        
        'F'    : ['F', '\u095E', '\u0AAB', '\u09AB', '\u0A5E', '\u0B2B'], 
        'K'    : ['K', '\u0958', '\u0A95', '\u0995', '\u0A15', '\u0B15'],
        'Kh'   : ['Kh', '\u0959', '\u0A96', '\u0996', '\u0A59', '\u0B16'], 
        'G'    : ['G', '\u095A', '\u0A97', '\u0997', '\u0A5A', '\u0B17'],
        'Z'    : ['Z', '\u095B', '\u0A9C', '\u099C', '\u0A5B', '\u0B1C'], 
        'Dd'   : ['Dd', '\u095C', '\u0AA1', '\u09DC', '\u0A21', '\u0B5C'],
        'DH'   : ['DH', '\u095D', '\u0AA2', '\u09DD', '\u0A22', '\u0B5D'], 
        'Y'    : ['Y', '\u095F', '\u0AAF', '\u09DF', '\u0A2F', '\u0B5F'],
        // Numbers
        '0'    :  ['0', '\u0966', '\u0AE6', '\u09E6', '\u0A66', '\u0B66'], 
        '1'    :  ['1', '\u0967', '\u0AE7', '\u09E7', '\u0A67', '\u0B67'],
        '2'    :  ['2', '\u0968', '\u0AE8', '\u09E8', '\u0A68', '\u0B68'], 
        '3'    :  ['3', '\u0969', '\u0AE9', '\u09E9', '\u0A69', '\u0B69'],
        '4'    :  ['4', '\u096A', '\u0AEA', '\u09EA', '\u0A6A', '\u0B6A'], 
        '5'    :  ['5', '\u096B', '\u0AEB', '\u09EB', '\u0A6B', '\u0B6B'],
        '6'    :  ['6', '\u096C', '\u0AEC', '\u09EC', '\u0A6C', '\u0B6C'], 
        '7'    :  ['7', '\u096D', '\u0AED', '\u09ED', '\u0A6D', '\u0B6D'],
        '8'    :  ['8', '\u096E', '\u0AEE', '\u09EE', '\u0A6E', '\u0B6E'], 
        '9'    :  ['9', '\u096F', '\u0AEF', '\u09EF', '\u0A6F', '\u0B6F']
      };

var sym_tbl_d = {
        // Wovels
        'a'    :  ['a', '\u0C85', '\u0C05', '\u0D05', '\u0B85'],
        'aa'   :  ['aa','\u0C86', '\u0C06', '\u0D06', '\u0B86'],
        'A'    :  ['A','\u0C86', '\u0C06', '\u0D06', '\u0B86'],
        'ee'   :  ['ee','&#xC8F;', '\u0C0F', '\u0D0F', '\u0B8F'],
        'E'    :  ['E','&#xC8F;', '\u0C0F', '\u0D0F', '\u0B8F'],
        'e'    :  ['e','&#xC8E;', '\u0C0E', '&#x0D05E;', '\u0B8E'],
        'ii'   :  ['ii','\u0C88', '\u0C08', '\u0D08', '\u0B88'],
        'I'    :  ['I','\u0C88', '\u0C08', '\u0D08', '\u0B88'],
        'i'    :  ['i','\u0C87', '\u0C07', '\u0D07', '\u0B87'],
        'oo'   :  ['oo','\u0C93', '\u0C13', '\u0D13', '\u0B93'],
        'O'    :  ['O','\u0C93', '\u0C13', '\u0D13', '\u0B93'],
        'o'    :  ['o','\u0C92', '\u0C12', '\u0D12', '\u0B92'],
        'uu'   :  ['uu','\u0C8A', '\u0C0A', '\u0D0A', '\u0B8A'],
        'U'    :  ['U','\u0C8A', '\u0C0A', '\u0D0A', '\u0B8A'],
        'u'    :  ['u','\u0C89', '\u0C09', '\u0D09', '\u0B89'],
        'ai'   :  ['ai','\u0C90', '\u0C10', '\u0D10', '\u0B90'],
        'au'   :  ['au','\u0C94', '\u0C14', '\u0D14', '\u0B94'],

        // Anuswaar will be handled in a different way
        'M'    :  ['M','\u0C82', '\u0C02', '\u0D02', '\u0B82'],
        'AN'   :  ['AN','AN', '\u0C01', '\u0D02', '\u0B82'],
        'AM'   :  ['AM','AM', '\u0C01', '\u0D02', '\u0B82'],
        'Ha'   :  ['Ha','\u0C83', '\u0C03', '\u0D03', '\u0B83'],

        // Kanaa/Matra/Velantee etc.
        'complete'  :  [ 'a', '', '', '', '', ''],
        'kanaa'  :  ['aa','\u0CBE', '\u0C3E', '\u0D3E', '\u0BBE'],
        'vel1'   :  ['i', '\u0CBF', '\u0C3F', '\u0D3F', '\u0BBF'],
        'vel2'   :  ['ii','\u0CC0', '\u0C40', '\u0D40', '\u0BC0'],
        'ukar1'  :  ['u','\u0CC1', '\u0C41', '\u0D41', '\u0BC1'],
        'ukar2'  :  ['uu','\u0CC2', '\u0C42', '\u0D42', '\u0BC2'],
        'rukar'  :  ['ru', '\u0CC3', '\u0C43', '\u0D43', '\u0BB0\u0BC1'],
        'chandra3' :  ['AM','&#x0C82', '\u0C01', '\u0D02', '\u0B82'],
        'matra1' :  ['e', '\u0CC6', '\u0C46', '\u0D46', '\u0BC6'],
        'matra11':  ['ee', '\u0CC7', '\u0C47', '\u0D47', '\u0BC7'],
        'matra2' :  ['ai', '\u0CC8', '\u0C48', '\u0D48', '\u0BC8'],
        'matra3' :  ['o', '\u0CCA', '\u0C4A', '\u0D4A', '\u0BCA'],
        'matra33' :  ['oo', '\u0CCB', '\u0C4B', '\u0D4B', '\u0BCB'],
        'matra4' :  ['au','\u0CCC', '\u0C4C', '\u0D4C', '\u0BCC'],
        'anuswar' : ['M', '&#x0C82', '\u0C02', '\u0D02', '\u0B82'],
        'halant' :  ['_','\u0CCD', '\u0C4D', '\u0D4D', '\u0BCD'],

        // k kh g gh Ng
        'c'    :  ['c', '\u0C95', '\u0C15', '\u0D15', '\u0B95'],
        'k'    :  ['k', '\u0C95', '\u0C15', '\u0D15', '\u0B95'],
        'kh'   :  ['kh', '\u0C96', '\u0C16', '\u0D16', '\u0B95'],
        'g'    :  ['g', '\u0C97', '\u0C17', '\u0D17', '\u0B95'],
        'gh'   :  ['gh', '\u0C98', '\u0C18', '\u0D18', '\u0B95'],
        'Ng'   :  ['Ng', '\u0C99', '\u0C19', '\u0D19', '\u0B99'],

        // ch chh j jh nY
        'ch'   :  ['ch', '\u0C9A', '\u0C1A', '\u0D1A', '\u0B9A'],
        'chh'  :  ['chh', '\u0C9B', '\u0C1B', '\u0D1B', '\u0B9A'],
        'j'    :  ['j', '\u0C9C', '\u0C1C', '\u0D1C', '\u0B9C'],
        'jh'   :  ['jh', '\u0C9D', '\u0C1D', '\u0D1D', '\u0B9C'],
        'z'    :  ['z', '\u0C9D', '\u0C1D', '\u0D1D', '\u0BB4'],
        'nY'   :  ['nY', '\u0C9E', '\u0C1E', '\u0D1E', '\u0B9E'],
        
        // T Th D Dh N
        'T'    :  ['T', '\u0C9F', '\u0C1F', '\u0D1F', '\u0B9F'],
        'Th'   :  ['Th', '\u0CA0', '\u0C20', '\u0D20', '\u0B9F'],
        'D'    :  ['D', '\u0CA1', '\u0C21', '\u0D21', '\u0B9F'],
        'Dh'   :  ['Dh', '\u0CA2', '\u0C22', '\u0D22', '\u0B9F'],
        'N'    :  ['N', '\u0CA3', '\u0C23', '\u0D23', '\u0BA8'],
        
        // t th d dh n
        't'    :  ['t', '\u0CA4', '\u0C24', '\u0D24', '\u0BA4'],
        'th'   :  ['th', '\u0CA5', '\u0C25', '\u0D25', '\u0BA4'],
        'd'    :  ['d', '\u0CA6', '\u0C26', '\u0D26', '\u0BA4'],
        'dh'   :  ['dh', '\u0CA7', '\u0C27', '\u0D27', '\u0BA4'],
        'n'    :  ['n', '\u0CA8', '\u0C28', '\u0D28', '\u0BA9'],
        
        // p ph b bh m
        'p'    :  ['p', '\u0CAA', '\u0C2A', '\u0D2A', '\u0BAA'],
        'ph'   :  ['ph', '\u0CAB', '\u0C2B', '\u0D2B', '\u0BAA'],
        'f'    :  ['f', '\u0CAB', '\u0C2B', '\u0D2B', '\u0BAA'],
        'b'    :  ['b', '\u0CAC', '\u0C2C', '\u0D2C', '\u0BAA'],
        'bh'   :  ['bh', '\u0CAD', '\u0C2D', '\u0D2D', '\u0BAA'],
        'm'    :  ['m', '\u0CAE', '\u0C2E', '\u0D2E', '\u0BAE'],
//---------------
        
        // y r l v sh
        'y'    :  ['y', '\u0CAF', '\u0C2F', '\u0D2F', '\u0BAF'],
        'r'    :  ['r','\u0CB0', '\u0C30', '\u0D30', '\u0BB0'],
        'l'    :  ['l','\u0CB2', '\u0C32', '\u0D32', '\u0BB2'],
        'v'    :  ['v','\u0CB5', '\u0C35', '\u0D35', '\u0BB5'],
        'w'    :  ['w','\u0CB5', '\u0C35', '\u0D35', '\u0BB5'],
        'sh'   :  ['sh','\u0CB6', '\u0C36', '\u0D36', '\u0BB7'],
        
        // Sh s h L 
        'Sh'   :  ['Sh','\u0CB7', '\u0C37', '\u0D37', '\u0BB7'],
        's'    :  ['s','\u0CB8', '\u0C38', '\u0D38', '\u0BB8'],
        'h'    :  ['h','\u0CB9', '\u0C39', '\u0D39', '\u0BB9'],
        'L'    :  ['L','\u0CB3', '\u0C33', '\u0D33', '\u0BB3'],
        'Z'    :  ['L','\u0C9D', '\u0C1D', '\u0D34', '\u0BB4'],

        // rushi cha ru
        'RU'   :  ['RU','\u0CE0', '\u0C60', '\u0D60', '\u0BB1\u0BC1'],
        // handle rlu of krlupti
        
        // Half r has different unicode. If we use 
        // normal r + halant, it becomes rafar
        'R'    :  ['R','\u0CB1', '\u0C31', '\u0D31', '\u0BB1'],
      
        // For tamil Loong N
        'Nn'    :  ['Nn','\u0CA3', '\u0C23', '\u0D23','\u0BA3'], 
        
        // Numbers
        '0'    :  ['0','\u0CE6', '\u0C66', '\u0D66', '0'],
        '1'    :  ['1','\u0CE7', '\u0C67', '\u0D67', '1'],
        '2'    :  ['2','\u0CE8', '\u0C68', '\u0D68', '2'],
        '3'    :  ['3','\u0CE9', '\u0C69', '\u0D69', '3'],
        '4'    :  ['4','\u0CEA', '\u0C6A', '\u0D6A', '4'],
        '5'    :  ['5','\u0CEB', '\u0C6B', '\u0D6B', '5'],
        '6'    :  ['6','\u0CEC', '\u0C6C', '\u0D6C', '6'],
        '7'    :  ['7','\u0CED', '\u0C6D', '\u0D6D', '7'],
        '8'    :  ['8','\u0CEE', '\u0C6E', '\u0D6E', '8'],
        '9'    :  ['9','\u0CEF', '\u0C6F', '\u0D6F', '9']
      };

var sym_tbl;
var sym_list;

function process_mysym(msym) {


  if((mysym.charAt(0) == '{') && (mysym.length > 1)) { 
    ps(mysym.substring(1,(mysym.length -1)));
    return;
  } 

  if(sym_list[msym] != undefined) { 
    eval(sym_list[msym]); 
    return;
  }  

  ps(msym); 

} 

function parse_text(text) 
{
  var re;

  if(CT == 0) {
    re = new RegExp(reg_table_a, 'g');
  } else { 
    re = new RegExp(reg_table_d, 'g');
  } 

  var input = text.match(re);
  
  var op  ;
  var opstr = '';

  i_a(); 
  //print(input);
  if(input) {
    while ((mysym = input.shift())) { 
    process_mysym(mysym);
    }
  } else {
    return '';
  }

  while((op = obr.shift()) != null) {
    opstr += op;
  }

  return opstr;
}

function convert_text_wrapper(i, o, l) 
{
  var it = document.getElementById(i).value;
  var ot;
  document.getElementById(o).innerHTML = '';
  if(l == 0) { 
    return;
  }
  CL = llt[l][1];
  if(CL == undefined) {
    return;
  }    
  CT = llt[l][0];
  if(CL == undefined) {
    return;
  }    
  ot = parse_text(it);
  document.getElementById(o).innerHTML = ot;
}

function convert_text_wrapper_txt(it, o, l) 
{
  var ot;
  document.getElementById(o).innerHTML = '';
  if(!it) {
    return;
  }
  if(l == 0) { 
    return;
  }
  CL = llt[l][1];
  if(CL == undefined) {
    return;
  }    
  CT = llt[l][0];
  if(CL == undefined) {
    return;
  }    
  ot = parse_text(it);
  document.getElementById(o).innerHTML = ot;
}

function ptw(txt, l) { 
    CL = llt[l][1];
    if(CL == undefined) {
        return;
    }    
    CT = llt[l][0];
    if(CL == undefined) {
        return;
    }     
    ot = parse_text(txt);
    return ot;
}
