import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

def sequence_to_vector(sequence):
    char_counts = Counter(sequence)
    return np.array([char_counts.get(chr(i), 0) for i in range(65, 91)]).reshape(1, -1)

def check_sequence_similarity(seqA, seqB, threshold=0.8):
    vectorA = sequence_to_vector(seqA)
    vectorB = sequence_to_vector(seqB)

    similarity = cosine_similarity(vectorA, vectorB)
    similarity_score = similarity[0][0]
    
    print(f"The similarity score with Omicron is: {similarity_score:.2f}")
    
    if similarity_score < threshold:
        return "Warning: The sequence similarity is below 80%. Predictions might be unreliable."
    else:
        return "The sequences are similar. Predictions are more reliable."

# Example
SeqA = "MFVFLVLLPLVSSQCVNLITRTQSYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAISGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKYFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLSGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSKFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT"
SeqB = "MKAELFVLFCTFTALKADTICVGYHANNSTDTVDTILEKNVTVTHSVNLLENSHNGKLCSLNGMAPLQLGKCNVAGWILGNPECELLLTANSWSYIIETSNSENGTCYPGEFIDYEELREQLSSVSSFERFEIFPKANSWPDHETTKGVTAACSYSGTRSFYRNLLWIVKKGNSYPKLSKSYTNNKGKEVLVIWGVHHPPTTNDQQSLYQNADAYVSVGSSKYNRRFTPEIAARPKVKGQAGRMNYYWTLLDQGDTITFEATGNLIAPWYAFALDKGSGSGIIMSDAPVHNCDTKCQTPHGALNSSLPFQNVHPITIGECPKYVKSTKLRMATGLRNVPSIQSR"
SeqC = "MTDAATASSTRRNVMKPAASATPLNRTAPALPAGIHEIEEEASAHASPSHSPAQSEGALTMLSRRPSKRGKETADVTASAAQSASHLQSVELQVSQPAVSPNTGNASLVRLKEQLAADNLRPVEPELAAELINKTRPMKLADATGPQERAATHADLLGRIRETDAMAWYRAQGLSENEIANLRRSALLSGMPNPTGSFLNNAMQYIVSPWINYATHQPWAGAGFGFATAAIAAPMNAAQQSAVVSLCESIREHGGHVIVPDKKQINDKHWLPALAKALESHIAEFSGCCDRFRALKDAADQNPAAQPTADFIAAAHQVLQAETRLHQAQHDFVMTQGAHERQWMGNRWQAVPRILRSPLSGTLGLLSKTGAMRALSPTAQTVGALLMSAVQHVAAGFDEQAKQDYNNKLNLLYADVLTDTGKAKLARGEPVAAEEIDQGKLRKLIQSPTQALVKRITSGLVAMEKELKAQVAAPRSPQVTTGDDDLDLEAGHGAGPAKALKLLSQDLKALREGRLDELDPDGVAATLLLGAEKSVVSDQLIGDIIKKYTSREFSAQTAQRIGQMFHLGVLGSAASSVIGKASSAARGGTRNVPIPQALAISALSGGMAAVGALNQHTAITVKNNRREGDTDIGLKQQVLRGVMGGANEALSQRRATKASQAINALVQRSDVEALLSRAKALTQRSGATSSATHASPALTLPEAVEQLRPGVASASQSHEVIVQIGEEDRALPPA"
SeqD = "MDDETKKLKNKNKEAKEGDDVVAAESSFGSMNLHIDPTLITMNDVRQLGTQQNAALNRDLFLALKGKHPNLPDKDKDFHIAMMLYRLAVKSSSLQSDDDTTGITYTREGVDVNLPDKLWTDVVFNSKGIGNRTNALRVWGRTNDALYLAFCRQNRNLSYGGRPLDAGIPAGYHYLCADFLTGAGLTDLECAVYIQAKEQLLKRRGADEVVVTNVRQLGKFNTR"
SeqE = "SGVLWDVPSPPETQKAELEEGVYRIKQQGIFGKTQVGVGVQKEGVFHTMWHVTRGAVLTYNGKRLEPNWASVKKDLISYGGGWRLSAQWQKGEEVQVIAVEPGKNPKNFQTMPGTFQTTTGEIGAIALDFKPGTSGSPIINREGKVVGLYGNGVITKNGGYVSGIAQTNAEPDGPTPELEEEMFKKRNLTIMDLHPGSGKTRKYLPAIVREAIKRRLRTLILAPTRVVAAEMEEALKGLPIRYQTTATKSEHTGREIVDLMCHATFTMRLLSPVRVPNYNLIIMDEAHFTDPASIAARGYISTRVGMGEAAAIFMTATPPGTADAFPQSNAPIQDEERDIPERSWNSGNEWITDFAGKTVWFVPSIKAGNDIANCLRKNGKKVIQLSRKTFDTEYQKTKLNDWDFVVTTDISEMGANFKADRVIDPRRCLKPVILTDGPERVILAGPMPVTAASAAQRRGRVGRNPQKENDQYIFTGQPLNNDEDHAHWTEAKMLLDNINTPEGIIPALFEPEREKSAAIDGEYRLKGESRKTFVELMRRGDLPVWLAHKVASEGIKYTDRKWCFDGQRNNQILEENMDVEIWTKEGEKKKLRPRWLDARTYSDPLALKEFKDFAAGRK"

result1 = check_sequence_similarity(SeqA, SeqE)
result2 = check_sequence_similarity(SeqB, SeqE)
result3 = check_sequence_similarity(SeqC, SeqE)
result4 = check_sequence_similarity(SeqD, SeqE)
print("The similarity score with Omicron is: ", result1)
print("The similarity score with Influenza is: ", result2)
print("The similarity score with Xant is: ", result3)
print("The similarity score with CTV is: ", result4)
