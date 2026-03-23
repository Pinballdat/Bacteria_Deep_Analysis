# Phân tích các genes Stress Response & Environmental Adaptation Genes

## Quy trình phân tích cụ thể

### Chú giải cấu trúc (CDS, rRNA, tRNA)

- Sử dụng công cụ Prokka

### Chú giải chức năng (GO, COG, KEGG, Pfam)


- Sử dụng công cụ Eggnog_mapper

a/ Phân nhóm theo COG

- Stress genes thường nằm trong các nhóm COG như sau: O (Chaperones), P (Inorganic ion transport), T (Signal transduction), V (Defense mechanisms)

b/ Phân nhóm theo GOs

Trong ene Ontology (GO), các gene liên quan đến Stress Response & Environmental Adaptation chủ yếu tập trung ở nhánh Biological Process (BP) kèm theo một phần ở Molecular Function (MF):

- Heat / temperature stress
  - GO:0009408 - response to heat (OGCDPPDJ_00287 - Lon protease 1, OGCDPPDJ_00350 - D_aminoacyl-tRNA deacylase, OGCDPPDJ_00411 - Putative cysteine protease YraA, OGCDPPDJ_00591 - Endoribonuclease YbeY,  - RNA polymerease sigma factor SigA, OGCDPPDJ_00620 - superoxide dismutase, OGCDPPDJ_00912 - hypo, OGCDPPDJ_01374 - Spore coat prot M, OGCDPPDJ_02401 - Chaperone prot HtpG,  - polyribonucleotide transferase, OGCDPPDJ_02722 - ATP_dependent protease ATPase subunit ClpY, OGCDPPDJ_02723 - ClpQ, OGCDPPDJ_02862 - GTP-binding protein TypA/BipA, OGCDPPDJ_03704 - Phosphoserine phosphatase RbsX, OGCDPPDJ_04212 - Acylphosphatase, OGCDPPDJ_04231 - General stress prot 18, OGCDPPDJ_04409 - 33 kDa Chaperonin, OGCDPPDJ_04416 - Stage II prot E)
  - GO:0009409 - response to cold ( - Glycine betaine transporter OupD, OGCDPPDJ_00219 - Translation initiation factor IF-3, OGCDPPDJ_00609 - DEADbox ATP_dependent RNA helicase CshB, OGCDPPDJ_00943 - Cold shock protein CspD, OGCDPPDJ_02317 - ATP_dependent RNA helicase DbpA, OGCDPPDJ_02673 - Ribosome-binding factor A, OGCDPPDJ_02862 - GTP-binding protein TypA/BipA, OGCDPPDJ_02899 - putative ABC transporter ATP_binding prot YbiT, OGCDPPDJ_03295 - Enoyl_reductase [NADH] FabI, OGCDPPDJ_03553 - Cold shock protein CspB, OGCDPPDJ_03705 - RNA polymerase sigma-B factor, OGCDPPDJ_03720 - RNA helicase CshA, OGCDPPDJ_04195 - RNA helicase YfmL)

