"""
In order to use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file, 
what steps should we take? (Check all that apply)



Create an instance of the DictWriter() class

Correct
Excellent! We have to create a DictWriter() object instance to work with, and pass to it the fieldnames parameter defined as a list of keys.


Write the fieldnames parameter into the first row using writeheader()

Correct
Nice work! The non-optional fieldnames parameter list values should be written to the first row.


Open the csv file using with open

Correct
Good call! The CSV file has to be open before we can write to it.


"""