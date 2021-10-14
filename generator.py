#############################
# Generating the data files #
# for eternal sort.         #
#############################
# STRUCTURE                 #
# --------------------------#
# CustomerID: int(8)        #
# Name:       char(25)      #
# SIN:        int(9)        #
# Address:    char(58)      # 
#############################
import string
import random

REPEATED_CUSTOMER_IDS = ["",]

def generateString(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def generateCustomerId(id_root: int):
    return str(id_root).zfill(8)
    # return generateRandomName()

def generateRandomName():
    return generateString(25, string.ascii_lowercase + string.ascii_uppercase)

def generateSin():
    return generateString(9, string.digits)

def generateAddress():
    return generateString(58, string.ascii_lowercase + string.ascii_uppercase + string.punctuation)


def main():
    INITIAL_CUSTOMER_ID = 10000000

    '''
    Change the file name and the upper limit in range()
    '''
    fileSmall = open("file1000000.txt", "w")
    for i in range(1, 1000000):
        id = generateCustomerId(INITIAL_CUSTOMER_ID)
        name = generateRandomName()
        sin = generateSin()
        address = generateAddress()
        if i % 1000 == 0:
            print(F"Sample data: {id}, {name}, {sin}, {address}")
        currentRow = [id, name, sin, address,"\n"]
        
        fileSmall.writelines(currentRow)
        
        INITIAL_CUSTOMER_ID = INITIAL_CUSTOMER_ID - 1
    
    fileSmall.close()




if __name__ == "__main__":
    main()