- Oxidative stress
  - GO:0006979 - response to oxidative stress (OGCDPPDJ_00120 - Thioredoxin-like protein YtpP, OGCDPPDJ_00193 - Isocitrate dehydrogenase, OGCDPPDJ_00257 - Thiorendoxin, OGCDPPDJ_00411 - putative cysteine protease YraA, OGCDPPDJ_00620 - superoxide dismutase [Mn], OGCDPPDJ_01118 - Thiorendoxin, OGCDPPDJ_01204 - superoxide dismutase-like prot YojM, OGCDPPDJ_01211 - hypo, OGCDPPDJ_01279 - putative protease YdeA, OGCDPPDJ_01613 - hypo, OGCDPPDJ_01781 - phospholycarate mutase, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311  - Catalase HPII, OGCDPPDJ_02401 - Chaperone prot HtpG, OGCDPPDJ_02429, OGCDPPDJ_02557, OGCDPPDJ_02830 - 50S ribosomal prot L32, OGCDPPDJ_02880 (dihydrolipoyl dehydrogenase), OGCDPPDJ_03005 - hypo, OGCDPPDJ_03582 - calatse, OGCDPPDJ_03642 - hypo, OGCDPPDJ_03705 - RNA polymerase sigma-B factor, OGCDPPDJ_03723 - Thirodoxin-like prot Ybdp, OGCDPPDJ_04231 - Genaral stress prot 18, OGCDPPDJ_04320 - putative peroxiredoxin bcp, OGCDPPDJ_04409 - 33 kDa chapronin)
  - GO:0034599 - cellular response to oxidative stress (OGCDPPDJ_00120 - Thioredoxin-like protein YtpP, OGCDPPDJ_00257 - Thiorendoxin, OGCDPPDJ_00620 - superoxide dismutase [Mn], OGCDPPDJ_01118 - Thiorendoxin, OGCDPPDJ_01204 - superoxide dismutase-like prot YojM, OGCDPPDJ_01211 - hypo, OGCDPPDJ_01613 - hypo, OGCDPPDJ_02401 - Chaperone prot HtpG, OGCDPPDJ_03005 - hypo, OGCDPPDJ_03642 - hypo, OGCDPPDJ_03723, OGCDPPDJ_04320)
  - GO:0000302 - response to reactive oxygen species (OGCDPPDJ_00620, OGCDPPDJ_01204, OGCDPPDJ_01211, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311 - Catalase HPII, OGCDPPDJ_02401, OGCDPPDJ_02830, OGCDPPDJ_03005, OGCDPPDJ_03582)
  - GO:0072593 - reactive oxygen species metabolic process (OGCDPPDJ_00411 - putative cysteine protease YraA, OGCDPPDJ_00620, OGCDPPDJ_01204, OGCDPPDJ_01211, OGCDPPDJ_01279 - putative protease YdeA, OGCDPPDJ_02271, OGCDPPDJ_02311, OGCDPPDJ_03045 - Flavohemoprotein, OGCDPPDJ_03582 - Vegetative catalase, OGCDPPDJ_04211 - Nitric oxide synthase oxygenase, OGCDPPDJ_04231 - General stress prot 18)

- Osmotic & salt stress
  - GO:0006970 - response to osmotic stress (OGCDPPDJ_00098 - Glycine betaine transporter OpuD, OGCDPPDJ_02921 - putative MscS family prot YkuT, OGCDPPDJ_03207 - hypo, OGCDPPDJ_04241 - putative MscS family prot YfkC)
  - GO:0009651 - response to salt stress (OGCDPPDJ_03207)
  - GO:0042538 - hyperosmotic response (No prot)
  - GO:0042539 - hypoosmotic response (No prot)

- Acid / pH stress
  - GO:0009268 - response to pH (OGCDPPDJ_00411 - putative cysteine protease YraA, OGCDPPDJ_00620, OGCDPPDJ_04231)
  - GO:1901700 - response to acidic pH (OGCDPPDJ_00134 - Acetoin utilization prot AcuA, OGCDPPDJ_00444 - leucine-responsive regulatory prot, OGCDPPDJ_00603 - RNA polymerase sigma factor SigA, OGCDPPDJ_00620, OGCDPPDJ_01204, OGCDPPDJ_01211, OGCDPPDJ_02011 - hypo, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311, OGCDPPDJ_02401, OGCDPPDJ_02429 - Akyl hydroproxide reductase C, OGCDPPDJ_02760 - Serine/threonine prot kinase PrkC, OGCDPPDJ_02830, OGCDPPDJ_03005 - hypo, OGCDPPDJ_03372 - hypo, OGCDPPDJ_03386 - scyllo-inositol 2-dehydrogenase (NAD(+)), OGCDPPDJ_03537 - Glycerol uptake operon antiterminator regularoty prot, OGCDPPDJ_03582 - Vegetative catalase, OGCDPPDJ_03754 - HTH-type transcriptional regulator LrpC, OGCDPPDJ_04096 - LprC, OGCDPPDJ_04097 - L-methionine/branched-chain amino acid exporter YjeH)
  - GO:1901701 - response to alkaline pH (OGCDPPDJ_00134, OGCDPPDJ_00620, OGCDPPDJ_01204, OGCDPPDJ_01211, OGCDPPDJ_02401, OGCDPPDJ_02760, OGCDPPDJ_03005, OGCDPPDJ_03372, OGCDPPDJ_03386, OGCDPPDJ_03537, OGCDPPDJ_04097)

