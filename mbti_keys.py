from table import KeyTypes
#This is a class where it will present MBTI keys and the user will pick one per category
# E / I 
# N / S
# F / T
# J / P
mbti_type = [] #an empty list with four characters
#present a table of keys per option 
class Category(KeyTypes):
    #E or I 
    def option1(self):
        while len(mbti_type) != 4:
            #call the function to present table1
            KeyTypes().keychart1()
            choice1 = str(input("E or I: "))
            
            if (choice1 == 'E') or (choice1 == 'I'):
                mbti_type.append(choice1)
                return choice1
            
            else:
                print("try again")
                self.mbti_type = []
                self.option1()
                break
        
    def option2(self):
        while len(mbti_type) != 4:
            #call function to display table2
            KeyTypes().keychart2()
            choice2 = str(input("N or S: "))

            if (choice2 == 'N') or (choice2 == 'S'):
                mbti_type.append(choice2)
                return choice2

            else:
                print("try again")
                self.mbti_type = []
                self.option2()
                break

    def option3(self):
        while len(mbti_type) != 4:
            #call function to display table3
            KeyTypes().keychart3()
            choice3 = str(input("F or T: "))

            if (choice3 == 'F') or (choice3 == 'T'):
                mbti_type.append(choice3)
                return choice3

            else:
                print("try again")
                self.mbti_type = []
                self.option3()
                break

    def option4(self):
        while len(mbti_type) != 4:
            #call function to display table4
            KeyTypes().keychart4()
            choice4 = str(input("J or P: "))

            if (choice4 == 'J') or (choice4 == 'P'):
                mbti_type.append(choice4)
                return choice4

            else:
                print("try again")
                self.mbti_type = []
                self.option4()
                break    

    def results(self):
        return mbti_type