"""
This is a 'fixture' that stores orbit schemata
"""



# K: 2, L: 8, M: 18, N: 32, O: 50, P: 72

                       # x  y  z
SCHEMATA = {'atomic': [(-5, 0, 0),         # Shell 1: 2 electrons | 1st
                       (5, 0, 0),          #                      | 2nd

                       (0, 0, 7),          # Shell 2: 8 electrons | 3rd
                       (0, 0, -7),         #                      | 4th
                       (5.25, 0, 1.75),    #                      | 5th
                       (-5.25, 0, -1.75),  #                      | 6th
                       (3.5, 0, 3.5),      #                      | 7th
                       (-3.5, 0, -3.5),    #                      | 8th
                       (7, 0, 0),          #                      | 9th
                       (-7, 0, 0)],        #                      | 10th

           'planetary': [(-5, 0, 0),       # Mercury
                         (-7, 0, 0),       # Venus
                         (-9, 0, 0),       # Earth
                         (-11, 0, 0),      # Mars
                         (-13, 0, 0),      # Jupiter
                         (-15, 0, 0),      # Saturn
                         (-17, 0, 0),      # Uranus
                         (-19, 0, 0),      # Neptune
                         (-21, 0, 0),      # IX
                         (-23, 0, 0)]}     # X




