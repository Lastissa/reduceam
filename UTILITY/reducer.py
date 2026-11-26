from helper import Helper
from PIL import Image
import os

class Reducer(Helper):
    def __init__(self, raise_error=True):
        super().__init__(raise_error)

    def reduce(self, file_path: str, target_kb: int = 200, replace: bool = False) -> dict:
        """
        Reduce image size to target KB.
        If replace=True, replace original. If False, return a copy.
        """
        ERRORS = []
        MESSAGE = None

        file_ext = file_path.split(".")
        if len(file_ext) != 2:
            msg = "Not a valid image file"
            self._call_exception(exception_type=TypeError(msg))
            ERRORS.append(msg)
            return self._return_message(MESSAGE, ERRORS)

        elif file_ext[-1].upper() not in self.supported_image_format:
            msg = 'Unsupported image type'
            self._call_exception(exception_type=TypeError(msg))
            ERRORS.append(msg)
            return self._return_message(MESSAGE, ERRORS)

        # FILE VALID, START REDUCE
        try:
            img = Image.open(file_path)
            # Convert to RGB so JPEG fit save
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            output_path = file_path
            if not replace:
                name, ext = os.path.splitext(file_path)
                output_path = f"{name}_reduced{ext}"

            quality = 95
            # Keep reducing quality until e reach target or quality low
            while quality > 10:
                img.save(output_path, quality=quality, optimize=True)
                size_kb = os.path.getsize(output_path) / 1024
                if size_kb <= target_kb:
                    break
                quality -= 5

            MESSAGE = f"Reduced to {os.path.getsize(output_path)/1024:.1f}KB -> {output_path}"
            return self._return_message(MESSAGE, ERRORS)

        except Exception as e:
            msg = str(e)
            self._call_exception(exception_type=Exception(msg))
            ERRORS.append(msg)
            return self._return_message(MESSAGE, ERRORS)

# TEST
# print(Reducer(raise_error=False).reduce(file_path='', target_kb=200))