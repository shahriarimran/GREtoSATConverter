x = input('Convert SAT to GRE?:')
y = input('Convert entire test or section-wise?:')

if x == 'y' and y =='y':
    SAT = int(input('SAT Score:'))
    if SAT<800 or SAT>1600:
        print('invalid')
    else:
      GRE = int((SAT-800)/10 + 260)
      GREP = int((GRE-260)/0.8)
      myGRE = ("Your expected GRE score is {0}")
      myGREP = ("Your score is within the {0}th percentile")
      print(myGRE.format(GRE))
      print(myGREP.format(GREP))
elif x == 'y':
    SATM = int(input('SAT Math Score:'))
    SATR = int(input('SAT Reading Score:'))
    if SATM<400 or SATM>800 or SATR<400 or SATR>800:
        print('invalid')
    else:
        SAT = SATM + SATR
        GREM = int((SATM-400)/10 + 130) 
        GRER = int((SATR-400)/10 + 130) 
        GRE = GREM + GRER
        mySAT = ("Your SAT score is {}")
        myGREM = ("Your expected GRE Math score is {}")
        myGRER = ("Your expected GRE Reading score is {}")
        myGRE = ("Your expected GRE score is {0}")
        print(mySAT.format(SAT))
        print(myGREM.format(GREM))
        print(myGRER.format(GRER))
        print(myGRE.format(GRE))
elif y == 'y':
    GRE = int(input('GRE Score:'))
    if GRE < 260 or GRE > 340:
        print('invalid')
    else: 
        SAT = int((GRE - 260)*10 + 800)
        mySAT = ("Your SAT would have been similar to {0}")
        print(mySAT.format(SAT))
else:
    GREM = int(input('GRE Math Score:'))
    GRER = int(input('GRE Reading Score:'))
    if GREM<130 or GREM>170 or GRER<130 or GRER>170:
        print('invalid')
    else:
        SATM = int((GREM-130)*10 + 400) 
        SATR = int((GRER-130)*10 + 400) 
        SAT = SATM + SATR
        mySATM = ("Your expected SAT Math score is {}")
        mySATR = ("Your expected SAT Reading score is {}")
        mySAT = ("Your SAT would have been similar to {}")
        print(mySATM.format(SATM))
        print(mySATR.format(SATR))
        print(mySAT.format(SAT))
