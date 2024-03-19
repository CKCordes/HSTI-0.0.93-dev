from matplotlib.colors import ListedColormap

def import_cm():
    cm_data = [[0.1607822 ,0.02174219,0.36553504],
               [0.16179567,0.03348725,0.36219837],
               [0.16299883,0.04464816,0.35933774],
               [0.16432363,0.05438842,0.35670512],
               [0.16575288,0.06300251,0.35425233],
               [0.16728259,0.07077683,0.35198694],
               [0.16890031,0.07791927,0.3498749 ],
               [0.17059903,0.08456004,0.3479046 ],
               [0.17237412,0.09078775,0.34607474],
               [0.17421827,0.09667636,0.34436822],
               [0.17612488,0.10228251,0.34276877],
               [0.17809211,0.10764021,0.34128517],
               [0.18011358,0.11278808,0.339899  ],
               [0.18218559,0.1177525 ,0.33860518],
               [0.1843062 ,0.12255162,0.33740899],
               [0.18647146,0.12720567,0.33630185],
               [0.18867526,0.13173791,0.33525748],
               [0.19091826,0.13615319,0.33429537],
               [0.19319699,0.14046517,0.33340548],
               [0.19550938,0.14468307,0.33258651],
               [0.19785267,0.14881698,0.3318305 ],
               [0.20022543,0.15287298,0.33113935],
               [0.20262535,0.15685883,0.33050643],
               [0.20505077,0.16078033,0.32992937],
               [0.20750009,0.16464272,0.32940569],
               [0.20997203,0.16845023,0.32893474],
               [0.21246514,0.17220723,0.32851376],
               [0.21497836,0.17591701,0.3281428 ],
               [0.21751031,0.17958347,0.32781814],
               [0.22006004,0.18320934,0.32753951],
               [0.22262641,0.18679776,0.32730397],
               [0.22520792,0.19035286,0.32710274],
               [0.22780448,0.19387481,0.32694411],
               [0.23041519,0.19736599,0.32682576],
               [0.23303932,0.20082824,0.32674719],
               [0.23567621,0.20426325,0.32670797],
               [0.23832461,0.20767442,0.32669822],
               [0.24098431,0.21106216,0.32672256],
               [0.24365491,0.21442727,0.32678327],
               [0.24633592,0.21777097,0.32688023],
               [0.24902654,0.22109542,0.32700756],
               [0.25172611,0.22440243,0.32716067],
               [0.25443475,0.22769121,0.32734915],
               [0.2571521 ,0.23096252,0.32757407],
               [0.2598769 ,0.23422044,0.32781619],
               [0.26260963,0.23746284,0.32809257],
               [0.26534986,0.24069083,0.3284012 ],
               [0.26809694,0.24390647,0.32873345],
               [0.27087092,0.24709842,0.32911162],
               [0.27366526,0.25027346,0.32951186],
               [0.27648434,0.25342964,0.32993808],
               [0.27933136,0.25656569,0.33039317],
               [0.28219872,0.25968634,0.33087002],
               [0.28508663,0.26279166,0.33137039],
               [0.28800604,0.26587638,0.33190168],
               [0.29094591,0.26894656,0.33245695],
               [0.29390647,0.27200261,0.33303514],
               [0.29689256,0.27504214,0.33364123],
               [0.29990509,0.27806493,0.33427678],
               [0.30293888,0.28107425,0.33493588],
               [0.30599416,0.28407001,0.33562095],
               [0.30907755,0.28704898,0.33633733],
               [0.31218649,0.29001301,0.33708143],
               [0.31531827,0.29296352,0.33785309],
               [0.3184737 ,0.29590039,0.33865258],
               [0.32165889,0.2988208 ,0.33948359],
               [0.32487342,0.30172515,0.34034619],
               [0.3281152 ,0.30461483,0.34123802],
               [0.33138611,0.30748919,0.34215949],
               [0.33468981,0.31034681,0.3431109 ],
               [0.33803481,0.3131837 ,0.34409667],
               [0.34141782,0.31600207,0.34511113],
               [0.3448433 ,0.31880032,0.34615271],
               [0.34831683,0.32157651,0.34721839],
               [0.35184657,0.32432736,0.34830639],
               [0.35544332,0.32704864,0.34941318],
               [0.35910952,0.32974051,0.35052765],
               [0.36285352,0.33240033,0.35164006],
               [0.36668365,0.3350257 ,0.35273777],
               [0.37060669,0.33761495,0.35380702],
               [0.37463416,0.34016398,0.35483582],
               [0.37876197,0.3426762 ,0.35580544],
               [0.38298799,0.34515357,0.356702  ],
               [0.38730757,0.34759877,0.35751482],
               [0.3917134 ,0.35001521,0.35823745],
               [0.39619729,0.35240618,0.35886824],
               [0.40075552,0.35477231,0.35941231],
               [0.4053735 ,0.35711948,0.35987184],
               [0.41004421,0.35944975,0.36025411],
               [0.4147621 ,0.36176444,0.36056739],
               [0.41952317,0.3640642 ,0.36082015],
               [0.42432472,0.36634921,0.36102042],
               [0.42917161,0.36861574,0.36117973],
               [0.43405656,0.3708667 ,0.36130082],
               [0.43897897,0.37310158,0.36138931],
               [0.44393873,0.37531976,0.36145009],
               [0.44893577,0.37752064,0.36148754],
               [0.4539702 ,0.37970362,0.36150527],
               [0.45904876,0.38186447,0.36151087],
               [0.4641654 ,0.38400599,0.36150361],
               [0.46931946,0.38612814,0.36148547],
               [0.47451078,0.3882306 ,0.36145864],
               [0.47973918,0.39031309,0.361425  ],
               [0.485006  ,0.3923745 ,0.36138726],
               [0.49031581,0.39441178,0.36135065],
               [0.49566167,0.39642854,0.36131231],
               [0.5010428 ,0.39842485,0.36127386],
               [0.50645887,0.40040063,0.36123621],
               [0.51190949,0.40235583,0.36120015],
               [0.51740277,0.40428533,0.36117286],
               [0.52292941,0.4061942 ,0.36115011],
               [0.52848843,0.40808278,0.36113234],
               [0.53407927,0.40995117,0.36112016],
               [0.53970363,0.41179813,0.3611152 ],
               [0.5453666 ,0.41362019,0.36112289],
               [0.55105882,0.4154227 ,0.36113892],
               [0.5567807 ,0.41720537,0.36116248],
               [0.56253146,0.41896847,0.36119409],
               [0.56831859,0.42070682,0.36124249],
               [0.57413515,0.42242478,0.36130085],
               [0.57997881,0.42412362,0.36136842],
               [0.58584741,0.42580433,0.36144692],
               [0.59175229,0.42745964,0.36154233],
               [0.59768454,0.4290951 ,0.36164884],
               [0.60363969,0.43071314,0.36176729],
               [0.60962097,0.43231187,0.36189662],
               [0.61563736,0.43388508,0.36204459],
               [0.62167548,0.43544123,0.36220447],
               [0.62773717,0.43697937,0.36237385],
               [0.63383159,0.43849329,0.36255812],
               [0.63992335,0.44000716,0.36273014],
               [0.64603898,0.44150679,0.36286643],
               [0.652179  ,0.44299191,0.36296484],
               [0.65832085,0.44447537,0.3630406 ],
               [0.66448624,0.4459449 ,0.36307778],
               [0.67067567,0.44740023,0.3630745 ],
               [0.67688556,0.44884336,0.36303296],
               [0.68310064,0.45028341,0.36296238],
               [0.68933586,0.45171176,0.36285019],
               [0.69559154,0.45312825,0.36269528],
               [0.70186593,0.45453397,0.36249759],
               [0.70815895,0.4559291 ,0.36225511],
               [0.71446854,0.45731498,0.36196784],
               [0.72079057,0.4586944 ,0.36163601],
               [0.72712515,0.46006748,0.36125776],
               [0.73347581,0.46143225,0.36082791],
               [0.73984146,0.46278964,0.36034444],
               [0.74622115,0.46414051,0.35980487],
               [0.75261674,0.4654841 ,0.35920284],
               [0.75902286,0.46682405,0.35854032],
               [0.76544077,0.46816006,0.3578107 ],
               [0.77186711,0.4694949 ,0.35701037],
               [0.77829291,0.47083507,0.35614076],
               [0.78472416,0.47217736,0.35519013],
               [0.791163  ,0.47352131,0.35414643],
               [0.79760665,0.4748696 ,0.35300278],
               [0.8040231 ,0.47624533,0.35177118],
               [0.81043752,0.47763294,0.35041682],
               [0.81682376,0.47905254,0.34893809],
               [0.8231831 ,0.48050533,0.34731466],
               [0.82947021,0.48202638,0.34554836],
               [0.83568217,0.48362199,0.34360107],
               [0.84176963,0.48533185,0.3414663 ],
               [0.84767114,0.48720606,0.33913207],
               [0.85325165,0.48934805,0.33664597],
               [0.8583761 ,0.49185845,0.3341    ],
               [0.86283054,0.49488527,0.33176642],
               [0.86649044,0.4984969 ,0.33001719],
               [0.86942117,0.50261947,0.32910154],
               [0.87178572,0.50711909,0.32903598],
               [0.87378617,0.51184559,0.32966498],
               [0.87551084,0.51673585,0.33086554],
               [0.87706046,0.52172011,0.33249969],
               [0.87846863,0.52677652,0.33448779],
               [0.87979455,0.53186863,0.3367023 ],
               [0.88113596,0.53694322,0.33887751],
               [0.88249222,0.54200343,0.34098731],
               [0.88387158,0.54704476,0.34302272],
               [0.8852709 ,0.55207045,0.34498146],
               [0.88669394,0.55707915,0.34685654],
               [0.88814491,0.56206926,0.34864029],
               [0.88962789,0.56703941,0.35032396],
               [0.89114748,0.57198802,0.35189775],
               [0.89270894,0.57691315,0.35335074],
               [0.8943184 ,0.58181243,0.35467082],
               [0.89598626,0.586681  ,0.35584159],
               [0.89772267,0.59151434,0.35684594],
               [0.89953189,0.59631185,0.3576679 ],
               [0.90144014,0.60105942,0.35827834],
               [0.90345372,0.60575565,0.358657  ],
               [0.90559716,0.6103881 ,0.35877165],
               [0.90790045,0.61494127,0.35858708],
               [0.91039264,0.6194005 ,0.35806735],
               [0.91311464,0.6237439 ,0.35717356],
               [0.91610644,0.62794989,0.35587288],
               [0.91941614,0.63199125,0.35414079],
               [0.92309442,0.63583805,0.35196813],
               [0.92717829,0.63946675,0.34937621],
               [0.931685  ,0.64286368,0.34641858],
               [0.93646195,0.64611562,0.34323688],
               [0.94095436,0.64954896,0.34017594],
               [0.945073  ,0.65321257,0.3373582 ],
               [0.948772  ,0.65712749,0.33491177],
               [0.9520308 ,0.66129864,0.33296059],
               [0.954856  ,0.66571463,0.33160689],
               [0.95728059,0.67034966,0.33090895],
               [0.95935541,0.67516947,0.33087555],
               [0.96113792,0.68013814,0.3314737 ],
               [0.96268441,0.68522219,0.33264487],
               [0.96403382,0.69039888,0.33433502],
               [0.96523028,0.69564371,0.33647335],
               [0.96629876,0.70094314,0.33900737],
               [0.96726098,0.70628564,0.34188897],
               [0.96813469,0.71166208,0.34507465],
               [0.9689355 ,0.71706464,0.34852562],
               [0.96967571,0.72248736,0.35220834],
               [0.97035586,0.72793018,0.35610802],
               [0.97098795,0.73338769,0.36018949],
               [0.97156686,0.73886202,0.36445906],
               [0.97210147,0.74434795,0.36891513],
               [0.97259323,0.74984403,0.3735634 ],
               [0.97304413,0.75534861,0.37840918],
               [0.97345629,0.76086026,0.38345212],
               [0.97383267,0.76637681,0.38869819],
               [0.97417594,0.77189669,0.39414613],
               [0.97448981,0.77741765,0.3997974 ],
               [0.97477818,0.78293741,0.40565375],
               [0.97504498,0.78845418,0.4117082 ],
               [0.97529499,0.79396498,0.41796905],
               [0.9755327 ,0.79946828,0.42442258],
               [0.9757633 ,0.80496136,0.43107112],
               [0.97599189,0.81044208,0.43790863],
               [0.97622349,0.81590869,0.44492455],
               [0.97646379,0.82135834,0.4521233 ],
               [0.97671761,0.82678997,0.45948664],
               [0.97699021,0.83220146,0.46701268],
               [0.97728648,0.83759132,0.47469273],
               [0.97761095,0.8429585 ,0.48251492],
               [0.97796854,0.8483012 ,0.49047765],
               [0.97836275,0.85361935,0.4985629 ],
               [0.978798  ,0.85891125,0.50677333],
               [0.97927728,0.86417731,0.51508852],
               [0.97980341,0.86941655,0.52351261],
               [0.98033755,0.87464937,0.53200996],
               [0.98088057,0.8798813 ,0.54049147],
               [0.98142582,0.88511499,0.54896807],
               [0.98197663,0.89034949,0.55743666],
               [0.98253456,0.89558452,0.5658966 ],
               [0.98310003,0.90082018,0.5743488 ],
               [0.98366971,0.90605787,0.58279923],
               [0.98424909,0.91129595,0.59124179],
               [0.98483248,0.91653662,0.59968556],
               [0.98542438,0.92177856,0.60812572],
               [0.98601741,0.9270245 ,0.6165735 ],
               [0.98661219,0.93227439,0.62502922],
               [0.98713011,0.93755403,0.63359896]]
    newtec_cm = ListedColormap(cm_data, name="newtec_cm")
    return newtec_cm
