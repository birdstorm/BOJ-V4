
class CONST():
    LANGUAGE_LENGTH = 8
    LANGUAGE = (
        ( 'gcc', 'GNU C'),
        ( 'g++', 'GNU C++'),
        ( 'java', 'java'),
    )
    LANGUAGE_DEFAULT = 'g++'

    STATUS_CODE = (
        ( 'PD', 'Pending'),
        ( 'SE', 'System Error'),
        ( 'CL', 'Compiling'),
        ( 'CE', 'Compilation Error'),
        ( 'JD', 'Judging'),
        ( 'AC', 'Accepted'),
        ( 'PE', 'Presentation Error'),
        ( 'WA', 'Wrong Answer'),
        ( 'RE', 'Runtime Error'),
        ( 'TLE', 'Time Limit Exceed'),
        ( 'MLE', 'Memory Limit Exceed'),
        ( 'OLE', 'Output Limit Exceed'),
        ( 'EXT', 'Extended Judge Result'),
        ( 'NUM', 'Judge Score'),
    )
    STATUS_DEFAULT = 'PD'
    