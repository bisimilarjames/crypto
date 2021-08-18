class Crypt1:

    #Challenge 1
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
        data output: A 4 bit binary (str)
        """
        #####Declerations#####
        ####Lists####
        #Holds the hex alphabet
        hex_holder = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

        ####Variables####
        #Holds the decimal number
        dec = 0
        #Holds the string of the 4 bit binary that will be returned

        #####Computations#####
        #If the hex sumbitted is between 0-9
        if digit.isnumeric() == True:
            dec = int(hex_holder.index(digit))
        #If it is a-f
        else:
            dec = int(hex_holder.index(digit.lower()))

        #Returns a four bit binary string
        return self.base10_to_binary(dec, 4)

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

        # Xors the two binary strings
        xor_bin = self.xor(mess_bin,key_bin)

        #Loops through each 4 bits in the xor binary string and converts it back to hex
        for i in range(int(len(mess))):
            # The binary decoder produces the index in the hex list for the appropriate hex value
            # This is added to the hex string
            xor_hex += hex_holder[self.n_bit_binary_decoder(xor_bin[0 + 4 * i: 4 +  4 * i],4)]

        return xor_hex

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
        #Loops through each bit in the message and key binary strings
        for i in range(len(m)):
            #This is the xor truth table
            if m[i] == '1' and k[i] == '1':
                x += '0'
            elif m[i] == '0' and k[i] == '0':
                x += '0'
            elif m[i] == '1' and k[i] == '0':
                x += '1'
            elif m[i] == '0' and k[i] == '1':
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
            max_bin /= 2

        return int(sum)

    #Challenge 3
    def single_byte_xor(self, mess):
        """
        Finds the byte key for a single

        data input: Takes in a hex string (str)
        data output:
        """
        #####Declerations#####
        ####Lists####
        mess_hol = ''
        decrypt_bin =''

        decimal_hol = []

        ####Variables####
        #Frequency anlaysis english
        freq_dict = 'etaoinshrdlcumwfgypbvkjxqz'
        #Holds the potential binary key
        key = ''
        #Holds the length of the message
        encrypt_len = int(len(mess))


        #####Computations#####
        self.hex_checker(mess)

        for i in mess:
            mess_hol += self.hex_digit_to_4bit(i)

        for i in range(0,2) :
            key = self.base10_to_binary(i,8)
            for j in range(encrypt_len):
                if j % 2 == 0:
                    decrypt_bin += self.xor(mess_hol[0 + 4 * j: 4 +  4 * j], key[0:4])
                elif j % 2 == 1:
                    decrypt_bin += self.xor(mess_hol[0 + 4 * j: 4 +  4 * j], key[4:8])


            for j in range(encrypt_len//2):

                decimal_hol.append(self.n_bit_binary_decoder(decrypt_bin[0 + 8 * j: 8 +  8 * j],8))



    def base10_to_binary(self, decimal, bits):
        """
        Decodes an nbit binary string into base 10

        data input: Takes in a positive integer less than 256 (int)
        data output: A binary string of the required number of bits (str)
        """
        #####Declerations#####
        ####Lists####
        #Holds the binary number
        binary_holder = []

        ####Variables####
        strh = ''

        #####Computations#####
        #Binary conversion algorithm
        while decimal >= 1:
            #If there remainder of the number submitted divided by 2 add a one to the binary arrray
            if decimal % 2 > 0:
                binary_holder.append('1')
            #Else add zero
            elif decimal % 2 == 0:
                binary_holder.append('0')

            #Floor divide the number by 2
            decimal = decimal // 2

        #If the binary version of the hex is less than 4 bits the loop adds the remainder 0 bits
        if len(binary_holder) < bits:
            while len(binary_holder) < bits:
                binary_holder.append('0')

        #Reverse the order of the binary number
        binary_holder.reverse()

        #Converts the binary holder array into a string
        for i in binary_holder:
            strh += i

        return strh
