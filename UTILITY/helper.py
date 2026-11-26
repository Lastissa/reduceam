"""
# This file hold all kind of reusable files in other codes, ranging from functions classess to even any reusable variables

"""

from django.conf import settings

class Helper:
    """
    **HELPER CLASS FOR SIMILAR TASK BETWEEN ALL OTHER ACTIVITIES NEEDING IT e.g havign how messages returned universal**
    """
    
    def __init__(self, raise_error=True):
        self.supported_image_format = ['PNG', 'JPEG', 'JPG', 'WEBP']
        self.supported_video_format = ['MP3', 'MKV']
        self.raise_error = raise_error
    
    def _call_exception(self, exception_type = Exception('something went wrong')):
        """will raise an error if raise error is true"""
        if self.raise_error: raise exception_type
        else:pass
    
    def _return_message(self, message = None, error = None)->dict:
        return {
                'messages':message,
                'error': error
                }
    
PROJECT_SIGN_KEY = settings.PROJECT_SIGN_KEY or None