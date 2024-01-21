from Organization_registration import Organization
from Company_registration import Company
import Match_algorithm
import time

match_cutoff = 50

def main():
    org = Organization()
    org.finish_registration()

    comp = Company()
    comp.finish_registration()



#the tk stuff
    # root_org = Tk()
    # root_org.title("Organization Registration")
    # org = ApplicationOrg(root_org)

    # root_org.mainloop()

    # root_comp = Tk()
    # root_comp.title("Company Registration")
    # comp = ApplicationComp(root_comp)


    # root_comp.mainloop() 


    mission_sim = Match_algorithm.key_word_similarity(org.mission, comp.mission)
    val_sim = Match_algorithm.key_word_similarity(org.keyword, comp.keyword)
    match_score = ((mission_sim + val_sim)/2.0)

    print("Mission similarity: " + str(mission_sim))
    print("Values similarity: " + str(val_sim))
    print("Your match score is " +  str(match_score) + "\n")
    print("\n Matching... \n \n")
    time.sleep(3)
    
    if(match_score > 50):
        print("Congratulations 🥳 You matched!! (profile will appear in dashboard)")
    else:
        print("Not a match... try again?")



    


if __name__ == "__main__":
    main()