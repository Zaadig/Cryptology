import random
import sys
from math import sqrt

from common import *
from rsa import *
from elgamal import *
from attacks import *
from rsaTest import *

def main():    
    # consider changing it to test stability
    random.seed(1)
    
    #########################################################################################################################
    # RSA                                                                                                             #
    #########################################################################################################################
    print("test RSA")
    print()

    ####################
    # Q12
    ####################
    test_gen_rsa()
    test_enc_rsa()
    test_dec_rsa()
    test_RSAcipher()
    test_RSAdecipher()



    
    ####################
    # Q13
    ####################
    
    # signez et verifiez le message m
    # utilisez la meme signature sur un autre message et montrez que la signature est invalide

    #########################################################################################################################
    # ELGAMAL                                                                                                             #
    #########################################################################################################################
    print("test elgamal")
    print()
    
    ####################
    # Q18
    ####################
    
    m1 = "test1"
    m2 = "test2"
    
    #########################################################################################################################
    # Attacks                                                                                                             #
    #########################################################################################################################
    print("test attacks")
    print()

    ####################
    # Q19
    ####################
    
    c = 398723314681284 
    e = 117180248165219 
    n = 430540814772407  
    
    ####################
    # Q20
    ####################
    
    e1 = 12314003193011162113536159235283755243151610011888992283738731576726467407404999105615587391468857109847472523566826261828936711606118675045749751883975613970391088132400898832287168303353277765962059043060910231865339818814918966076743207747495586565293509515628246776362598116138951211448901151416948465617
    N1 = 86511960632558160032498009393431656383977260101233731109164947213629281844246780991976031693841856361185188781456487133525225294650519099398172362014558481492658198608932657967543869247706944199969935947646396998232005604377481903119395982120554280799653244204766810784117010682507772032840164138335758884419
    c = 5916457946589733624948860147434462339248019646224958719331143483715854530559109812229574779736823235000024530402888943789196938927157015568640675578730352657516898943152697438038017843629406779332408062642497952749289810378717203273275486650519227929027102293022292297104903561478957430406493752322856394238
    e2 = 131092117760054235922794981094423493739010822596484024829395284834242993659248301268157084602277908778355356260880209096935769664245650409197887766438460540827098183882296587174092697140404949218720632073751412585397840921553424369294971985800144479187978442094968875655423498868349579366428675134565203050475
    N2 = 152550851702642655960312091082169895236219108131780080055609726817253655750925849797703236086458826797808689336026279823934002929592826629890373068055618252764389516922965865448185211488698969546738827100020385518550258565137571681815155926167486082400436059833484496738329848604422190617285574633095747587519
         

    ####################
    # Q21
    ####################
    
    e = 3
    N1 = 11251801425414225104110625102691121852788334176880197666543376107659809892179100498201755964603481035892887501127372056474334718347881299258181802642164119
    c1 = 833563997841090231197903454163239412599612560621
    N2 = 10417214967844826388588056677654192660859762829613547308015053260129157068943923286591537675798485616825967635964559269642421553329296560166659868708557517
    c2 = 833563997841090231197903454163239412599612560621    
    N3 = 8914498449316444061177636337699544875488879613765320756791345578761962950876726672392315003384900100591266625407915960033626485455438323026203229084548179
    c3 = 833563997841090231197903454163239412599612560621    

    ####################
    # Q22 - bons
    ####################
    
    e1 = 335005463960816278593867316896417983166152916344794573850343153194217911312049872711136325234993418003668720236803986830311580268508550980361654685346311
    N1 = 5091051477963388231001637916796944302688369871753703137277176206069939465618876740391747924500711710028638413264341759139522270049313860235633263862054043
    c1 = 4145467078845472644712994806773571070731259201297400785818159271701026566350697311159454042538512643215451570946380981445723923315865474776196912541298967

    e2 = 3880522386929786816439757650057726253188135798562155960090443809425982789187841739707198985802185440418350010118211685642720469665257056875247463135661403
    d2 = 2270270259341137360152942794271619370360758459724185928285877626378514257525937090103380531321958458730253721937068263828249543225253424826884975859409347 
    N2 = 5091051477963388231001637916796944302688369871753703137277176206069939465618876740391747924500711710028638413264341759139522270049313860235633263862054043
    
main()





