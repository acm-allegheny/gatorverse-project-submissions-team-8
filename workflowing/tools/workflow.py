# This will be the file containing the task class and the functions that will be used to create, edit, and delete tasks.
# Tasks will have diffrent data values partaingin to the description of the tast, status of the task, and the time it was created, and when the task is to be done by.
# future scope will be to add a priority level to the task, and a way to sort the tasks by priority level, and chokehold and throttles for tasks that must be completed before other tasks.

from .subtask import Subtask

class workflow:
    """
    This class will hold all of the information for a workflow.
    The workflow will have a name, description, status, and end date.
    """
    def __init__(self, name, description, status, end_date):
        self.name = name
        self.description = description
        self.status = status
        self.end_date = end_date
        self.subtasks = []  # Initialize an empty list for subtasks
        
    def __str__(self):
        return f"workflow: {self.name}, Description: {self.description}, Status: {self.status}, End Date: {self.end_date}"
    
    def add_subtask(self, subtask):
        """
        This function will add a subtask to the workflow.
        
        Parameters:
        subtask (Subtask): The subtask object to add.
        """
        if isinstance(subtask, Subtask):
            self.subtasks.append(subtask)

    def remove_subtask(self, subtask_name):
        """
        This function will remove a subtask from the workflow.
        
        Parameters:
        subtask_name (str): The name of the subtask to remove.
        
        Returns:
        bool: True if the subtask was removed, False if the subtask was not found.
        """
        for subtask in self.subtasks:
            if subtask.name == subtask_name:
                self.subtasks.remove(subtask)
                return True
        return False
    
    def get_subtasks(self):
        """
        This function will return the list of subtasks.
        
        Returns:
        list: The list of subtasks.
        """
        return self.subtasks
    
    def get_status(self):
        """
        This function will return the status of the workflow.
        
        Returns:
        str: The status of the workflow.
        """
        return self.status

    def set_status(self, status):
        """
        This function will set the status of the workflow.
        
        Parameters:
        status (str): The status of the workflow.
        """
        self.status = status    

    def get_end_date(self):
        """
        This function will return the end date of the workflow.
        
        Returns:
        str: The end date of the workflow.
        """
        return self.end_date
    
    def set_end_date(self, end_date):
        """
        This function will set the end date of the workflow.
        
        Parameters:
        end_date (str): The end date of the workflow.
        """
        self.end_date = end_date
    
    def get_description(self):
        """
        This function will return the description of the workflow.
        
        Returns:
        str: The description of the workflow.
        """
        return self.description
    
    def set_description(self, description):
        """
        This function will set the description of the workflow.
        
        Parameters:
        description (str): The description of the workflow.
        """
        self.description = description
    
    def get_name(self):
        """
        This function will return the name of the workflow.
        
        Returns:
        str: The name of the workflow.
        """
        return self.name
    
    def set_name(self, name):
        """
        This function will set the name of the workflow.
        
        Parameters:
        name (str): The name of the workflow.
        """
        self.name = name
    
    def get_subtask(self, subtask_name):
        """
        This function will return the subtask by name.
        
        Parameters:
        subtask_name (str): The name of the subtask.
        
        Returns:
        Subtask: The subtask object, or None if not found.
        """
        for subtask in self.subtasks:
            if subtask.name == subtask_name:
                return subtask
        return None