- Starvation & nutrient limitation

  - GO:0009267 - response to starvation (OGCDPPDJ_00036 - 50S ribosomal prot L31 type B, OGCDPPDJ_00134, OGCDPPDJ_00432 - hypo, OGCDPPDJ_00574 - GrpE, OGCDPPDJ_00912 - hypo,  OGCDPPDJ_01374 - Spore coat prot M, OGCDPPDJ_02429 - Alkyl hydroperoxide reductase C, OGCDPPDJ_03565 - hypo, OGCDPPDJ_03685 - RNA polymerase-binding transcription factor CarD, OGCDPPDJ_03705 - RNA polymerase sigma-B factor, OGCDPPDJ_04379 - 50S ribosomal prot L11)
  - GO:0042594 - response to nutrient levels (OGCDPPDJ_00036, OGCDPPDJ_00134, OGCDPPDJ_00349 - GTP pyrophoskinase, OGCDPPDJ_00432, OGCDPPDJ_00574, OGCDPPDJ_00912, OGCDPPDJ_01342 - Acyl-CoA dehydrogenase, OGCDPPDJ_01374, OGCDPPDJ_02256 - GTP pyrophosphokinase YwaC, OGCDPPDJ_02429,  - GTP pyrophosphokinase YjbM, OGCDPPDJ_03565, OGCDPPDJ_03685, OGCDPPDJ_03705, OGCDPPDJ_04379)

- Heavy metal / toxic compound stress
  - GO:0046686 - response to cadmium ion (OGCDPPDJ_00432, OGCDPPDJ_00541 - Cadmium-induced protein CadI, OGCDPPDJ_03655 - hypo, OGCDPPDJ_04394 - Negative regulator of genetic competence ClpC/MecB, OGCDPPDJ_04395 - Prot-arginine kinase, OGCDPPDJ_04396 - Prot-arginine kinase activator prot, OGCDPPDJ_04397 - Transcriptional regulator CtsR)
  - GO:0010038 - response to metal ion (OGCDPPDJ_00031 - Manganese transport system membrane protein MntC, OGCDPPDJ_00032 - Manganese transport system membrane protein MntD, OGCDPPDJ_00432, OGCDPPDJ_00541, OGCDPPDJ_00620 - Superoxide dismutase [Mn], OGCDPPDJ_00673 - HTH-type transcriptional regulator MntR, OGCDPPDJ_00912 - hypo, OGCDPPDJ_01374, OGCDPPDJ_01534 - dehydrogenase, OGCDPPDJ_01544 - Ferredoxin--NADP reductase 2, OGCDPPDJ_02071 - Urease subunit beta, OGCDPPDJ_02072 - Urease subunit gamma, OGCDPPDJ_03655 - hypo, OGCDPPDJ_03743 - Divalent metal cation transporter MntH, OGCDPPDJ_03860 - Ferredoxin--NADP reductase 1, OGCDPPDJ_03901 - High-affinity zinc uptake system membrane protein ZnuB, OGCDPPDJ_04201 - Fe(3+)-citrate-binding protein YfmC, OGCDPPDJ_04394 - Negative regulator of genetic competence ClpC/MecB, OGCDPPDJ_04395 - Protein-arginine kinase, OGCDPPDJ_04396 - Protein-arginine kinase activator protein, OGCDPPDJ_04397 - Transcriptional regulator CtsR)
  - GO:0046688 - response to copper ion (OGCDPPDJ_04394, OGCDPPDJ_04395, OGCDPPDJ_04396, OGCDPPDJ_04397)
  - GO:0009636 - response to toxic substance (OGCDPPDJ_00120 - Thioredoxin-like protein YtpP, OGCDPPDJ_00257 - Thioredoxin, OGCDPPDJ_00411 - Putative cysteine protease YraA, OGCDPPDJ_00620 - Superoxide dismutase [Mn], OGCDPPDJ_00751 - D-serine dehydratase, OGCDPPDJ_01118 - Thioredoxin, OGCDPPDJ_01204 - Superoxide dismutase-like protein YojM, OGCDPPDJ_01211 - hypo, OGCDPPDJ_01279 - Putative protease YdeA, OGCDPPDJ_01613 - hypo, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311 - Catalase HPII, OGCDPPDJ_02429 - Alkyl hydroperoxide reductase C, OGCDPPDJ_02890 - Adenine deaminase, OGCDPPDJ_03582 - Vegetative catalase, OGCDPPDJ_03642 - hypo, OGCDPPDJ_03723 - Thioredoxin-like prot YdbP, OGCDPPDJ_04231 - General stress prot 18, OGCDPPDJ_04306 - Trifunctional nucleotide phosphoesterase prot YfkN, OGCDPPDJ_04320 - Putative peroxiredoxin bcp)

