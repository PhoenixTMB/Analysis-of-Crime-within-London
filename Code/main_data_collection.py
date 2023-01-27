import requests
import pandas as pd
import time
import numpy as np
import json

#these are all the links we created for all 32 boroughs
city_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.51103,-0.11272:51.50793,-0.07950:51.51023,-0.07727:51.51023,-0.07264:51.51429,-0.07427:51.51894,-0.07805:51.52161,-0.07856:51.52187,-0.08096:51.52016,-0.08534:51.51894,-0.08629:51.52000,-0.09006:51.52075,-0.08980:51.52166,-0.09410:51.52310,-0.09495:51.52348,-0.09684:51.52289,-0.09804:51.52086,-0.09787:51.51781,-0.10766:51.51824,-0.11367:51.51103,-0.11272'

ken_chel_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.52926,-0.23675:51.47754,-0.17821:51.48545,-0.14903:51.50245,-0.15812:51.49860,-0.17872:51.51003,-0.18782:51.52574,-0.20636:51.53086,-0.22954:51.52114,-0.22833:51.52926,-0.23675'

ham_ful_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.47748,-0.17704:51.53218,-0.22923:51.53261,-0.23541:51.53218,-0.24674:51.52578,-0.25292:51.50484,-0.24742:51.50484,-0.25395:51.50377,-0.25498:51.49800,-0.25120:51.49821,-0.24536:51.48902,-0.24296:51.46379,-0.19490:51.47748,-0.17704'

wandsworth_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.47267,-0.23170:51.48165,-0.17643:51.48550,-0.14587:51.48572,-0.12596:51.42132,-0.13626:51.41704,-0.14347:51.42539,-0.18329:51.43909,-0.20698:51.43309,-0.25161:51.43737,-0.25505:51.44294,-0.24269:51.45578,-0.25779:51.46583,-0.25436:51.47267,-0.23170'

lambeth_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.50842,-0.11940:51.48598,-0.12798:51.46695,-0.14927:51.45198,-0.14721:51.45026,-0.14377:51.44812,-0.14549:51.44149,-0.14309:51.44171,-0.13657:51.43700,-0.14034:51.42073,-0.13828:51.41195,-0.14892:51.41238,-0.12558:51.42266,-0.11322:51.41966,-0.07923:51.45176,-0.10052:51.46481,-0.09022:51.49282,-0.10395:51.49581,-0.11116:51.51077,-0.10910:51.50842,-0.11940'

southwark_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.50961,-0.11109:51.48076,-0.10971:51.46985,-0.09220:51.45253,-0.10216:51.42299,-0.08053:51.45488,-0.04345:51.48867,-0.05272:51.49487,-0.03144:51.50684,-0.02938:51.50940,-0.04208:51.50213,-0.05856:51.50961,-0.11109'

tow_ham_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.53098,-0.07370:51.54454,-0.03318:51.54380,-0.01705:51.51390,0.00749:51.50834,0.01006:51.50567,0.00732:51.50578,-0.00143:51.48583,0.00046:51.48786,-0.02734:51.50581,-0.03215:51.50111,-0.06082:51.50742,-0.08039:51.53098,-0.07370'

hackney_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.52044,-0.08360:51.54436,-0.01580:51.56176,-0.02884:51.56315,-0.04601:51.57723,-0.06094:51.57563,-0.08137:51.57350,-0.09751:51.57403,-0.09802:51.57062,-0.09751:51.56528,-0.10506:51.55184,-0.08721:51.54799,-0.07691:51.53390,-0.09785:51.52044,-0.08360'

islington_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.56896,-0.14352:51.53130,-0.12324:51.51884,-0.10536:51.51884,-0.08588:51.52698,-0.08428:51.53246,-0.09602:51.54723,-0.07787:51.55121,-0.07867:51.57593,-0.11977:51.56896,-0.14352'

camden_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.55533,-0.21273:51.53495,-0.18877:51.53717,-0.15461:51.51318,-0.12982:51.51935,-0.10503:51.52638,-0.11384:51.53135,-0.11660:51.53152,-0.12211:51.54780,-0.12817:51.56938,-0.14139:51.57280,-0.16949:51.56972,-0.17995:51.55533,-0.21273'

ealing_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.55895,-0.34752:51.54578,-0.30840:51.53260,-0.30601:51.53846,-0.28306:51.53426,-0.27857:51.53007,-0.28756:51.53461,-0.25496:51.53181,-0.24654:51.49579,-0.25721:51.49929,-0.40556:51.52762,-0.37634:51.53811,-0.41905:51.54545,-0.39826:51.55895,-0.34752'

