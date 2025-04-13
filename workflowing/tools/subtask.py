#File dealing with subtasks to be under the workflow class.
# Github Copilot was used to help with the code in this file.
class Subtask:
    """
    This class will hold all of the information for a subtask.
    A subtask will have a name, description, status, end date, and a reference to its parent workflow.
    """
    def __init__(self, name, description, status, end_date, parent_workflow):
        self.name = name
        self.title = None
        self.description = description
        self.status = status
        self.end_date = end_date
        self.parent_workflow = parent_workflow
        self.not_subtask = False
        self.subtasks = []  # Initialize an empty list for subtasks


    def __str__(self):
        if self.not_subtask:
            return f"{self.title}: {self.name}, Description: {self.description}, Parent Workflow: {self.parent_workflow.name}"
        else:
            return f"Subtask: {self.name}, Description: {self.description}, Status: {self.status}, End Date: {self.end_date}, Parent Workflow: {self.parent_workflow.name}"
    
    def get_status(self):
        """
        This function will return the status of the subtask.
        
        Returns:
        str: The status of the subtask.
        """
        return self.status

    def set_status(self, status):
        """
        This function will set the status of the subtask.
        
        Parameters:
        status (str): The status of the subtask.
        """
        self.status = status

    def get_end_date(self):
        """
        This function will return the end date of the subtask.
        
        Returns:
        str: The end date of the subtask.
        """
        return self.end_date
    
    def set_end_date(self, end_date):
        """
        This function will set the end date of the subtask.
        
        Parameters:
        end_date (str): The end date of the subtask.
        """
        self.end_date = end_date
    
    def get_description(self):
        """
        This function will return the description of the subtask.
        
        Returns:
        str: The description of the subtask.
        """
        return self.description
    
    def set_description(self, description):
        """
        This function will set the description of the subtask.
        
        Parameters:
        description (str): The description of the subtask.
        """
        self.description = description
    
    def get_name(self):
        """
        This function will return the name of the subtask.
        
        Returns:
        str: The name of the subtask.
        """
        return self.name
    
    def set_name(self, name):
        """
        This function will set the name of the subtask.
        
        Parameters:
        name (str): The name of the subtask.
        """
        self.name = name

    def get_parent_workflow(self):
        """
        This function will return the parent workflow of the subtask.
        
        Returns:
        Workflow: The parent workflow.
        """
        return self.parent_workflow

    def add_subtask(self, subtask):
        """
        This function will add a subtask to this subtask.
        
        Parameters:
        subtask (Subtask): The subtask object to add.
        """
        if isinstance(subtask, Subtask):
            self.subtasks.append(subtask)

    def remove_subtask(self, subtask_name):
        """
        This function will remove a subtask from this subtask.
        
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
        This function will return the list of subtasks for this subtask.
        
        Returns:
        list: The list of subtasks.
        """
        return self.subtasks

    def get_subtask(self, subtask_name):
        """
        This function will return a subtask by name from this subtask.
        
        Parameters:
        subtask_name (str): The name of the subtask.
        
        Returns:
        Subtask: The subtask object, or None if not found.
        """
        for subtask in self.subtasks:
            if subtask.name == subtask_name:
                return subtask
        return None

    def get_title(self):
        """
        This function will return the title of the subtask.
        
        Returns:
        str: The title of the subtask.
        """
        return self.title

    def set_title(self, title):
        """
        This function will set the title of the subtask.
        
        Parameters:
        title (str): The title of the subtask.
        """
        self.title = title

    def get_not_subtask(self):
        """
        This function will return whether the subtask is marked as not a subtask.
        
        Returns:
        bool: True if not a subtask, False otherwise.
        """
        return self.not_subtask

    def set_not_subtask(self, not_subtask):
        """
        This function will set whether the subtask is marked as not a subtask.
        
        Parameters:
        not_subtask (bool): True if not a subtask, False otherwise.
        """
        self.not_subtask = not_subtask

