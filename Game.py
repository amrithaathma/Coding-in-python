import sys
import random

class Fight:
    def enter(self):
        print ("\n", "-" * 10)
        print ("There are two Monsters:")
        print ("Monster1")
        print ("Monster2")
        print (".")

        your_hit_points = 20
        monster1_hit_points = 6
        monster2_hit_points = 11
        monster1 = True
        monster2 = True


        while your_hit_points > 0 or (not monster1 and not monster2):
            print ("\n", "-" * 10)
            your_attack = random.randint(4,12)
            monster1_attack = random.randint(1,4)
            monster2_attack = random.randint(4,8)


            attack = int(raw_input("Type 1 to attack Monster1, 2 to attack Monster2 >"))

            if attack == 1:
                monster1_hit_points - your_attack
                print ("You hit monster1 for %d hit points.") % your_attack

                if monster1_hit_points <= 0 and monster1:
                    monster1 = False
                    print ("monster1 killed!")
                else:
                    pass

            elif attack == 2:
                monster2_hit_points - your_attack
                print ("You hit monster2 for %d hit points." % your_attack)

                if monster2_hit_points <= 0 and monster2:
                    monster2 = False
                    print ("monster2 killed!")
                else:
                    pass

            else:
                print ("DOES NOT COMPUTE")
                pass

            your_hit_points - monster1_attack
            print ("monster1 hit you for %d points, you have %d hit points left." % (monster1_attack, your_hit_points))

            your_hit_points - monster2_attack
            print ("monster2 hit you for %d points, you have %d hit points left." % (monster2_attack, your_hit_points))

        exit(1)

    
    