hounslow_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.45591,-0.45770:51.43815,-0.45632:51.42894,-0.42989:51.43215,-0.41787:51.42231,-0.40551:51.42338,-0.39555:51.42060,-0.38525:51.42830,-0.38766:51.44200,-0.36809:51.44628,-0.38525:51.45719,-0.37358:51.45698,-0.35264:51.45912,-0.34200:51.45462,-0.33616:51.48649,-0.29290:51.47109,-0.26269:51.48799,-0.24381:51.49782,-0.24552:51.50017,-0.25308:51.50102,-0.25239:51.49525,-0.25548:51.49440,-0.25685:51.49483,-0.27127:51.50316,-0.28020:51.50209,-0.28123:51.49910,-0.35058:51.49141,-0.37152:51.49654,-0.37736:51.49996,-0.40997:51.47131,-0.41341:51.45270,-0.44602:51.45591,-0.45770'

bromley_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.29195,0.01658:51.37817,-0.02770:51.42567,-0.07435:51.41592,-0.00395:51.44437,0.03059:51.42466,0.06220:51.43177,0.07589:51.41388,0.12120:51.40799,0.14858:51.39274,0.16194:51.39213,0.14760:51.34492,0.13652:51.34431,0.11826:51.33189,0.12022:51.31519,0.08469:51.29726,0.09056:51.29277,0.04297:51.29175,0.01886:51.29195,0.01658'

croydon_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.34618,-0.11673:51.40705,-0.13252:51.42332,-0.10918:51.41978,-0.07848:51.38783,-0.03757:51.33083,0.00229:51.33902,-0.03810:51.32591,-0.04806:51.31903,-0.06957:51.31598,-0.08445:51.28778,-0.12118:51.30188,-0.15566:51.32071,-0.16083:51.32653,-0.14454:51.34361,-0.14454:51.34618,-0.11673'

lewisham_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.48895,-0.05527:51.49322,-0.03089:51.48125,-0.01579:51.47291,-0.01304:51.47355,0.01476:51.43247,0.03845:51.42819,0.02506:51.42284,0.03639:51.41363,-0.01270:51.42220,-0.05424:51.42883,-0.07553:51.45794,-0.04566:51.48895,-0.05527'

bexley_base_url ='https://data.police.uk/api/outcomes-at-location?poly=51.51343,0.11806:51.47695,0.12388:51.47885,0.11819:51.47334,0.11184:51.47538,0.09835:51.46666,0.08258:51.45994,0.08274:51.45942,0.07864:51.44563,0.08642:51.41334,0.11203:51.40910,0.15300:51.44335,0.17228:51.48208,0.22360:51.48509,0.18553:51.50819,0.16312:51.51044,0.14746:51.51568,0.12674:51.51343,0.11806'

greenwich_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.50724,0.00201:51.51301,0.12045:51.47710,0.12354:51.46833,0.08372:51.44266,0.08887:51.42511,0.06209:51.44330,0.01608:51.46534,0.00819:51.47240,0.01574:51.47069,-0.01961:51.48651,-0.02682:51.49100,-0.00039:51.50724,0.00201'

havering_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.63105,0.22425:51.62288,0.13932:51.56491,0.15248:51.56640,0.18597:51.50985,0.16085:51.48677,0.17999:51.48677,0.20990:51.51879,0.25655:51.53293,0.26971:51.54111,0.33550:51.56789,0.28765:51.60951,0.26014:51.63105,0.22425'

bark_dag_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.50850,0.15743:51.55399,0.18867:51.56573,0.18455:51.57000,0.15022:51.59922,0.14678:51.58877,0.12481:51.56722,0.12790:51.54332,0.06610:51.53072,0.07022:51.52559,0.08945:51.51138,0.09992:51.50850,0.15743'

enfield_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.60656,-0.03676:51.68016,-0.01057:51.69035,-0.11242:51.68750,-0.16408:51.66258,-0.18705:51.65475,-0.15490:51.63266,-0.13079:51.61270,-0.13997:51.60656,-0.03676'

barnet_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.63450,-0.30638:51.55575,-0.21740:51.58576,-0.15695:51.60453,-0.15653:51.59723,-0.15065:51.63268,-0.12631:51.65664,-0.15737:51.66940,-0.18297:51.66107,-0.22957:51.63450,-0.30638'

haringey_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.60576,-0.04151:51.61123,-0.13505:51.59754,-0.15170:51.60515,-0.15660:51.57254,-0.17186:51.57505,-0.12033:51.56558,-0.10510:51.57811,-0.06119:51.58797,-0.05267:51.59762,-0.04950:51.60576,-0.04151'

