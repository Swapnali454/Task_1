# Task_1
Create a form in the frontend where the user will upload the provided csv file (data.csv). After the csv is uploaded, the contents of the csv should be inserted into the database. You should use the pandas library to read the uploaded csv. You have to store the following information from the csv into the database.
Steps to run the task_1 file:
Step 1:Open the XAMPP server
Step 2:Connect your sql server with " mysql -u root" command.
Step 3: After connecting to your mysql server Create the database which we are going to use for our task.
Step 4: To create the database use the query " CREATE DATABASE interview;" the db will be create the use it with query "USE interview;"
Step 5: Now create the table where we are going to insert our data.
          Query for table creation:
          CREATE TABLE mydata(id int,
          star_rating float,
          title varchar(25),
          content_rating varchar(10),
          genre varchar(10),
          duration float);
 Now the table is created.
 Step 6: Come back to the task file now open it and run the code.
 Note: the movie.csv file should be in the same folder where the code file is present.
 The code will be executed and the message "Data transferted successfully...!" will be displayed.
