import os 
import datetime
from mutagen.easyid3 import EasyID3 
from mutagen.mp3 import MP3
import glob






lower_case= ['Lower case', 'Lower Case', 'lower case']
upper_case =['Upper case','Upper Case', 'upper case' ]
title_case= ['Title case', 'Title Case', 'title case']




def custom_log ( message,user_name, message_type="INFO"):
 file_name= f"log_user_{user_name}.txt"
 timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 log_output= f"[{timestamp}] [user:{user_name}][{message_type.upper()}] {message}"
 print(log_output)

 try:
    with open(file_name, 'a', encoding='utf-8') as log_file:
            log_file.write(log_output + '\n')
 except Exception as e:
        print(f"CRITICAL ERROR: Could not write to log file for user {user_name}. Reason: {e}")

 
   
 
   





















def meta_tags ():
    user_name = input ('Enter your preferred username ')
   
    
    
    custom_log(f"User entered username:{user_name}", user_name, "INFO" )

    file_extension = input("Enter the file's extension... ")
    custom_log(f"User entered file extension: {file_extension}", user_name, "INFO" )


    if file_extension != '.mp3' :
      
      print('Extension not available for now, coming soon')

    else:
     
     file_directory =  input('Enter the file directory ')
     custom_log(f"User entered file directory: {file_directory}", user_name, "INFO")
    
    my_files = glob.glob(os.path.join(file_directory, "*mp3"))
     
     
    user_request= input('Do you want your file changed to lower case, upper case or title case ')
    custom_log(f"User entered request: {user_request}", user_name, "INFO")

    for my_files in my_files :
                
        audio = MP3(my_files, ID3=EasyID3)
         
        if 'title' in audio and 'artist' in audio:
                    current_title = str(audio['title'][0])
                    current_artist = str(audio['artist'][0])
                    
                    new_title = current_title
                    new_artist = current_artist
                    
                    
                    if user_request in lower_case:
                        new_title = current_title.lower()
                        new_artist = current_artist.lower()
                    
                    elif user_request in upper_case:
                        new_title = current_title.upper()
                        new_artist = current_artist.upper()
                        
                    elif user_request in title_case:
                        new_title = current_title.title()
                        new_artist = current_artist.title()
                        
                    else:
                        print('Invalid case request. Skipping file.')
                        custom_log(f"Invalid request for file: {file_directory}", user_name, "WARNING")
                        continue 
                    
                    
                    audio['title'] = new_title
                    audio['artist'] = new_artist
                    audio.save()
                    
                    print(f"Successfully changed: '{new_artist}' - '{new_title}'")
                    custom_log(f"Updated tags for file: {file_directory}", user_name, "INFO")
                    
        else:
                    print(f"Skipping file {file_directory}: Missing Title or Artist tag.")
                    custom_log(f"Missing tags for file: {file_directory}", user_name, "WARNING")

                    audio['title'] = new_title
                    audio['artist'] = new_artist
                    audio.save()

                    print(f"'{new_artist}'{new_title}'")

       
     
      
 
if __name__ == "__main__":
 meta_tags()