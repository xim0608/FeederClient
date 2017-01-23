from datetime import datetime, timedelta

class Lib:
    @classmethod
    def prints(cls, line):
        # [2017/01/22 17:22:30]: (line)
        print("[" + (datetime.utcnow() + timedelta(hours=9)).strftime('%Y/%m/%d %H:%M:%S') + "]: " + line)