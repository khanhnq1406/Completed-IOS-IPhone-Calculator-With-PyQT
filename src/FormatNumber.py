MAX_LEN = 9
class FormatNumber:
        @staticmethod
        def convertToNumber(number):
                        if str(number).find('.') == -1:
                                return int(number)
                        else:
                                return float(number)
        @staticmethod
        def deleteFirstZero(numberInput):
                print ('Number input 1: ', numberInput)
                if str(numberInput).find('.') == -1:
                        for runner in str(numberInput):
                                if runner == '0' and len(str(numberInput)) > 1:
                                        numberInput = str(numberInput)[1:]
                                elif runner == '0' and len(str(numberInput)) <= 1: 
                                        return numberInput
                                else: break
                print ('Number input 2: ', numberInput)
                return numberInput
        @staticmethod
        def displayNumber(ui, numberInput, hasRound):
                if len(str(numberInput)) > MAX_LEN:
                        if hasRound:
                                numberInput = str("%e" % numberInput)
                                while len(str(numberInput)) > 9:
                                        prevE = str(numberInput).find('e') - 1
                                        numberInput = numberInput[0 : prevE : ] + numberInput[prevE + 1 : :]
                        else:
                                numberInput = str(numberInput)[:-1]
                ui.label.setText(str(numberInput))
                print (numberInput)
                return numberInput