""""""  		  	   		  	  		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  	  		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  	  		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  	  		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  	  		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  		  		  		    	 		 		   		 		  
or edited.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  	  		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  	  		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  	  		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  	  		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  	  		  		  		    	 		 		   		 		  
"""  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def author():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    return "ylei75"  # replace tb34 with your Georgia Tech username.
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def gtid():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    return 903756141  # replace with your GT ID number
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  	  		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    result = False  		  	   		  	  		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  	  		  		  		    	 		 		   		 		  
        result = True  		  	   		  	  		  		  		    	 		 		   		 		  
    return result  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def test_code():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    win_prob = 9/19  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		  	  		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  	  		  		  		    	 		 		   		 		  
    # add your code here to implement the experiments

    # dataframeGenerator(simulator(win_prob=win_prob,num_episodes=1))
    plotting(simulator(win_prob=win_prob,num_episodes=1))


def simulator(win_prob,num_episodes):
    results = np.full((num_episodes,1001),80)
    print(results)
    episode = 1
    episode_winnings = 0
    spin = 0
    bet_amount = 1
    won = False
    while episode <= num_episodes:
        while (not won and spin < 1000):
            won = get_spin_result(win_prob)
            if won==True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            spin +=1
            results[episode-1,spin] = episode_winnings
        episode +=1
    print(results)

    return results

def dataframeGenerator(results):
    df = pd.DataFrame(results)
    column_names = ['spin'+ str(i) for i in range(1001)]
    df.columns = column_names
    print(df)
    df.plot()
    plt.show()

def plotting(results):
    print(results[1,:])
    plt.plot(results[1,:])
    # plt.scatter(results)
    # plt.show()



if __name__ == "__main__":  		  	   		  	  		  		  		    	 		 		   		 		  
    test_code()  		  	   		  	  		  		  		    	 		 		   		 		  
