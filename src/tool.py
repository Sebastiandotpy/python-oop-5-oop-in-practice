from abc import ABC, abstractmethod

# Do not modify this class
class Tool:
    def work(self):
        raise NotImplementedError("Abstract Method not implemented")


# Write your code here to implement the Laptop class correctly

class Tool(ABC):
    """Abstract class representing a tool."""
    
    @abstractmethod
    def work(self):
        """Perform the work specific to the tool."""
        pass

class Laptop(Tool):
    """Subclass representing a laptop tool."""
    
    def work(self):
        """Print a message indicating that the laptop is running."""
        print("Laptop is running")




