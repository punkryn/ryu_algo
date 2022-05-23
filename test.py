class FuncEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year
    
    def __str__(self):
        return f"FuncEvent(tags={self.tags}, year={self.year})"

tags = ['google', 'ml']
year = 2022
bootcamp = FuncEvent(tags)
tags.append('bootcamp')
yaer = 2023
print(bootcamp)