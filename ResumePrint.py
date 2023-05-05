import traceback
import codecs

MAXLENGTH = 512
print("PRINT RESUMER")
IMAGE_WIDTH:int=int(input("Image width \n\
1)  350\n\
2)  696\n\
3) 1024\n\
any other number will be considered as resolution itself: "))

if IMAGE_WIDTH==1:
  IMAGE_WIDTH=350
elif IMAGE_WIDTH==2:
  IMAGE_WIDTH=696
elif IMAGE_WIDTH==3:
  IMAGE_WIDTH=1024

start_at_line:int=int(input("Start at line: "))

def process_line(string,image_width:int,start_at_line:int,actually_processed_pixels:int=0):
  
  # Initialize a variable to store the current number
  offset:int=image_width*start_at_line
  current_number = ""
  currnet_length:int = 0
  i:int= 0;
  actual_color=""
  actual_string = ""

  for char in string:
    
    i=i+1
    remaining_color = ""
    #print(char, i)
    if char.isdecimal():
      current_number += char
    else:
      if current_number:
        currnet_length=int(current_number)
        actual_color = current_number+char
        current_number = ""        
      else:
        currnet_length:int=1
        actual_color = char
      

      if (currnet_length + actually_processed_pixels > offset):
        remaining_color_length = currnet_length + actually_processed_pixels - offset
       
        if remaining_color_length>1:
          remaining_color=f"{remaining_color_length}"
          actually_processed_pixels+=currnet_length
          return (actually_processed_pixels,remaining_color, i, True)
        else:
          actually_processed_pixels+=currnet_length
          return (actually_processed_pixels,"", i, True)
      actually_processed_pixels+=currnet_length

        
  return actually_processed_pixels, remaining_color, i, False



try:


  with codecs.open("image_data.txt", "r", "utf-8") as f:
    try:
        i = -1
        actually_processed_pixels:int = 0
        lines=[]
        for line in f:
          i=i+1
          actually_processed_pixels,remaining_color, char_pos, done = process_line(line.rstrip(),IMAGE_WIDTH,start_at_line,actually_processed_pixels)
          lines.append(line.rstrip())
          if done:
            break
    except EOFError:
        pass
    except UnicodeDecodeError:
        with open("image_data.txt", "r") as f:
          try:
              i = -1
              actually_processed_pixels:int = 0
              lines=[]
              for line in f:
                i=i+1
                actually_processed_pixels,remaining_color, char_pos, done = process_line(line.rstrip(),IMAGE_WIDTH,start_at_line,actually_processed_pixels)
                lines.append(line.rstrip())
                if done:
                  break
          except EOFError:
              pass

##  with open("image_data.txt", "r") as f:
##    try:
##        i = -1
##        actually_processed_pixels:int = 0
##        lines=[]
##        for line in f:
##          i=i+1
##          actually_processed_pixels,remaining_color, char_pos, done = process_line(line.rstrip(),IMAGE_WIDTH,start_at_line,actually_processed_pixels)
##          lines.append(line.rstrip())
##          if done:
##            break
##    except EOFError:
##        pass


  print("\n\nLINE:", i, "\nCHAR:", char_pos, "\nREM COLOR:", remaining_color)

  input("\n\nPress ENTER")

except FileNotFoundError:
  print("ERROR: Unable to open image_data.txt")
  input("\nPress ENTER to continue") 
except Exception:
  traceback.print_exc()
  input("\n\nPress ENTER to continue")

