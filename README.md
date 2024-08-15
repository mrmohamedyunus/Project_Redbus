Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Project Overview
The "Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit" project focuses on automating the extraction of bus travel data from the Redbus website. The data is stored in a SQL database and visualized through an interactive Streamlit application that allows users to filter and analyze the data based on various criteria.

Skills Utilized
Web Scraping: Selenium, Python
Data Storage: SQL
Data Visualization: Streamlit
Data Analysis: SQL, Python
Problem Statement
This project addresses the need for efficient data collection and analysis in the transportation industry. By automating the scraping of bus routes, schedules, prices, and seat availability from Redbus, the project provides valuable insights that can improve operational efficiency and strategic planning.

Business Use Cases
Travel Aggregators: Real-time bus schedules and seat availability for customers.
Market Analysis: Travel patterns and preferences for market research.
Customer Service: Enhanced user experience with customized travel options.
Competitor Analysis: Comparing pricing and service levels.
Approach
Data Scraping: Selenium is used to extract data such as routes, schedules, prices, and seat availability from Redbus.
Data Storage: The scraped data is stored in a structured SQL database.
Streamlit Application: An interactive Streamlit application is developed for filtering and visualizing the data.
Data Set
Source: Redbus(https://www.redbus.in/)
Format: SQL database
Fields: Bus route name, route link, bus name, bus type, departure time, duration, arrival time, star rating, price, seat availability.
Database Schema
The data is stored in a table called bus_routes with the following schema:

Column Name	Data Type	Description
id	INT	Primary Key (Auto-increment)
route_name	TEXT	Bus route information
route_link	TEXT	Link to the route details
busname	TEXT	Name of the bus
bustype	TEXT	Type of the bus
departing_time	TIME	Departure time
duration	TEXT	Duration of the journey
reaching_time	TIME	Arrival time
star_rating	FLOAT	Rating of the bus
price	DECIMAL	Price of the ticket
seats_available	INT	Number of seats available
Results
Successfully scraped data from at least 10 Government State Bus Transport routes and private buses.
Stored the data in a SQL database.
Developed a user-friendly Streamlit application for data filtering and visualization.
Project Evaluation Metrics
Data Scraping Accuracy: Completeness and correctness of the scraped data.
Database Design: Efficient database schema.
Application Usability: User experience and ease of use.
Filter Functionality: Effectiveness and responsiveness of data filters.
Code Quality: Adherence to coding standards and best practices.
Installation

Install the required packages using pip install selenium.
Set up the SQL database using the provided schema.
Run the Streamlit application with streamlit run app.py.
Usage
Launch the Streamlit application.
Use the provided filters to analyze bus routes, schedules, prices, and more.
Project Structure
data_scraping.py: Script for scraping data using Selenium.
database.py: SQL database schema and interaction.
app.py: Streamlit application code.
requirements.txt: List of dependencies.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or suggestions, feel free to reach out at [your email].

You can adjust and expand on this template based on your specific project details. Would you like any additional sections or more detail on how to format specific parts?





You said:
i need with # heading and **_** short heading change in that format
ChatGPT said:
ChatGPT
Here's the README with # for headings and **_ for short headings:

Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Project Overview
The "Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit" project focuses on automating the extraction of bus travel data from the Redbus website. The data is stored in a SQL database and visualized through an interactive Streamlit application that allows users to filter and analyze the data based on various criteria.

Skills Utilized
Web Scraping: Selenium, Python
Data Storage: SQL
Data Visualization: Streamlit
Data Analysis: SQL, Python
Problem Statement
This project addresses the need for efficient data collection and analysis in the transportation industry. By automating the scraping of bus routes, schedules, prices, and seat availability from Redbus, the project provides valuable insights that can improve operational efficiency and strategic planning.

Business Use Cases
Travel Aggregators: Real-time bus schedules and seat availability for customers.
Market Analysis: Travel patterns and preferences for market research.
Customer Service: Enhanced user experience with customized travel options.
Competitor Analysis: Comparing pricing and service levels.
Approach
Data Scraping: Selenium is used to extract data such as routes, schedules, prices, and seat availability from Redbus.
Data Storage: The scraped data is stored in a structured SQL database.
Streamlit Application: An interactive Streamlit application is developed for filtering and visualizing the data.
Data Set
Source: Redbus
Format: SQL database
Fields: Bus route name, route link, bus name, bus type, departure time, duration, arrival time, star rating, price, seat availability.
Database Schema
The data is stored in a table called bus_routes with the following schema:

Column Name	Data Type	Description
id	INT	Primary Key (Auto-increment)
route_name	TEXT	Bus route information
route_link	TEXT	Link to the route details
busname	TEXT	Name of the bus
bustype	TEXT	Type of the bus
departing_time	TIME	Departure time
duration	TEXT	Duration of the journey
reaching_time	TIME	Arrival time
star_rating	FLOAT	Rating of the bus
price	DECIMAL	Price of the ticket
seats_available	INT	Number of seats available
Results
Successfully scraped data from at least 10 Government State Bus Transport routes and private buses.
Stored the data in a SQL database.
Developed a user-friendly Streamlit application for data filtering and visualization.
Project Evaluation Metrics
Data Scraping Accuracy: Completeness and correctness of the scraped data.
Database Design: Efficient database schema.
Application Usability: User experience and ease of use.
Filter Functionality: Effectiveness and responsiveness of data filters.
Code Quality: Adherence to coding standards and best practices.
Installation
Clone this repository.
Install the required packages using pip install -r requirements.txt.
Set up the SQL database using the provided schema.
Run the Streamlit application with streamlit run app.py.
Usage
Launch the Streamlit application.
Use the provided filters to analyze bus routes, schedules, prices, and more.
Project Structure
data_scraping.py: Script for scraping data using Selenium.
database.py: SQL database schema and interaction.
app.py: Streamlit application code.
requirements.txt: List of dependencies.

Contact
For any questions or suggestions, feel free to reach out at [mryunus.in@gmail.com].
![Screenshot (34)](https://github.com/user-attachments/assets/a0a4372a-f04a-4ad2-b3dc-71a09cb548b7)

