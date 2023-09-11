"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
   e()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """ 
    def __init__(self,start):
        self.start=start
        self.original_start=start
        
    def __repr__(self):
        return f"Serial Number---> originial serial number={self.original_start}. The current serial number = {self.start}."
        
    def generate(self):
        """Generates the next sequential number, beginning at the start value"""
        self.start += 1
        return self.start -1
    
    def reset(self):
        """Resets the generator to the original start value"""
        self.start=self.original_start
       
        
   
        
        

