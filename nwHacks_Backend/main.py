from Organization_registration import Organization
from Company_registration import Company
import Match_algorithm
import time

def registration():
    match_cutoff = 50
    org = Organization()
    org.finish_registration()

    print("\n")

    comp = Company()
    comp.finish_registration()

    mission_sim = Match_algorithm.mission_similarity(org.mission, comp.mission) * 100
    val_sim = Match_algorithm.key_word_similarity(org.keyword, comp.keyword)
    goal_sim = Match_algorithm.goals_similarity(org.all_goals, comp.all_goals)
    match_score = (((mission_sim + val_sim)*2) + goal_sim)/5.0

    print("Mission similarity: " + str(mission_sim))
    print("Values similarity: " + str(val_sim))
    print("Goals_similarity: " + str(goal_sim))
    print("Your match score is " +  str(match_score) + "\n")
    print("\n Matching... \n \n")
    time.sleep(3)
    
    if(match_score > 50):
        print("Congratulations 🥳 You matched!! (profile will appear in dashboard)")
        comp.matched_list.update({org.name:match_score})
        org.matched_list.update({comp.name:match_score})
    else:
        print("Not a match... try again?")

#; request function
# def request(org, name, dscr, keywords):

#     attr = org.matched_list
#     def quicksort(arr, attr):
#         if len(arr) <= 1:
#             return arr
#         pivot = getattr(arr[len(arr) // 2], attr)
#         left = [x for x in arr if getattr(x,attr) > pivot]
#         middle = [x for x in arr if getattr(x,attr) == pivot]
#         right = [x for x in arr if getattr(x,attr) < pivot]
#         return request(left, attr) + middle + request(right, attr)
        
def main():
    registration()

if __name__ == "__main__":
    main()


