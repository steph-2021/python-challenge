#Import CSV Data File
import os
import csv

#Path to collect data from the Resources folder
#def create_file(budget_data_csv):
path_file = os.path.join('\\Users\\stephaniewilson2014\\Documents\\steph\\Butler Education\\Homework\\Python Homework\\PyBank\\Resources\\budget_data.csv')
month_count = 0
total_value = 0
change_list=[]   
month_maxchange = [] 
month_minchange = []


#Open and read csv file
with open(path_file) as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row=next(reader)
    first_value=int(first_row[1])
    #print(row)   
    for row in reader:
        print(row)
        month_count+=1
        total_value+=int(row[1]) 
        print(month_count+1)
        print(total_value/month_count)
        net_change=int(row[1])-first_value
        first_value=int(row[1])
        change_list.append(net_change)
        month_maxchange+=[row[0]]
        month_minchange+=[row[0]]
    max_increase=max(change_list)
    min_increase=min(change_list)
    index_maxchange=change_list.index(max_increase)
    index_minchange=change_list.index(min_increase)
    print(month_maxchange[index_maxchange])
    print(month_minchange[index_minchange])
  
   
results = (f"Financial Analysis\n"
f"----------------------"
f"Total Months: {month_count+1}\n"
f"Total: ${total_value}\n"
f"Average Change: ${total_value/month_count}\n"
f"Greatest Increase in Profits: {month_maxchange[index_maxchange]} ${max_increase}\n"
f"Greatest Decrease in Profits: {month_minchange[index_minchange]} ${min_increase}\n")

print(results)

write_results = os.path.join('\\Users\\stephaniewilson2014\\Documents\\steph\\Butler Education\\Homework\\Python Homework\\PyBank\\Analysis\\analysis.text')
with open(write_results, 'w+') as textfile:
        textfile.write(str(results)) 



        

    
        






   
    
   
            



    
    
    

   
        
            
            