harrow_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.64066,-0.31255:51.61292,-0.40555:51.55343,-0.37637:51.55797,-0.33626:51.57101,-0.32440:51.57837,-0.32531:51.58630,-0.28428:51.59480,-0.28975:51.60103,-0.26787:51.64066,-0.31255'
#initailly i started my defining the response but i then just internalised this in the API loop
westminster_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.51106,-0.11169:51.51293,-0.11255:51.51373,-0.11195:51.51378,-0.11118:51.51581,-0.11203:51.51800,-0.11366:51.51827,-0.11152:51.51784,-0.10817:51.52073,-0.09779:51.52222,-0.09736:51.52286,-0.09804:51.52340,-0.09676:51.52324,-0.09684:51.52281,-0.09650:51.52313,-0.09513:51.52139,-0.09324:51.52110,-0.09226:51.52060,-0.08967:51.52003,-0.09013:51.51881,-0.08645:51.52039,-0.08518:51.51974,-0.08311:51.52192,-0.08127:51.52157,-0.07868:51.51892,-0.07949:51.51892,-0.07822:51.51663,-0.07736:51.51412,-0.07368:51.51018,-0.07264:51.50979,-0.07558:51.51036,-0.07667:51.50936,-0.07863:51.50782,-0.07949:51.51106,-0.11169'
westminster_resp = requests.get(westminster_base_url)

brent_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.51343,0.11806:51.47695,0.12388:51.47885,0.11819:51.47334,0.11184:51.47538,0.09835:51.46666,0.08258:51.45994,0.08274:51.45942,0.07864:51.44563,0.08642:51.41334,0.11203:51.40910,0.15300:51.44335,0.17228:51.48208,0.22360:51.48509,0.18553:51.50819,0.16312:51.51044,0.14746:51.51568,0.12674:51.51343,0.11806'
brent_resp = requests.get(brent_base_url)

hillingdon_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.53965,-0.41931:51.55524,-0.37849:51.61265,-0.40570:51.61932,-0.44510:51.63088,-0.49666:51.55791,-0.47733:51.53831,-0.49523:51.50667,-0.48449:51.46832,-0.50884:51.45359,-0.44510:51.47055,-0.41215:51.49999,-0.41000:51.50756,-0.39138:51.52807,-0.37777:51.53965,-0.41931'
hillingdon_resp = requests.get(hillingdon_base_url)

kingston_upon_thames_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.32637,-0.32882:51.35145,-0.29392:51.37942,-0.26017:51.38051,-0.24679:51.38704,-0.24039:51.39793,-0.24679:51.43675,-0.25668:51.42116,-0.28635:51.43349,-0.31311:51.42696,-0.31369:51.42007,-0.30730:51.37796,-0.30904:51.32819,-0.33057:51.32637,-0.32882'
kingston_upon_thames_resp = requests.get(kingston_upon_thames_base_url)

merton_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.43094,-0.25458:51.44103,-0.19104:51.42571,-0.18324:51.42010,-0.16166:51.41748,-0.14488:51.41786,-0.14428:51.41075,-0.12989:51.39692,-0.12629:51.38794,-0.21082:51.39654,-0.24739:51.41412,-0.25098:51.43094,-0.25458'
merton_resp = requests.get(merton_base_url)

newham_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.55104,0.01810:51.55525,0.04443:51.56146,0.04249:51.56427,0.04991:51.54262,0.06699:51.52959,0.07409:51.52538,0.09214:51.52578,0.09246:51.51314,0.10020:51.49709,0.06828:51.49689,0.02057:51.51414,0.00316:51.53139,-0.01649:51.53921,-0.02004:51.55104,-0.01810'
newham_resp = requests.get(newham_base_url)

redbridge_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.62889,0.02041:51.60710,0.07786:51.62361,0.13690:51.60115,0.14860:51.58826,0.12733:51.56744,0.12839:51.56644,0.12679:51.54726,0.09328:51.54395,0.06881:51.56281,0.05073:51.56049,0.04222:51.55586,0.04381:51.56281,0.01349:51.61106,0.02041:51.61866,0.00924:51.62889,0.02041'
redbridge_resp = requests.get(redbridge_base_url)

richmond_upon_thames_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.44438,-0.24093:51.42024,-0.28826:51.43187,-0.31192:51.39296,-0.32196:51.41174,-0.36068:51.40906,-0.38649:51.42963,-0.38721:51.44215,-0.36857:51.44974,-0.38649:51.45779,-0.37430:51.45600,-0.33630:51.48682,-0.29471:51.47967,-0.27535:51.47253,-0.26029:51.48593,-0.24810:51.48994,-0.23591:51.47476,-0.22372:51.46404,-0.23520:51.46538,-0.25456:51.45555,-0.25886:51.44438,-0.24093'
richmond_upon_thames_resp = requests.get(richmond_upon_thames_base_url)

