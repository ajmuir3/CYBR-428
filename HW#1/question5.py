#Create a script or program in a language of your choosing.  This program should
def valid_ip(input):
    true_ip = True
    split_ip = input.split(".")
    if len(split_ip) == 4:
        for number in split_ip:
            number = int(number)
            if number >= 0 and number<=255:
                true_ip = True
            else:
                true_ip = False
                return true_ip, split_ip
        return true_ip, split_ip
    else:
        true_ip = False
        return true_ip, split_ip
    
def convert_to_binary(input):
    return_binary = ""
    #Bin converts all decimals to binary
    for value in input:
        value = int(value)
        return_binary += f"{bin(value)} "
    return return_binary

def main():
    #Prompt the user to enter an ip address, or type quit if they are done
    ip = input("Enter your ip address (separated by periods), or type quit to end: ")
    #If the input value is “quit”, the program should terminate
    while ip != "quit":
        #Accept an IP address as an input as a single string, with periods separating each octet
        return_bool, split_ip = valid_ip(ip)
        #Should output if the address is valid or invalid
        if return_bool == True:
            binary_ip = convert_to_binary(split_ip)
            #Should output the address in binary, with no dots or periods
            print(f"{ip} in binary is: {binary_ip}")

        else:
            #If the address is invalid, tell the user why, and ask to enter a new ip address
            print(f"{ip} is an invalid ip address, as not all of the 4 octets fall within the decimal range of 0-255. Please enter a new ip address.")
        #Should repeat the process until a user types quit
        ip = input("Enter your ip address (separated by periods), or type quit to end: ")

    print("Thank you, have a nice day")

main()
#Submit a screen shot of your program running after two inputs, one with a bad ip address, and one with a good ip address
#Submit your code to scholar
