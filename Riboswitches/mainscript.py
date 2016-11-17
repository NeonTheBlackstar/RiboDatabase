import os
import re
import sys
import linecache
sys.path.insert(0, './Programs/shine-dalgarno')
import __init__
# python3 mainscript.py NC_000964.3

def promoters(promoter_id):
    #Promotory - Szymon

    fh1 = open('./Programs/PromPredict_temp.txt', 'w')
    fh1.write('{0}.fasta\n100\ndefault'.format(promoter_id))#nadpisywanie pliku z argumentami do PromPredict
    fh1.close()

    os.system('cp ./Genomes/{0}.fasta ./'.format(promoter_id))#kopiowanie pliku fasta do katalogu z PromPredict
    os.system('touch ./Results/{0}.promoters.bed'.format(promoter_id))
    os.system('./Programs/PromPredict_genome < ./Programs/PromPredict_temp.txt')

    fh2 = open('{0}_PPde.txt'.format(promoter_id[:-2]), 'r+')
    fh3 = open('./Results/{0}.promoters.bed'.format(promoter_id), 'a')

    lines = [] #list of lines from PromPredict

    for i in fh2:
        if i.startswith('#'):
            pass
        else:
            lines.append(i)
    fh2.close()

    for i in range(0, len(lines)):
        lines[i] = lines[i].split()

    for i in range(0, len(lines)):
        start = lines[i][2] #pozycja startu
        end = lines[i][3] #pozycja konca
        _id = start #id = start
        level = lines[i][-1][-1] #jakosc
        fh3.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(promoter_id, start, end, _id, level))
    fh3.close()

    #Usuwanie niepotrzebnych plikow wynikowych
    os.system('rm {0}_PPde.txt'.format(promoter_id[:-2]))
    os.system('rm {0}_stb.txt'.format(promoter_id[:-2]))
    os.system('rm {0}_GCstat.txt'.format(promoter_id[:-2]))
    os.system('rm {0}.fasta'.format(promoter_id))

def aptamers(genome):
    #Aptamery - Jakub
    lista = []
    lista = os.listdir('Alignments')
    counter = 0

    bedfile = open("./Results/{0}.aptamers.bed".format(genome), "w")

    for i in range(0, len(lista)):
        
        os.system("./Programs/cmsearch ./Alignments/{0} ./Genomes/{1}.fasta > ./Results/processing.txt".format(lista[i], genome))

        processingfile = open("./Results/processing.txt", "r")

        for line in processingfile:
            temp = line.split()
            if len(temp) > 5:
                if temp[1] == "!" and temp[5][0:1] == "g":
                    if temp[8] == "-":
                        bedfile.write("{5}\t{1}\t{0}\t{2}_{0}\t{3}\t{4}\n".format(temp[6], temp[7], lista[counter][0:-3], temp[3], temp[8], genome))
                    else:
                        bedfile.write("{5}\t{0}\t{1}\t{2}_{0}\t{3}\t{4}\n".format(temp[6], temp[7], lista[counter][0:-3], temp[3], temp[8], genome))
        counter = counter + 1
        processingfile.close()
    bedfile.close()
    
    #os.system("rm ./Results/processing.txt")
    os.system('sort -nk2,2 ./Results/{0}.aptamers.bed -o ./Results/aptamers.sorted.bed'.format(genome))
    os.system('rm ./Results/{0}.aptamers.bed'.format(genome))
    os.system('mv ./Results/aptamers.sorted.bed ./Results/{0}.aptamers.bed'.format(genome))

