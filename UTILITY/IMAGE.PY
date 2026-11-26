"""
ALL IMAGES HAVE WETHER TO REPLACE OR RETURN A COPY
"""
from helper import Helper

  
            
class Images(Helper):
    def __init__(self, raise_error=True):
        super().__init__(raise_error)
        
    def convert(self, file_path: str, new_format:str, *args, **kwargs)-> dict:
        
        file_ext = file_path.split(".")
        ERRORS = []
        MESSAGE = None
        if len(file_ext) != 2:
            msg = "Not a valid image file"
            self._call_exception(exception_type=TypeError(msg))
            ERRORS.append(msg)
        elif file_ext[-1].upper() not in self.supported_image_format:
            msg =  'Unsupported image type'
            self._call_exception(exception_type=TypeError(msg))
            ERRORS.append(msg)
            
        # FILE VALID IMAGE AND EXTENSION IN OUR SUPPORTED
        return self._return_message('success', ERRORS)
            


# TEST 
print(Images().supported_image_format)

# print(Images().raise_error)

# print(Images(raise_error=False).convert(file_path='',new_format='png'))