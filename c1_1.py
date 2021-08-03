class Crypt1:


    def hex_to_base64(self,hex):
        """
        Converts a hexadecimal input to base 64 encoding

        data input: A string representing the hex input
        data output: A string representing the base64 encoding
        """
        #####Declerations#####
        ####Variables####
        #Holds the 8bit binary
        binary_string = ''
        #If the number of hex's not divisble into 25 bits, this holds the remainder hex's
        padding_holder = ''
        #Holds the base64 encoding
        base_holder = ''
        #Holds the number of hexadecimal numbers submitted
        numbyte = len(hex)/2


        #####Computations#####
        #Valid input checker
        self.hex_checker(hex)

        # Loops through each decimal of the hex number and converts it to a 4 bit binary
        for i in hex:
            #adds it to the string of 4 bit binary
            binary_string += self.hex_digit_to_4bit(i)

        #If there is two hexs short of a 24 bit number
        if numbyte%3 == 1 :
            print('a')
            #Convert all the 24bit binary chunks into base64
            base_holder = self.bin_to_base(base_holder,binary_string, 4 * int(numbyte//3))
            #Adds the padding to the remainder
            padding_holder = binary_string[-8:] + '0000'
            #Converts the modified remainder into base64
            base_holder += self.bin_to_base(base_holder,padding_holder, 2)
            #Adds the padding indicator
            base_holder += '=='

        #If there is one hex short of a 24 bit number
        elif numbyte%3 == 2:
            base_holder = self.bin_to_base(base_holder,binary_string, 4 * int(numbyte//3))
            padding_holder = binary_string[-16:] + '00'
            base_holder += self.bin_to_base(base_holder,padding_holder, 3)
            base_holder += '='

        #If no padding is required
        else:
            base_holder = self.bin_to_base(base_holder,binary_string, 4 * int(numbyte/3))

        return base_holder

    def hex_digit_to_4bit(self,digit):
        """
        Converts a digit of hexadecimal to 4 bit binary

        data input: A char of the hex input
        data output: A 4 bit binary
        """
        #####Declerations#####
        ####Lists####
        #Holds the binary number
        binary_holder = []
        #Holds the hex alphabet
        hex_holder = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

        ####Variables####
        #Holds the decimal number
        dec = 0
        #Holds the string of the 4 bit binary that will be returned
        strh = ''

        #####Computations#####
        #If the hex sumbitted is between 0-9
        if digit.isnumeric() == True:
            dec = int(hex_holder.index(digit))
        #If it is a-f
        else:
            dec = int(hex_holder.index(digit.lower()))

        #Binary conversion algorithm
        while dec >= 1:
            #If there remainder of the number submitted divided by 2 add a one to the binary arrray
            if dec % 2 > 0:
                binary_holder.append('1')
            #Else add zero
            elif dec % 2 == 0:
                binary_holder.append('0')

            #Floor divide the number by 2
            dec = dec // 2

        #If the binary versiuon of the hex is less than 4 bits the loop adds the remainder 0 bits
        if len(binary_holder) < 4:
            while len(binary_holder) < 4:
                binary_holder.append('0')

        #Reverse the order of the binary number
        binary_holder.reverse()

        #Converts the binary holder array into a string
        for i in binary_holder:
            strh += i

        return strh

    def bin_to_base(self,bass,str,itr):
        """
        Creates a base64 encoding of a binary stream

        data input: number of 6 bit segments in the binary (int)
                    the binary string (str)
        data output:The base64 string (str)
        """
        #####Declerations#####


        #####Computations#####
        for i in range(itr):
            bass += self.bitbin_to_ascii(str[0 + 6 * i: 6 + 6 * i])

        return bass

    def bitbin_to_ascii(self,binary):
        """
        Converts a single 6 bit binary chunk into a base64 encoded character

        data input: 6 bit binary chunk (str)
        data output: base64 encoded character (char)
        """
        #####Declerations#####
        ####Variables####
        #Base64 alphabet in a string
        b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


        #####Computations#####
        #Converts the 6 bit binary number into a decimal number
        self.n_bit_binary_decoder(binary,6)

        #for i in range(6):
        #    if i == 0:
        #        sum += int(binary[i]) * 32
        #    elif i == 1:
        #        sum += int(binary[i]) * 16
        #    elif i == 2:
        #        sum += int(binary[i]) * 8
        #    elif i == 3:
        #        sum += int(binary[i]) * 4
        #    elif i == 4:
        #        sum += int(binary[i]) * 2
        #    elif i == 5:
        #        sum += int(binary[i]) * 1

        #Returns the base64 character
        return b64_index_table[self.n_bit_binary_decoder(binary,6)]

    def hex_checker(self,hex):
        """
        Checks the hex string is correct

        data input: A hex string (str)
        data output: n/a
        """
        #####Declerations#####
        alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']

        #####Computations#####
        # Checks that it is even number of charaters becaseu a hex number is 2 things long
        if len(hex) % 2 != 0:
            print('Invalid hex input. It needs to be an even number of characters.')
            quit()

        for i in range(len(hex)):
            if hex[i] not in alphabet:
                print('Character {} is an invalid hex character'.format(i + 1))
                quit()

    def fixed_xor(self,mess,key):
        """
        Xor to equal length hex strings together

        data input: two hex strings (str) of eqaul length
        data output: A hex string (str)
        """
        #####Declerations#####
        ####Variables####
        mess_bin = ''
        key_bin = ''
        xor_bin = ''
        xor_hex = ''

        ####list###
        #Holds the hex alphabet
        hex_holder = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']


        #####Computations#####
        #Checks the hex string are equal length
        if len(mess) != len(key):
            print('The hex strings must be of equal length')
            quit()

        #Checks the hex's are valid
        self.hex_checker(mess)
        self.hex_checker(key)

        #Converts the hex strings into binary numbers
        # Loops through each decimal of the hex number and converts it to a 4 bit binary
        for i in mess:
            #adds it to the string of 4 bit binary
            mess_bin += self.hex_digit_to_4bit(i)

        for i in key:
            key_bin += self.hex_digit_to_4bit(i)


        xor_bin = self.xor(mess_bin,key_bin)

        print(xor_bin)
        for i in range(int(len(mess)/2)):
            print(xor_bin[0 + 4 * i: 4 +  4 * i])
            xor_hex += hex_holder[self.n_bit_binary_decoder(xor_bin[0 + 4 * i: 4 +  4 * i],4)]

    def xor(self,m,k):
        """
        Xor to equal length hex strings together

        data input: two binary numvers (str) of eqaul length
        data output: A binary number (str)
        """
        #####Declerations#####
        ####Variables####
        #Holds the xor binary
        x = ''
        #####Computations#####
        for i in range(len(m)):
            if m[i] == '1' and k[i] == '1':
                x += '0'
            elif m[i] == '0' and k[i] == '0':
                x += '0'
            else:
                x += '1'

        return x

    def n_bit_binary_decoder(self,bin,n):
        """
        Decodes an nbit binary string into base 10

        data input: two binary numvers (str) of eqaul length
        data output: A base 10 number (int)
        """
        #####Declerations#####
        ####Variables####
        #Calculates the max binary value
        max_bin = 2 ** (n-1)
        # Holds the base 10 sum of the binary number
        sum = 0

        #####Computations#####
        #loops through each bit of the binary number
        #Starts at the big end
        for i in range(n):
            #Adds the current maximum times either 0 or 1 to the base 10 sum
            sum += int(bin[i]) * max_bin

        print(int(sum))
        return int(sum)