def terminators(genome):
    #Terminatory - Pawel
    fh1 = open('./Genomes/{0}.gff'.format(genome))
    fh2 = open('temp.gff', 'w')
    semaphore=0
    for line in fh1:
        temp = line.split('\t')
        if temp[0][0]!='#':
            if (temp[2]=='region' and semaphore==0):
                semaphore=1
            else:
                fh2.write(line)
    fh1.close()
    fh2.close()
    os.system('bedtools closest -s -D a -io -iu -a ./Results/{0}.aptamers.bed -b temp.gff > bed_output.txt'.format(genome))
    os.system('rm temp.gff')

    fh1 = open('bed_output.txt')
    fh2 = open('./Results/{0}.ptt'.format(genome), 'w')

    fh2.write('Location\tStrand\tLength\tPID\tGene\tSynonym\tCode\tCOG\tProduct\n\n\n')

    for line in fh1:
        temp = line.split('\t')
        if (temp[8]=='gene'):
            location1=temp[1]+'..'+temp[2]
            location2=temp[9]+'..'+temp[10]
            strand=temp[5]
            length1=str(int(temp[2])-int(temp[1])+1)
            length2=str(int(temp[10])-int(temp[9])+1)
            gene1 = temp[3]
            name = re.search(r'Name=[^;^\n]*',temp[14])
            if (str(name) == 'None'):
                gene2 = '-'
            else:
                gene2 = name.group()
                gene2 = gene2[5:]
                locus_tag = re.search(r'locus_tag=[^;^\n]*',temp[14])
                if (str(locus_tag) == 'None'):
                    synonym = '-'
                else:
                    synonym = locus_tag.group()
                    synonym = synonym[10:]
        if (temp[8]=='CDS' or temp[8]=='exon'):
            protein_id = re.search(r'protein_id=[^;^\n]*',temp[14])
            if (str(protein_id) == 'None'):
                pid = '-'
            else:
                pid = protein_id.group()
                pid = pid[11:]
                product_name = re.search(r'product=[^;^\n]*',temp[14])
                if (str(product_name) == 'None'):
                    product = '-'
                else:
                    product=product_name.group()
                    product=product[8:]
            fh2.write(location1+'\t'+strand+'\t'+length1+'\t'+pid+'\t>'+gene1+'\t>'+gene1+'\t-\t-\t'+gene2+';'+synonym+'\n')
            fh2.write(location2+'\t'+strand+'\t'+length2+'\t'+pid+'\t'+gene2+'\t'+synonym+'\t-\t-\t'+product+'\n')
    os.system('rm bed_output.txt')

    fh1.close()
    fh2.close()
    
    fh1 = open('./Genomes/{0}.fasta'.format(genome))
    fh2 = open('sequence.fasta', 'w')
    for line in fh1:
        if line[0]=='>':
            fh2.write('>{0}\n'.format(genome))
        else:
            fh2.write(line)
    
    os.system('transterm -p ./Programs/transterm/expterm.dat sequence.fasta ./Results/{0}.ptt > output.tt'.format(genome))
    os.system('rm sequence.fasta')

    fh1 = open('output.tt')
    fh2 = open('./Results/{0}.terminators.bed'.format(genome), 'w')

    data = []
    RF = []
    terminators_tt = []
    terminators_bed = []

    for line in fh1:
        if (line != '\n'):
            data.append(line)

    counter=0
    for line in data:
        temp = line.split()
        if (line[0][0] == '>' and temp[4] == '+'):
                end_RF = temp[3]
                for i in range(counter+1,len(data)):
                    check = data[i].split()
                    if (check[0] == 'TERM'):
                        start_term = check[2]
                        distance = int(start_term)-int(end_RF)
                        if (distance<150):
                            RF.append(line[1:])
                            terminators_tt.append(data[i])
                            break
        if (line[0][0] == '>' and temp[4] == '-'):
                start_RF = temp[3]
                j=counter-1
                for i in range(0,counter):
                    check = data[j].split()
                    if (check[0] == 'TERM'):
                        end_term = check[2]
                        distance = int(start_RF)-int(end_term)
                        if (distance<150):
                            RF.append(line[1:])
                            terminators_tt.append(data[j])
                            break
                    j=j-1			
        counter=counter+1

    counter=0
    for line in terminators_tt:
        temp1 = line.split()
        temp2 = RF[counter].split()
        counter=counter+1	
        if (temp1[5] == '+'): 
            fh2.write('{0}\t'.format(genome)+temp1[2]+'\t'+temp1[4]+'\t'+temp2[0]+';'+temp2[6]+'\t'+temp1[7]+'\t'+temp1[5]+'\n')
        if (temp1[5] == '-'): 
            fh2.write('{0}\t'.format(genome)+temp1[4]+'\t'+temp1[2]+'\t'+temp2[0]+';'+temp2[6]+'\t'+temp1[7]+'\t'+temp1[5]+'\n')

    fh1.close()
    fh2.close()
    
    os.system('rm output.tt')

def bedtools(genome):
    #ignore overlaps, ignore downstream, signed dist. w. r. t. A's strand
    os.system('bedtools closest -io -id -D a -a ./Results/{0}.aptamers.bed -b ./Results/{0}.promoters.bed > ./Results/{0}.bedAP.txt'.format(genome))

def comparison(genome, distance_P = 150, distance_T = 150, distance_SD = 200):
    #format: genome start_R end_R name_R strand_R start_P end_P distance_P start_T end_T strand_T distance_T start_SD end_SD strand_SD distance_SD gene_annotation type_of_mechanism
    #default distance: P = 150, T = 150, SD = 200 
    final = open('./Results/{0}.final.txt'.format(genome), 'w')
    aptamers = open('./Results/{0}.bedAP.txt'.format(genome), 'r')
    for lineA in aptamers:
        P_exist = False
        T_exist = False
        SD_exist = False
        tempA = lineA.split()
        final.write('{0}\t{1}\t{2}\t{3}\t{4}\t'.format(genome, tempA[1], tempA[2], tempA[3], tempA[5]))
        if int(tempA[11]) >= (-(int(distance_P))):
            final.write('{0}\t{1}\t{2}\t'.format(tempA[7], tempA[8], tempA[11]))
            P_exist = True
        else:
            final.write('---\t---\tNo_P\t')
        terminators = open('./Results/{0}.bedAT.txt'.format(genome), 'r')
        for lineT in terminators:
            tempT = lineT.split()
            if int(tempT[13]) <= distance_T and tempT[3] == tempA[3]:
                final.write('{0}\t{1}\t{2}\t{3}\t'.format(tempT[7], tempT[8], tempT[12], tempT[13]))
                T_exist = True
                break
        else:
            final.write('---\t---\t---\tNo_T\t')
        terminators.close()
        '''
        sdsequence = open('./Results/{0}.bedASD.txt'.format(genome))
        for lineSD in sdsequence:
            tempSD = lineSD.split()
            if ...
                ...
                break
        else:
            final.write(...)
        sdsequence.close()
        '''
        
        if P_exist and T_exist:
            final.write('Termination\n')
        if P_exist and not T_exist and not SD_exist:
            final.write('Unknown\n')
        if P_exist and SD_exist and not T_exist:
            final.write('Translation\n')
        if not P_exist and T_exist:
            final.write('Termination\n')
        if not P_exist and not T_exist:
            final.write('Unknown\n')

        

aptamers(sys.argv[1])
#promoters(sys.argv[1])
#terminators(sys.argv[1])
#__init__.runShineDalAnalysis(sys.argv[1], True) # If set true, then meme will be runed
#bedtools(sys.argv[1])
#comparison(sys.argv[1])