- DNA damage & stress genome stability
  - GO:0006974 - cellular response to DNA damage stimulus (OGCDPPDJ_00008 - GlgB, OGCDPPDJ_00197 - DNA polymerase I,  OGCDPPDJ_00244 - Ribonuclease HIII, OGCDPPDJ_00248 - Endonuclease MutS2, OGCDPPDJ_00258 - UvrABC system prot C, OGCDPPDJ_00334 - DNA helicase RuvA, OGCDPPDJ_00335 - DNA helicase B, OGCDPPDJ_00411, OGCDPPDJ_00482 - Prot RecT, OGCDPPDJ_00596 - DNA repair prot RecO, OGCDPPDJ_00610 - Endonuclease 4, OGCDPPDJ_00701 - DnA repair prot RecN, OGCDPPDJ_00751, OGCDPPDJ_00832 - RNA helicase DbpA, OGCDPPDJ_00896 - 3-5 exonuclease DinG, OGCDPPDJ_00905 - Holliday junction resolvase RecU, OGCDPPDJ_00935 - 5-3 exonuclease, OGCDPPDJ_01179 - Purine nucleoside phosphorylase DeoD-type, OGCDPPDJ_01223 - DNA helicase RecQ, OGCDPPDJ_01385 - Cell division suppressor prot YneA, OGCDPPDJ_01386 - LexA repressor, OGCDPPDJ_01432 - Putative membrane prot YuaF, OGCDPPDJ_01441 - hypo, OGCDPPDJ_01598 - UvrABC system prot C, OGCDPPDJ_01891 - Pyrophosphatase PpaX, OGCDPPDJ_01937 - ComF prot 1, OGCDPPDJ_02134 - Resporatory nitrate reductase 1 beta chain, OGCDPPDJ_02204 - Uracil-DNA glycosylase, OGCDPPDJ_02270 - DNA glycosylase, OGCDPPDJ_02352 - CTP pyrophosphohydrolase, OGCDPPDJ_02401 - Chaperone prot HtpG, OGCDPPDJ_02553 - Exodeoxyribonuclease, OGCDPPDJ_02575 - DNA replication and repair prot RecF, OGCDPPDJ_02635 - DNA mismatch repair prot MutL, OGCDPPDJ_02636 - DNA mismatch repair prot MutS,  OGCDPPDJ_02646 - Prot RecA, OGCDPPDJ_02673 - Ribosome binding factor A, OGCDPPDJ_02732 - Ribonuclease HII, OGCDPPDJ_02766 - Primosomal prot N, OGCDPPDJ_02992 - methyltransferase constitutive, OGCDPPDJ_03106 - Putative manganese catalase, OGCDPPDJ_03210 - hypo, OGCDPPDJ_03244 - Crossover junction endodeoxyribonuclease RuvC, OGCDPPDJ_03369 - hypo, OGCDPPDJ_03409 - helicase subunit B, OGCDPPDJ_03524 - hypo, OGCDPPDJ_03736 - Putative manganese catalase, OGCDPPDJ_03947 - homocysteine S-methyltransferase, OGCDPPDJ_04105 - DNA ligase, OGCDPPDJ_04141 - manganese catalase, OGCDPPDJ_04183 - Fosmidomycin resistance prot, OGCDPPDJ_04218 - PTS system N-acetylglucosamine-specific EIICB component, OGCDPPDJ_04227 - Trehalose-6-phosphate hydrolase, OGCDPPDJ_04230 - YfkN, OGCDPPDJ_04231, OGCDPPDJ_04247 - hypo,  - Regulatory prot RecX, OGCDPPDJ_04462 - Recombination prot RecR, OGCDPPDJ_04472 - Pyridoxal 5-phosphate synthase subunit PdxT)
  - GO:0006281 - DNA repair (OGCDPPDJ_00197 - DNA plolymerase I, OGCDPPDJ_00244, OGCDPPDJ_00248, OGCDPPDJ_00334, OGCDPPDJ_00411, OGCDPPDJ_00482, OGCDPPDJ_00596, OGCDPPDJ_00610, OGCDPPDJ_00701, OGCDPPDJ_00832, OGCDPPDJ_00896, OGCDPPDJ_00905, OGCDPPDJ_00935, OGCDPPDJ_01223, OGCDPPDJ_01891, OGCDPPDJ_01937, OGCDPPDJ_02204, OGCDPPDJ_02270, OGCDPPDJ_02352, OGCDPPDJ_02553, OGCDPPDJ_02575, OGCDPPDJ_02635, OGCDPPDJ_02636, OGCDPPDJ_02646, OGCDPPDJ_02732, OGCDPPDJ_02766, OGCDPPDJ_02992, OGCDPPDJ_03244, OGCDPPDJ_03409, OGCDPPDJ_04105, OGCDPPDJ_04231, OGCDPPDJ_04247, OGCDPPDJ_04462)
  - GO:0009432 - SOS response (OGCDPPDJ_00334, OGCDPPDJ_00335 - Holliday junction ATP-dependent DNA helicase RuvB, OGCDPPDJ_00701, OGCDPPDJ_01385 - Cell division suppressor protein YneA, OGCDPPDJ_01386 - LexA repressor, OGCDPPDJ_02646, OGCDPPDJ_04299 - Regulatory protein RecX, OGCDPPDJ_04472 - Pyridoxal 5'-phosphate synthase subunit PdxT)

- Stress do kháng sinh & yếu tố ngoại lai
  - GO:0046677 - response to antibiotic (OGCDPPDJ_00134 - Acetoin utilization protein AcuA, OGCDPPDJ_00744 - 50S ribosomal protein L33 2, OGCDPPDJ_01199 - Multidrug resistance protein NorM, OGCDPPDJ_01387 - Metallothiol transferase FosB, OGCDPPDJ_01446 - Undecaprenyl-diphosphatase, OGCDPPDJ_01915 - Cell division ATP-binding protein FtsE, OGCDPPDJ_02117 - UDP-N-acetylglucosamine 1-carboxyvinyltransferase 2, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311 - Catalase HPII, OGCDPPDJ_02483 - putative transporter YycB, OGCDPPDJ_03207 - hypo, OGCDPPDJ_03372 - hypo, OGCDPPDJ_03389 - putative FMN/FAD exporter YeeO, OGCDPPDJ_03537 - Glycerol uptake operon antiterminator regulatory protein, OGCDPPDJ_03582 - Vegetative catalase, OGCDPPDJ_03705 - RNA polymerase sigma-B factor, OGCDPPDJ_04183 - Fosmidomycin resistance protein)
  - GO:0097237 - cellular response to antibiotic (OGCDPPDJ_00120 - Thioredoxin-like protein YtpP, OGCDPPDJ_00257 - Thioredoxin, OGCDPPDJ_00411 - Putative cysteine protease YraA, OGCDPPDJ_00620, OGCDPPDJ_01118 - Thioredoxin, OGCDPPDJ_01204 - Superoxide dismutase-like protein YojM, OGCDPPDJ_01211 - hypo, OGCDPPDJ_01279 - putative protease YdeA, OGCDPPDJ_01613 - hypo, OGCDPPDJ_02271 - Catalase, OGCDPPDJ_02311 - Catalase HPII, OGCDPPDJ_02429 - Alkyl hydroperoxide reductase C, OGCDPPDJ_02890 - Adenine deaminase, OGCDPPDJ_03582 - Vegetative catalase, OGCDPPDJ_03642 - hypo, OGCDPPDJ_03723 - Thioredoxin-like protein YdbP, OGCDPPDJ_04231 - General stress protein 18, OGCDPPDJ_04320 - Putative peroxiredoxin bcp)

- Biofilm, motility & surface adaptation
  - GO:0042710 - biofilm formation (OGCDPPDJ_00134 - Acetoin utilization protein AcuA, OGCDPPDJ_00744 - 50S ribosomal protein L33 2, OGCDPPDJ_01199 - Multidrug resistance protein NorM, OGCDPPDJ_01387, OGCDPPDJ_01446, OGCDPPDJ_01915, OGCDPPDJ_02117, OGCDPPDJ_02271, OGCDPPDJ_02311, OGCDPPDJ_02483, OGCDPPDJ_03207, OGCDPPDJ_03372, OGCDPPDJ_03389, OGCDPPDJ_03537, OGCDPPDJ_03582, OGCDPPDJ_03705, OGCDPPDJ_04183)
  - GO:0001539 - cilium or flagellum-dependent cell motility (OGCDPPDJ_00130 - Chemotaxis prot PomA, OGCDPPDJ_01924 - Flagellar hook-associated protein 2, OGCDPPDJ_02046 - Flagellar basal-body rod protein FlgG, OGCDPPDJ_02047 - Flagellar basal-body rod protein FlgG, OGCDPPDJ_02709 - Flagellar basal-body rod protein FlgG, OGCDPPDJ_02710 - hypo, OGCDPPDJ_02711 - hypo, OGCDPPDJ_02716 - Flagellar motor switch protein FliG, OGCDPPDJ_02719 - Flagellar basal-body rod prot FlgC, OGCDPPDJ_02720 - FlgB, OGCDPPDJ_02976 - Chemotaxis prot PomA)
  - GO:0006935 - chemotaxis (OGCDPPDJ_01996 - Ribose import binding prot RbsB, OGCDPPDJ_02693 - CheY-P phosphatase CheC, OGCDPPDJ_02694 - Chemotaxis prot Chew, OGCDPPDJ_02703 - Flagellar biosynthetic prot FliP, OGCDPPDJ_02706 - hypo, OGCDPPDJ_02707 - Flaggellar motor switch prot FliM, OGCDPPDJ_02716, OGCDPPDJ_02939 - Chemotaxis prot CheV, OGCDPPDJ_02946 - Methyl-accepting chemotaxis prot McpC, OGCDPPDJ_03432 - Heme-based aerotactic transducer HemAT, OGCDPPDJ_04187 - Putative sensory transducer prot YfmS)

- Two-component systems & sensing
  - GO:0000160 - phosphorelay signal transduction system (OGCDPPDJ_00215 - Sensory trnasduction prot LytR, OGCDPPDJ_00316 - GTPase Obg, OGCDPPDJ_00703 - Stage 0 sporulation prot A, OGCDPPDJ_01487 - Sensor histidine kinase DcuS, OGCDPPDJ_01488 - Transcriptional regulatory DcuR)
  - GO:0000156 - two-component signal transduction system (OGCDPPDJ_00215, OGCDPPDJ_00703)


c/ Phân nhóm theo KEGG

- Xác định dựa vào map02020: Two-component system
  - Salt Stress -> DegS (K07777, OGCDPPDJ_01940) -> DegU (K07692, OGCDPPDJ_01939) -> Degradative enzymes
  - Low temperature -> DesK (K07778, OGCDPPDJ_01226) -> DesR (K07693, OGCDPPDJ_01225) -> Des (K010255, OGCDPPDJ_01227) -> Membrane phospholipid desaturase
  - Cell wall-active antibiotics -> LiaS (K11617, OGCDPPDJ_01646) -> LiaR (K11618, OGCDPPDJ_01645) -> LiaI (K11619, OGCDPPDJ_01650) - LiaH (K11620, OGCDPPDJ_01649) - LiaG (K11621, OGCDPPDJ_01648) - LiaF (K11622, OGCDPPDJ_01647) - LiaS (K11617, OGCDPPDJ_01646) - LiaR (K11618, OGCDPPDJ_01645)
  - Environment conditions: KinA (K02491, OGCDPPDJ_02942), KinB (K07697, OGCDPPDJ_01479), KapB (K06347, OGCDPPDJ_01480), KinC (K07698, OGCDPPDJ_02893), KinD (K13532, OGCDPPDJ_02979), KinE (K13533, OGCDPPDJ_02993) -> Spo0F (K02490, OGCDPPDJ_02120) -> Spo0B (K06375, OGCDPPDJ_00315) -> Spo0A (K07699, OGCDPPDJ_00703) -> Sporulation Biofilm formation
  - Oxygen limitation -> ResE (K07651, OGCDPPDJ_00824) -> ResD (K07775, OGCDPPDJ_00823) -> CtaA (K02259, OGCDPPDJ_02852): Aerobic and anaerobic respiration
  - Chemotaxis family: Attractant/Repellent ->  MCP(K03406, OGCDPPDJ_02946), CheW (K03408, OGCDPPDJ_02694), CheA (K03407, OGCDPPDJ_02695), cheR (K00575, OGCDPPDJ_00864) -> CheY (K03413, OGCDPPDJ_02705), CheV (K03415, OGCDPPDJ_02939), cheB (K03412, OGCDPPDJ_02696)

- Xác định dựa vào map02030: Bacteria Chemotaxis
  - MCP (K03406, OGCDPPDJ_02946)
  - CheD (K03411, OGCDPPDJ_02692)
  - CheR (K00575, OGCDPPDJ_00864)
  - CheB cheB (K03412, OGCDPPDJ_02696)
  - CheA (K03407, OGCDPPDJ_02695)
  - CheW (K03408, OGCDPPDJ_02694)
  - CheV (K03415, OGCDPPDJ_02939)
  - CheC (K03410, OGCDPPDJ_02693)
  - CheY CheY (K03413, OGCDPPDJ_02705)
  - FliG (K02410, OGCDPPDJ_02716)
  - FliM (K02416, OGCDPPDJ_02707)
  - FliN (K02417, OGCDPPDJ_02706)
  - MotA (K02556, OGCDPPDJ_02976)
  - MotB (K02557, OGCDPPDJ_02977)

- Xác định dựa vào map02024: Quorum Sensing (Bacillus)
  - ComX (K02253, OGCDPPDJ_01505)
  - ComQ (K02251, OGCDPPDJ_01506)
  - ComP (K07680, OGCDPPDJ_01504)
  - ComA (K07691, OGCDPPDJ_01503)
  - SrfAA (K15654, OGCDPPDJ_03835)
  - SrfAB (K15655, OGCDPPDJ_03834)
  - SrfAC (K15656, OGCDPPDJ_03833)
  - SrfAD (K15657, OGCDPPDJ_03832)
  - ComK (K02250, OGCDPPDJ_03428)

  - PhrC (K06353, OGCDPPDJ_03805)
  - PhrF (K06355, OGCDPPDJ_02153)
  - PhrK (K06358, OGCDPPDJ_01250)
  - PhrG (K06356, OGCDPPDJ_02458)
  - PhrH (K20389, OGCDPPDJ_04133)
  - PhrA (K06352, OGCDPPDJ_03111)
  - PhrE (K06354, OGCDPPDJ_00529)
  - SecDF (K12257, OGCDPPDJ_00344)
  - SecE (K03073, OGCDPPDJ_04381)
  - SecG (K03075, OGCDPPDJ_01758)
  - SecY (K03076, OGCDPPDJ_04345)
  - yajC (K03210, OGCDPPDJ_00339)
  - yidC (K03217, OGCDPPDJ_00738)
  - SecA (K03070, OGCDPPDJ_01919)
  - ftsY (K03110, OGCDPPDJ_02743)
  - SecB (K03071, )
  - SRP54 (K03106, OGCDPPDJ_02740)
  - OppA (K15580, OGCDPPDJ_03054)
  - OppB (K15581, OGCDPPDJ_03057)
  - OppC (K15582, OGCDPPDJ_03323, OGCDPPDJ_03328, OGCDPPDJ_03056)
  - OppD (K15583, OGCDPPDJ_03322, OGCDPPDJ_03055)
  - OppF (K10823, OGCDPPDJ_03321)
  - RapC (K06361, OGCDPPDJ_03806)
  - RapK (K06369, OGCDPPDJ_01251)
  - RapG (K06365, OGCDPPDJ_02457)
  - RapH (K06366, OGCDPPDJ_04132)
  - RapA (K06359, OGCDPPDJ_00984)
  - RapE (K06363, OGCDPPDJ_04120)
  - RapB (K06360, OGCDPPDJ_02076)
  - DegU
  - Spo0F, Spo0B, Spo0A

d/ Phân tích cụ thể

Một số TCS tiêu biểu:

|TCS|Chức năng|Mô tả|Các gene|
|---|---------|-----|--------|
|EnvZ/OmpR|Áp suất thẩm thấu, điều hòa porin||Không có|
|PhoR/PhoB|Thiếu phosphate||Có 4 gene: PhoADPR|
|CpxA/CpxR|Stress màng, protein gấp sai|Không có|
|BaeS/BaeR|Stress do kháng sinh, kim loại|
|RcsC/RcsB|Stress vỏ tế bào, capsule|
|DesK/DesR|Nhiệt độ (độ bão hòa lipid màng)|
|ResE - ResD - CtaA|Giúp vi khuẩn cảm nhận oxy và duy trì chuỗi truyền electron
|BceSRAB|Envelope stress response|Một hệ thống phòng vệ kháng kháng sinh kiểu cảm ứng – bơm tống, thuộc nhóm Bce-like envelope stress response system ở vi khuẩn Gram-positive|
|YdxKJML|Cell envelope stress response / antimicrobial peptide resistance system|Một hệ Two-Component System kết hợp ABC transporter, tham gia đáp ứng stress vách tế bào và kháng peptide kháng sinh|
|VanYW||VanY, VanW là gene phụ trợ trong hệ Van (VanRS–VanHAX ± VanYWZ), hỗ trợ hoàn thiện kiểu kháng vancomycin bằng cách chỉnh sửa cấu trúc tiền chất vách tế bào|
|AlrSR||ArlS – ArlR thuộc một Two-Component System (TCS) có vai trò điều hòa toàn cục (global regulation), liên quan mạnh đến virulence, biofilm, autolysis và stress response, đặc biệt ở Staphylococcus aureus và các Gram-positive liên quan|
|KinABCDE, KapB, Spo0F, Spo0B, Spo0A|Thuộc hệ thống Spo0 phosphorelay, một hệ điều hòa tín hiệu nhiều bước đóng vai trò kích hoạt sporulation và điều phối các trạng thái sinh lý thích nghi|
|DctBSRP||Hệ thống Two-Component System (TCS) điều hòa vận chuyển và chuyển hóa C4-dicarboxylate|
|MalKRAN||Hệ thống vận chuyển và điều hòa Maltose / Maltodextrin (Mal system)|
|LytSR–LrgAB||Điều hòa autolysis, cân bằng sống–chết tế bào, stress thành tế bào và biofilm|
|NatKRAB||NatK–NatR–NatAB thuộc hệ Two-component system Nat, điều hòa cảm nhận Na⁺ và cân bằng ion thông qua hệ vận chuyển NatAB, giúp vi khuẩn thích nghi với stress thẩm thấu và môi trường mặn|
|NarGHIJ||Hệ thống Nitrate respiration (Nitrate reductase I system)|
|ComXPA||Hệ quorum sensing peptide-based kết hợp Two-component system (ComXPA), điều hòa competence và hành vi quần thể phụ thuộc mật độ tế bào ở vi khuẩn Gram-positive|
|DegSU||Hệ điều hòa toàn cục kiểm soát motility, enzyme ngoại bào, biofilm và competence, đóng vai trò trung tâm trong thích nghi môi trường ở vi khuẩn Gram-positive|
|DesKR||Cảm nhận nhiệt độ / độ cứng màng và điều hòa thích nghi lạnh (cold adaptation)|
|LiaSRIHGF||Cảm nhận và đáp ứng stress màng tế bào / thành tế bào, đặc biệt do kháng sinh tác động|
|NarGHIJ||Hệ thống Nitrate respiration – Nitrate reductase I (Nar system)|
|YdfHIJ||Operon liên quan đến cell envelope stress / antibiotic stress response|
|MCP, CheD, CheR, CheB, CheA, CheW, CheV, CheC, CheY, FliG, FliM, FliN, MotA, MotB||Hệ thống Chemotaxis (hóa hướng động) của vi khuẩn: cảm nhận môi trường và điều khiển chuyển động của vi khuẩn (bơi, đổi hướng) để tiến tới chất hấp dẫn hoặc tránh chất độc|
