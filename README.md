# AffinityAnswers_Test_DE
Assessment questions of Affinity Answers 

1. BestDelivery Courier Company has an issue. Many parcels they get to deliver have the wrong PIN code and that leads to packages going to the wrong location and then someone figuring out manually that the PIN code is wrong from the other parts of the address. You are the programmer who has to fix this issue by writing a program that takes as input a free flowing address and checking if the PIN code indeed corresponds to the address mentioned. Use this free API postalpincode.in/Api-Details for the purpose of PIN code identification.
e.g. of correct addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”,
"2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”, "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050”,
e.g. of an incorrect addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095”,
“Colony, Bengaluru, Karnataka 560050”

Once you have written the program above, list the test cases you would use to test your program.

https://github.com/mayankvashisht/AffinityAnswers_Test_DE/tree/main/Question%201%20-%20Validate%20Pincode


2. The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: docs.rfam.org/en/latest/database.html
a. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
b. Find all the columns that can be used to connect the tables in the given database.
c. Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)
d. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)


3. This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a tsv file. And ever wondered if this data should not be stored in JSON
