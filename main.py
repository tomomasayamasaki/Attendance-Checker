import datetime
import numpy as np


# Put your students' ID
# For example
"""
original_list = np.array([
              1004639,
              1004655
])
"""
# Dead time to provide score
compare_time = datetime.time(17, 20) # it means Students can get their attendance points until 17:20 
original_list = np.array([
              
])



result_list = np.zeros(len(original_list))


count = 1
while True:
    user_input = input("[No."+str(count)+"] Student ID: ")
    if user_input == "Yamasaki":
        save_time = datetime.datetime.now()
        np.savetxt('final_attend'+'.csv', result_list, delimiter=',')
        print(result_list)
        break
    
    
    save_time = datetime.datetime.now()
    np.savetxt('./backup/attend_'+str(save_time)+'.csv', result_list, delimiter=',')
    user_input = int(user_input)
    matching_indices = np.where(original_list == user_input)
    
    if len(matching_indices[0]) == 0:
          print('Your student ID ({}) is wrong. Try again.'.format(user_input))
          print()
    
    else:
       current_time = datetime.datetime.now().time()
       if current_time < compare_time:
              result_list[matching_indices] = 1
       else:
              result_list[matching_indices] = 0.5
       count += 1

    
    

        
