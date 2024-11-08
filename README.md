Hello! This is a quiz program that is implemented using python and GUIs. There really isn't much to it, but I'll tell you what is used for what. 

README:
YOU'RE READING IT RIGHT NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

questionmodifier.py:
This program allows you to select whatever quiz you'd like, then view/add/remove questions. This will affect the database, so remove wisely!! 

quiz_bowl.db:
The file which contains all of the data for the quiz. Don't mess around with this unless you know what you're doing!!!

quizprogram.py:
This is where all the meat and potatoes are. To use this program, you will need to launch it, then select whatever quiz you'd like to take. Upon doing that, the quiz selection window will dissappear, and a new quiz window will appear. There is an answer box that you can input your answers in, and you can submit them by clicking the submit button. A popup window will tell you whether your answer is correct or wrong, and if it is wrong, it will give you the correct answer. Upon completion of the quiz, it will show you your score.


Here are all of the questions I put in here. Sorry that some of the answers are long, I was being lazy and just took longwinded answers from my notes.

    #ECON2020
    1, 'Who was responsible the 2008 financial crisis happen?', 'Banks'
    2, 'What is the amount of money spent when making a decision?', 'Accounting Cost'
    3, 'What is the cost of making one decision over another called?', 'Opportunity Cost'
    4, 'What is it called when someone focuses on producing specific goods/services? ', 'Specialization'
    5, 'What is the difference between a customers willingness to pay for a good and the market price?', 'Consumer Surplus'
    6, 'What is the difference between a sellers production cost and the market price?', 'Producer Surplus'
    7, 'What is a form of price control that doesnt allow prices to rise above a certain level?', 'Price Ceiling'
    8, 'What is a form of price control that sets a minumum price?', 'Price Floor'
    9, 'What can occur when there is a surplus of avilable workers?', 'Unemployment'
    10, 'What says that identical goods should trade at the same price?', 'Law of One Price'

    # DS3850 Questions
    1, 'What keyword is used to define a function?', 'def'
    2, 'What character is needed to create a list?', 'brackets'
    3, 'What is the output of this? print(5 + 3 * 2)', '11'
    4, 'What does the len() function do?', 'returns the length of a string, list, or tuple'
    5, 'What defines a dictionary?', 'curly braces'
    6, 'What is the syntax to create a class?', 'class classname'
    7, 'Can you use list.append() to add new items to a list?', 'Yes'
    8, 'What is the result of this code? Hello + World', 'Hello World'
    9, 'What can you use to end a for loop?', 'break'
    10, 'When you define a variable, is it case sensitive?', 'Yes'

    # ECON3610 Questions
    1, 'What is the mean of this dataset? 5 7 8 12 15 20', '10'
    2, 'In a normal distribution, what percentage of data lies within one standard deviation of the mean?', '68%'
    3, 'What is the purpose of a p-value in hypothesis testing?', 'To determine the likelihood of the null hypothesis being true'
    4, 'What is a discrete random variable?', 'A variable that can take on a finite number of values'
    5, 'What does a correlation coefficient of 0.85 imply about the relationship between two variables?', 'Strong positive linear relationship'
    6, 'What is a sample standard deviation used for?', 'estimating the population standard deviation'
    7, 'What distribution is used for occurrences of an event in a fixed interval of time?', 'Poisson distribution'
    8, 'What does the coefficient of determination R^2 measure?', 'The strength of the relationship between the dependent and independent variables'
    9, 'What occurs when there is a type 1 error?', 'rejecting the null hypothesis when it is actually true'
    10, 'What does the central limit theorem state about the distribution of sample means?', 'The distribution of sample means will approach a normal distribution as the sample size increases'

    # DS3680 Questions
    1, 'What is a primary key?', 'A unique identifier for each record in a table'
    2, 'What does SQL stand for?', 'Structured Query Language'
    3, 'What SQL statement retrieves data from a database?', 'SELECT'
    4, 'What is normalization?', 'The process of reducing redundancy and improving data integrity'
    5, 'What SQL command is used to add new data into a table?', 'INSERT'
    6, 'What is required for a join?', 'Two tables and a common field'
    7, 'What does a foreign key represent?', 'A field in one table that refers to the primary key of another table'
    8, 'What is the purpose of an index?', 'To speed up data retrieval '
    9, 'What is a NULL value', 'an indicator of data absence '
    10, 'What kind of relationship would a student who can enroll in many courses, and each course can have many students be?', 'many to many'

    # ACCT2120 Questions
    1, 'What is the primary purpose of financial accounting?', 'to prepare financial statements for external users'
    2, 'Is accounts payable an example of a current liability?', 'yes'
    3, 'What does accrual basis of accounting mean?', 'Revenues are recognized when earned, regardless of when cash is recieved'
    4, 'What is straight line depreciation?', 'The even cost of an asset over its life'
    5, 'What does FIFO stand for?', 'First in First Out'
    6, 'What does LIFO stand for?', 'Last in First Out'
    7, 'What is operating income?', 'Income generated by business activities'
    8, 'Are bonds & notes payable liabilities?', 'yes'
    9, 'What is the current ratio formula?', 'Current Assets/Current Liabilities'
    10, 'Do you record Bad Debt Expenses when company accounts recievable cannot be collected?', 'yes'