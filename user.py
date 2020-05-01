from mbti_keys import Category
from table import DeStress 


#mbti controller
e_list = []

e_list = Category().results()

class UserMBTI():

    def personality_type(self):
        Category().option1()
        Category().option2()
        Category().option3()
        Category().option4()
        print("\nYour Personality type is: ")
        print(e_list)
        return e_list
      
    #extroverts
    def e_types(self):
        #judging
        if e_list == ['E', 'N', 'F', 'J']:
            print("As an ENFJ, here are three ways to relieve stress:\n")
            DeStress().ds_enfj()
        elif e_list == ['E', 'S', 'F', 'J']:
            print("As an ESFJ, here are three ways to relieve stress:\n")
            DeStress().ds_esfj()
        elif e_list == ['E', 'N', 'T', 'J']:
            print("As an ENTJ, here are three ways to relieve stress:\n")
            DeStress().ds_entj()
        elif e_list == ['E', 'S', 'T', 'J']:
            print("As an ESTJ, here are three ways to relieve stress:\n")
            DeStress().ds_estj()
        #perception
        elif e_list == ['E', 'N', 'F', 'P']:
            print("As an ENFP, here are three ways to relieve stress:\n")
            DeStress().ds_enfp()
        elif e_list == ['E', 'S', 'F', 'P']:
            print("As an ESFP, here are three ways to relieve stress:\n")
            DeStress().ds_esfp()
        elif e_list == ['E', 'N', 'T', 'P']:
            print("As an ENTP, here are three ways to relieve stress:\n")
            DeStress().ds_entp()
        elif e_list == ['E', 'S', 'T', 'P']:
            print("As an ESTP, here are three ways to relieve stress:\n")
            DeStress().ds_estp()

        else:
            return 0
    #intoverts
    def i_types(self):
        #judging
        if e_list == ['I', 'N', 'F', 'J']:
            print("As an INFJ, here are three ways to relieve stress:\n")
            DeStress().ds_infj()
        elif e_list == ['I', 'S', 'F', 'J']:
            print("As an ISFJ, here are three ways to relieve stress:\n")
            DeStress().ds_isfj()
        elif e_list == ['I', 'N', 'T', 'J']:
            print("As an INTJ, here are three ways to relieve stress:\n")
            DeStress().ds_intj()
        elif e_list == ['I', 'S', 'T', 'J']:
            print("As an ISTJ, here are three ways to relieve stress:\n")
            DeStress().ds_istj()
        #perception
        elif e_list == ['I', 'N', 'F', 'P']:
            print("As an INFP, here are three ways to relieve stress:\n")
            DeStress().ds_infp()
        elif e_list == ['I', 'S', 'F', 'P']:
            print("As an ISFP, here are three ways to relieve stress:\n")
            DeStress().ds_infp()
        elif e_list == ['I', 'N', 'T', 'P']:
            print("As an INTP, here are three ways to relieve stress:\n")
            DeStress().ds_intp()
        elif e_list == ['I', 'S', 'T', 'P']:
            print("As an ISTP, here are three ways to relieve stress:\n")
            DeStress().ds_istp()

        else:
            return 0
        
