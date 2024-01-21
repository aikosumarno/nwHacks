from Organization_registration import OrganizationRegistration
from Company_registration import CompanyRegistration
import Match_algorithm



def main():
    org_reg = OrganizationRegistration()
    org_reg.finish_registration()

    comp_reg = CompanyRegistration()
    comp_reg.finish_registration()

    org_data = org_reg.get_org_data()
    comp_data = comp_reg.get_comp_data()


#the tk stuff
    # root_org = Tk()
    # root_org.title("Organization Registration")
    # org = ApplicationOrg(root_org)

    # root_org.mainloop()

    # root_comp = Tk()
    # root_comp.title("Company Registration")
    # comp = ApplicationComp(root_comp)


    # root_comp.mainloop() 


    mission_sim = Match_algorithm.key_word_similarity(org_data["mission"], comp_data["mission"])
    val_sim = Match_algorithm.key_word_similarity(org_data["keyword"], comp_data["keyword"])
    print("Mission similarity: " + str(mission_sim))
    print("Values similarity: " + str(val_sim))
    print("your match is " +  (str((mission_sim + val_sim)/2.0)))

if __name__ == "__main__":
    main()