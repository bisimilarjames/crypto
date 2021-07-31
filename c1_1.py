import base64

class Crypt1:


    def hexfaroundandfindout(self,hex):
        """
        Converts a hexadecimal input to base 64 encoding

        data input: A string representing the hex input
        data output: A string representing the base64 encoding
        """
        #####Declerations#####
        ####Lists####
        binary_holder = []
        six_bit_holder = []

        ####Variables####
        binary_string = ''
        padding_holder = ''
        numbyte = len(hex)/2

        #####Computations#####

        for i in hex:
            binary_string += self.hex_digit_to_4bit(i)

        print(binary_string)

        if numbyte%3 == 1 :
            print('a')
            self.bin_to_hex(six_bit_holder,binary_string, 4 * int(numbyte//3))
            padding_holder = binary_string[-8:] + '0000'
            self.bin_to_hex(six_bit_holder,padding_holder, 2)
            for i in six_bit_holder:
                print(binascii.b2a_uu(i))

        elif numbyte%3 == 2:
            print('b')
            self.bin_to_hex(six_bit_holder,binary_string, 4 * int(numbyte//3))
            padding_holder = binary_string[-16:] + '00'
            self.bin_to_hex(six_bit_holder,padding_holder, 3)
        else:
            self.bin_to_hex(six_bit_holder,binary_string, 4 * int(numbyte/3))

        print(six_bit_holder)

    def hex_digit_to_4bit(self,digit):
        """
        Converts a digit of hexadecimal to 4 bit binary

        data input: A char of the hex input
        data output: A 4 bit binary
        """
        #####Declerations#####
        ####Lists####
        binary_holder = []
        hex_holder = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

        ####Variables####
        dec = 0
        strh = ''

        #####Computations#####
        if digit.isnumeric() == True:
            dec = int(hex_holder.index(digit))

        else:
            dec = int(hex_holder.index(digit.lower()))


        while dec >= 1:
            if dec % 2 > 0:
                binary_holder.append('1')
            elif dec % 2 == 0:
                binary_holder.append('0')

            dec = dec // 2


        if len(binary_holder) < 4:
            while len(binary_holder) < 4:
                binary_holder.append('0')

        binary_holder.reverse()

        for i in binary_holder:
            strh += i

        return strh

    def bin_to_hex(self,stor,str,itr):
        """


        data input:
        data output:
        """
        #####Declerations#####


        #####Computations#####
        for i in range(itr):

            stor.append(str[0 + 6 * i: 6 + 6 * i])

        return stor
