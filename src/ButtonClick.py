from FormatNumber import *
class ButtonClick:
    def checkNegative(ui, isNegative, numberInput):
            if isNegative:
                    isNegative, numberInput = ButtonClick.negativeClicked(ui, isNegative, numberInput)
                    isNegative = False
            return isNegative, numberInput
    def numberClicked(ui, numberInput, isNegative, number):
            numberInput = str(numberInput) + number
            isNegative, numberInput = ButtonClick.checkNegative(ui, isNegative, numberInput)
            numberInput = FormatNumber.deleteFirstZero(numberInput)
            numberInput = FormatNumber.displayNumber(ui, numberInput, False)
            return numberInput, isNegative
    def negativeClicked(ui, isNegative, numberInput):
            isNegative = not isNegative
            if numberInput == '' or numberInput == '0':
                return numberInput
            numberInput = -FormatNumber.convertToNumber(numberInput)
            isNegative = not isNegative
            numberInput = FormatNumber.displayNumber(ui, numberInput, False)
            return isNegative, numberInput
    def acButtonClicked(ui, numberInput, result, calculation, isNegative):
        numberInput = str(numberInput)[:-1]
        if numberInput == '':
                numberInput = '0'
                result = 0
                calculation = 0
                isNegative = False
                ui.addition.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
                ui.subtraction.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
                ui.multiplication.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
                ui.division.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
        ui.label.setText(str(numberInput))
        print (numberInput)
        return numberInput, result, calculation, isNegative
        
