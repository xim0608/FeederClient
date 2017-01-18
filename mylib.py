from datetime import datetime, timedelta

class Lib:
    @classmethod
    def prints(cls, line):
        print("[" + (datetime.utcnow() + timedelta(hours=9)).strftime('%Y/%m/%d %H:%M:%S') + "]: " + line)