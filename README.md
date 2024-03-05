# python_project
1. Define the Student Model:

    In student/models.py, define the Student model.

2. Create URLs for the CRUD Views:

    In student/urls.py, define URL patterns for the CRUD views.
    Include these patterns in the main urls.py of your project.
    
3. Create CRUD Views:

    In student/views.py, define the CRUD views (StudentList, StudentCreate, StudentUpdate, StudentDelete).

4. Create Templates:

    Create HTML templates for the views in student/templates/student/
   
6. Run Migrations:

    Run python manage.py makemigrations and python manage.py migrate to apply the model changes to the database.

7. Start the Development Server:

    Run python manage.py runserver to start the development server.
