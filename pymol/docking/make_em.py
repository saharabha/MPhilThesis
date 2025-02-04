import enz

BM3_DM = 'MTIKEMPQPKTFGELKNLPLLNTDKPVQALMKIADELGEIFKFEAPGRVTRYLSSQRLIKEACDESRFDKNLSQALKFVRDFFGDGLVTSWTHEKNWKKAHNILLPSFSQQAMKGYHAMMVDIAVQLVQKWERLNADEHIEVPEDMTRLTLDTIGLCGFNYRFNSFYRDQPHPFITSMVRALDEAMNKLQRANPDDPAYDENKRQFQEDIKVMNDLVDKIIADRKASGEQSDDLLTHMLNGKDPETGEPLDDENIRYQIITFLIAGHETTSGLLSFALYFLVKNPHVLQKAAEEAARVLVDPVPSYKQVKQLKYVGMVLNEALRLWPTAPAFSLYAKEDTVLGGEYPLEKGDELMVLIPQLHRDKTIWGDDVEEFRPERFENPSAIPQHAFKPFGNGQRACIGQQFALHEATLVLGMMLKHFDFEDHTNYELDIKETLTLKPEGFVVKAKSKKIPLGGIPSPSTEQSAKKVRK*'

PIOGLITAZONE = 'CCC1=CN=C(C=C1)CCOC2=CC=C(C=C2)CC3C(=O)NC(=O)S3'

def main():
    p = enz.protein('4KEY.pdb', 
            seq = BM3_DM, 
            cofactors = ['HEM'], 
            key_sites = [82, 87, 400, 49, 51, 181, 188, 263, 330])

    r1 = p.dock(PIOGLITAZONE)
    r1.save('DM')

    p.mutate(75,'W')
    p.refold()
    r2 = p.dock(PIOGLITAZONE)
    r2.save('DM_L75W')

    p.mutate(188,'S')
    p.refold()
    r3 = p.dock(PIOGLITAZONE)
    r3.save('DM_L75W_L188S')

    p.mutate(75, 'L')
    p.refold()
    r4 = p.dock(PIOGLITAZONE)
    r4.save('DM_L188S')
    

if __name__ == '__main__':
    main()
