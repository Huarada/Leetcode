import math

class Solution:
    def intToRoman(self, num: int) -> str:
        alg = []
        rom = []
        removed = 0
        resto = 0
        num_temp = num
        #colocar o numero em um alista, para definir direito cada algarismo
        while(num_temp > 10):
            resto = num_temp % 10
            alg.append(resto)
            num_temp = math.floor(num_temp/10)
        alg.append(num_temp)
        alg.reverse()

        if (len(alg) == 4):
            removed = alg.pop(0)
            #completar algarismo da milhar
            for i in range(removed):
                rom.append('M')
            
        if(len(alg) >= 3):
            #completar algarismo centenas
            removed = alg.pop(0)
            if(removed == 9):
                rom.append("CM")
            elif(removed >= 5):
                rom.append('D')
                for i in range(removed - 5):
                    rom.append('C')

            elif(removed == 4):
                rom.append("CD")
            else:
                for i in range(removed):
                    rom.append('C')

        if(len(alg) >= 2):
            removed = alg.pop(0)
            #completar algarismo dezenas

            if(removed == 9):
                rom.append("XC")
            elif(removed >= 5):
                rom.append('L')
                for i in range(removed - 5):
                    rom.append('X')

            elif(removed == 4):
                rom.append("XL")
            else:
                for i in range(removed):
                    rom.append('X')


        #completar algarismo unidades
        removed = alg.pop(0)
        if(removed == 9):
            rom.append("IX")
        elif(removed >= 5):
            rom.append('V')
            for i in range(removed - 5):
                rom.append('I')

        elif(removed == 4):
            rom.append("IV")
        else:
            for i in range(removed):
                rom.append('I')

        rom = "".join(rom)
        rom = rom.replace("DCCCCC", "M")
        rom = rom.replace("LXXXXX", "C" )
        rom = rom.replace("VIIIII", "X" )
        return rom