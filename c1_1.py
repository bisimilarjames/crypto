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
        # Loops through each decimal of the hex number and converts it to a 4 bit binary
        for i in hex:
            #adds it to the string of 4 bit binary
            binary_string += self.hex_digit_to_4bit(i)

        #If there is two hexs short of a 24 bit number
        if numbyte%3 == 1 :
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
        #Sum variable
        sum = 0


        #####Computations#####
        #Converts the 6 bit binary number into a decimal number
        for i in range(6):
            if i == 0:
                sum += int(binary[i]) * 32
            elif i == 1:
                sum += int(binary[i]) * 16
            elif i == 2:
                sum += int(binary[i]) * 8
            elif i == 3:
                sum += int(binary[i]) * 4
            elif i == 4:
                sum += int(binary[i]) * 2
            elif i == 5:
                sum += int(binary[i]) * 1

        #Returns the base64 character
        return b64_index_table[sum]
