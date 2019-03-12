#The Apocalypse: In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate.
#Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines.
#If all families abide by this policy—that is, they have continue to have children until they have one girl,
#at which point they immediately stop—what will the gender ratio of the new generation be?
#(Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.)
import random
class family():
    def __init__(self):
        self.childeren = []

    def have_childeren(self):

        while('G' not in self.childeren):
            chance = random.randint(0,2) #the output can be 1 or 2 so 50 percent chance
            if(chance == 2):
                self.childeren.append('G')
            else:
                self.childeren.append('B')



class birth_rate_numberof_families():
    def __init__(self):
        self.all_childeren = []

    def create_families_with_childeren(self,num):
        ctr= 0
        while(ctr<num):
            a = family()
            a.have_childeren()
            for i in range(len(a.childeren)):
                self.all_childeren.append(a.childeren[i])
            ctr +=1

        girls = self.all_childeren.count('G')
        boys = self.all_childeren.count('B')
        return girls/(girls+boys)


def main():
    br = birth_rate_numberof_families()
    print(br.create_families_with_childeren(5))
if __name__ == '__main__':
    main()