sutton_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.34701,-0.11690:51.39056,-0.13319:51.38852,-0.16579:51.39300,-0.17426:51.38690,-0.21142:51.38079,-0.22119:51.39096,-0.23684:51.36737,-0.24662:51.36289,-0.22902:51.34416,-0.21794:51.33561,-0.23032:51.33154,-0.21337:51.34253,-0.19447:51.32258,-0.15470:51.34172,-0.14558:51.34701,-0.11690'
sutton_resp = requests.get(sutton_base_url)

waltham_forest_base_url = 'https://data.police.uk/api/outcomes-at-location?poly=51.64641,0.01212:51.63739,0.023983:51.61730,0.014134:51.61177,0.020231:51.59546,0.010851:51.56690,0.018824:51.55494,0.019293:51.55290,-0.01728:51.56252,-0.04777:51.58001,-0.06231:51.61090,-0.03370:51.64641,-0.01212'
waltham_forest_resp = requests.get(waltham_forest_base_url)



#-------------------------------------------------

#for the purpose of the loop i compiled all the urls into a list along with all the names in the same order
urls = [westminster_base_url, city_base_url, ken_chel_base_url, ham_ful_base_url, wandsworth_base_url, lambeth_base_url, southwark_base_url, tow_ham_base_url, hackney_base_url, islington_base_url, camden_base_url, ealing_base_url, hounslow_base_url, bromley_base_url, croydon_base_url, lewisham_base_url, bexley_base_url,  havering_base_url, bark_dag_base_url, enfield_base_url, barnet_base_url, haringey_base_url, harrow_base_url, brent_base_url, hillingdon_base_url, kingston_upon_thames_base_url, merton_base_url, newham_base_url, redbridge_base_url, richmond_upon_thames_base_url, sutton_base_url, waltham_forest_base_url]
names = ['Westminster', 'City of London', 'Kensington and Chelsea', 'Hammersmith and Fulham', 'Wandsworth', 'Lambeth', 'Southwark', 'Tower Hamlets', 'Hackney', 'Islington', 'Camden', 'Ealing', 'Hounslow', 'Bromley', 'Croydon', 'Lewisham', 'Bexley', 'Havering', 'Barking and Dagenham', 'Enfield', 'Barnet', 'Haringey', 'Harrow', 'Brent', 'Hillingdon', 'Kingston Upon Thames', 'Merton', 'Newham', 'Redbridge', 'Richmond Upon Thames', 'Sutton', 'Waltham Forest']

#this is for when i was testing iterating over the responses
responses = [westminster_resp, brent_resp, hillingdon_resp, kingston_upon_thames_resp, merton_resp, newham_resp, richmond_upon_thames_resp, sutton_resp, waltham_forest_resp] 
#i set up the main dataframe by collecting the data for Westminster 
westminster_json = westminster_resp.json()

n_westminster = len(westminster_json)

crime_westminster = []


for i in range(0,n_westminster):
  crime_name = westminster_json[i]['crime']['category']
  crime_westminster.append(crime_name)
maindf = pd.DataFrame({'Crime':crime_westminster, str(names[0]): 1})
maindf = pd.pivot_table(maindf, index=['Crime'],values=[str(names[0])],aggfunc='sum')
print(maindf)

#--------------------------------------------------

#testing for Response 200 - wesite error meant we would get random 500 responses each time which would disrupt the loop
for url in urls:
  resp_check = requests.get(url)
  print(resp_check)


  p = len(urls)
k=1
while k <= p-1:
  print(k)
  resp = requests.get(urls[k])
  fails = []
  try:
    resp_json = resp.json()
    
    crime = []

    m = len(resp_json)
    print (m)
    for g in range(0, m):
      crime_name = resp_json[g]['crime']['category']
      crime.append(crime_name)
    df = pd.DataFrame({'Crime':crime, names[k]: 1})
    df = pd.pivot_table(df, index=['Crime'],values=[names[k]],aggfunc='sum')
    print (df)
    maindf = maindf.join(df)
    
    k= k+1
  
  except:
    j=k-1
    fails.append(j)

print(maindf)
print(fails)
main_csv = maindf.to_csv('main_data.csv')

#used the try and except syntax to work around the random dataframe and joined the resulting dataframe onto the main as they had the same index