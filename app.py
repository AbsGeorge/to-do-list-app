#                                  As a user
# I want to view my to-do task, so that I know what I need to do 
# I want to add a new to-do task, so I know I have a task to be completed (no description)
# I want to view my todo tasks, so that I know what I need to do
# I want to change the description of the task, so I can update its contents after creating it
# I want to delete a task, in case I don't need to do that task anymore
# I want to set a todo task as completed, so I know which tasks I've already done
# I want to set a todo task as incomplete, in case a complete task still needs doing

from application import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')