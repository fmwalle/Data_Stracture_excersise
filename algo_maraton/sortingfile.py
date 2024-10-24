#from datetime import datetime
def sortFiles(files: list) -> list:
    
    def sortbydate(file):
        date,time=file['date'].split(' ')
        m,d,y=date.split("-")
        m=m.zfill(2)
        d=d.zfill(2)

        return f"{y}{m},{d}{time}"
    return sorted(files,key=lambda f:(sortbydate(f),f['filename']),reverse=True)




myfile = [
    {"filename": "otter.mpeg", "size": 512, "date": "01-16-2023 14:23:13"},
    {"filename": "oliver.mp4", "size": 1024, "date": "01-18-2023 12:46:57"},
]

print(sortFiles(myfile))  


words=['apple','banana','kiwi']

answer=sorted(words,key=lambda w:len(w))
print(answer)