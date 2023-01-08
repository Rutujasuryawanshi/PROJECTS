# first we will take input of what nominee what we want to keep 

nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2nd nominee: ")

# initally vote count for both must be 0

num1_votes = 0
num2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

n0_of_voter = len(voter_id)

while True:

    if voter_id == []:
        print("Voting session is over !!!")
        if num1_votes > num2_votes:
            percent = (num1_votes/no_of_voter)*10
            print(nominee1,"has won the election with ",percent,"% of votes")
            break
        elif num2_votes > num1_votes:
            percent = (num2_votes/n0_of_voter)*100
            print(nominee,"has won the election with ",percent ,"% of votes")
            break
        else:
                print("Both have equal number of votes !!!! Government will decide who will rule")
                break


        voter = int(input("Enter your voter id: "))
        if voter in voter_id:
            print("your are a voter ")
            voter_id.remove(voter)
            print("------------------------------------")
            print("To give vote to ",nominee1,"Press 1 ")
            print("To give vote to ",nominee2,"Press 2 ")
            print("------------------------------------")
            vote = int(input("Enter your precious vote : "))
            if vote == 1:
                num1_votes +=1
                print(nominee1,"Thanks you to give your important vote for them")
            elif vote == 2:
                num2_votes +=1
                print(nominee2,"Thanks you to give your important vote for them")
            elif vote > 2:
                print("Check your pressed key !!")
            else:
                print("You are not a voter OR You have already voted")
                break
            
