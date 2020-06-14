import unittest

# all unit test is a class module 
# you have to import the class library 



#a whole bunch of code here but then u have to createn space for the test below 
#I can put functions here 




#This is where the unit test goes for testing the function 

class TestStringMethods(unitest.TestCase): #<--in this class u can create different functions example upper or lower case example below 

		def test_upper(self) # creating our function for upper case

				self.assertEqual('foo'.upper(), 'FOO')# <-- your just testing to see if its upper; here we want to make sure something is equal to something;this is a function in this unit class 

			def test_isupper(self): # write another function 

				self.assertTrue('FOO'.isupper()) #in the argumative example you have to give an example of that
				self.assertFalse("Foo".isupper()) #<--this is checking if its a upper case letter 

					#now we want to see if their is a space between 2 differnt words 
			def test_split(self): # in the argumative parameters remebr that is what is being tested 

				s = 'hello world' #created a string variable 
				self.assert(s.split(),['hello',, 'world']) # we called it self, pass in the strings;
				#Check that s.split fails when the seprator is not a string 

				with self.assertRaises(TypeError): 
					s.split(2)

					#call this maain function  #run this class with the main function; depdning on how you want to compile the code usally they want u to call the main functions
				if __name__ =='__main__':
					unittest.main() 
					# now were done this tested 3 string methods 



