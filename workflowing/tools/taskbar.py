from tools.subtask import Subtask
from tools.workflow import workflow as Workflow  # Ensure correct capitalization

# This file is meant to be the functions based around our taskbar that will hold all of our tasks.
# The general idea is to have a taskbar that will hold all of our tasks and allow us to add, remove, and edit tasks.
# The taskbar will be a list of tasks that will be displayed in the taskbar.

def create_taskbar():
    """
    This function will create a taskbar that will hold all of our tasks.
    The taskbar will be a list of tasks that will be displayed in the taskbar.
    """
    # Create a list to hold the tasks
    taskbar = []
    return taskbar

def delete_workflow(taskbar, workflow_name):
    """
    This function will remove a workflow from the taskbar.
    
    Parameters:
    taskbar (list): The list of workflows.
    workflow_name (str): The name of the workflow to remove.
        
    Returns:
    bool: True if the workflow was removed, False if the workflow was not found.
    """
    for wf in taskbar:
        if wf.name == workflow_name:
            taskbar.remove(wf)
            return True
    return False

def add_workflow(taskbar, workflow_obj):
    """
    This function will add a workflow to the taskbar.
    
    Parameters:
    taskbar (list): The list of workflows.
    workflow_obj (Workflow): The workflow object to add.
    
    Returns:
    bool: True if the workflow was added, False if the workflow was already in the taskbar.
    """
    if all(wf.name != workflow_obj.name for wf in taskbar):
        taskbar.append(workflow_obj)
        return True
    return False

