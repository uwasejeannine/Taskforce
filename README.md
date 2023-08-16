**THE PROJECT FUNCTIONALITY
**
Transaction Tracking:

Eric will be able to add incoming and outgoing transactions from various accounts.
They can select the account type (bank account, mobile money, etc.) and amount for each transaction.
They can associate transactions with specific categories and subcategories.
Budget Management:

Eric will be able to set budget limits.
The application will calculate and compare the total expenses to the set budget.
If costs exceed the budget, the application will notify the user.

Category and Subcategory Management:
Eric will be able to define categories and subcategories for better organization of expenses.
Subcategories are linked to parent categories.
Expense Categorization:

Report Generation:

Eric will generate reports by specifying a start and end date.
The application will display transactions within the selected date range.
It will calculate and display the total expenses for that period.
Transaction Visualization:

Eric can view transaction summaries in a visualized manner.

**ADMIN INTERFACE 
**The Django admin interface allows administrators to manage data efficiently.

Admins can add, edit, and delete records from the Category, Subcategory, Transaction, and Budget models.
Frontend Views:
The frontend provides views for adding transactions, setting budgets, generating reports, and displaying transaction summaries.
Users can interact with these views through forms and links.

**HOW TO START A PROJECT
**
Installation
I have created a GitHub repo and cloned the repository to my local machine.
I then navigated to the repo using  a command-line interface (cd command).
Pip install django (To insall all the nesecary packages)
Backend Setup
I have created a new project using this command(in window)
django-admin startproject wallet_tracker
I created the app that i will put all the files into
django-admin startapp wallet
Create the virtual environment for the Django project and activate it.
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt ( To install the required packages)

**END**
