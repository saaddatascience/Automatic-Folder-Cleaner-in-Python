import os # module 

def createIfNotExiss(folder): # function basically to create a file if it doesnt exists 
    if not os.path.exists('images'): # used os.path.exists 
     os.makedirs('images')          

def move(folderName , files):
   for file in files:
      os.replace(file , f"{folderName}/{files}") 


files = os.listdir()
files.remove("python_practice5.py")
print(files)

createIfNotExiss('images')
createIfNotExiss('Docs')
createIfNotExiss('media')
createIfNotExiss("others")

imgExts = [".png" , ".jpg" , "jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

docExrs = ['.txt' , '.docx' , '.doc' , '.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExrs]

mediaExts = ['.mp4' , '.mp3' , '.fiv']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
   ext = os.path.splitext(file)[1].lower()
   if (ext not in imgExts) and (ext not in docExrs) and (ext not in mediaExts) and os.path.isfile(file):
      others.append(file)


move("images" , images)  
move("docs" , docs)  
move("medias" , medias) 
move("others" , others) 