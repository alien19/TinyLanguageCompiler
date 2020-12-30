class ScannerError(Exception):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

class ParserError(Exception):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)