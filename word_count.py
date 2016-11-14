# First I create a function that takes in an attribute "string"
def words(string):
      ''' the second step requires that we count all words using str as a
       separator
       '''
   	my_string = string.split()
      '''
      Here create an empty dictionary called "my_dict"
       It's purpose is to store the number of words in the 
       string "my_string"
       '''
   	my_dict = {}
   	for item in my_string:
   		# This step tests for integer values
         try:                    
   			item2 = int(item)
   		except:
   			item2 = item

         #Loop through the words and add the count into "my_dict"
   		if item2 in my_dict:   
   			my_dict[item2] += 1
   		else:
   			my_dict[item2] = 1
   	return my_dict