__author__ = 'MihaZiK'

import random


class MyLion:

    def __init__(self, state):
        self.state = state

    def meet(self, obj):
        if ((obj == 'Antilopa') and (self.state == 'Sit')):
            print("Antilopa")
            print("Lion sleep")
            self.state = 'Goloden'
        else:
            if((obj == 'Antilopa') and (self.state == 'Goloden')):
                print("Antilopa")
                print("Lion eat Antilopa")
                self.state = 'Sit'
            else:
                if ((obj == 'Hunter') and (self.state == 'Sit')):
                    print("Hunter")
                    print("Lion run and Goloden")
                    self.state = 'Goloden'
                else:
                    if (obj == 'Hunter' and self.state == 'Goloden' ):
                        print("Hunter")
                        print("Lion run")
                    else:
                        if ((obj == 'Tree') and (self.state == 'Sit')):
                            print("Tree")
                            print("Lion look")
                            self.state = 'Goloden'
                        else:
                            print("Tree")
                            print("Lion sleep under the tree")
