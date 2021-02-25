def productFib(prod):
    last  , previous = 1,0
    '''we create variable and put 1 and zero into them'''
    while last*previous<prod :
        '''in here we create loop until last * pervious is less than product'''
        last , previous = last+previous , last
        '''until the loop s done we collect last and pervoius and pass last into prevois (this is the formule of the fiv numbers) '''
    return [previous , last , last*previous == prod] 

