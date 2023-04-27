import traceback

MAXLENGTH = 512
OFFSET=300
print("image_data.txt SPLIT")

IMAGE_WIDTH:int=int(input("Image width \n\
1)  350\n\
2)  696\n\
3) 1024\n\
any other number will be considered as resolution itself: "))


OFFSET:int=int(input("Split line: "))


if IMAGE_WIDTH==1:
  IMAGE_WIDTH=350
elif IMAGE_WIDTH==2:
  IMAGE_WIDTH=696
elif IMAGE_WIDTH==3:
  IMAGE_WIDTH=1024

def process_line(string,image_width,offset_lines,actually_processed_pixels=0):
    # Initialize a variable to store the current number
    offset:int=image_width*offset_lines
    current_number = ""
    currnet_length = 0
    i:int= 0;
    UP_string:str = []
    DOWN_string:str = []
    actual_color=""
    actual_string = ""
    fill_up=True
    breached=False
    b_actually_processed_pixels=0
    remaining_color=""
    b_pos=0
    for char in string:
      
      i=i+1
      #print(char, i)
      if char.isdecimal():
        current_number += char
      else:
        if current_number:
          currnet_length=int(current_number)
          actual_color = current_number+char
          current_number = ""        
        else:
          currnet_length=1
          actual_color = char

        if (currnet_length + actually_processed_pixels > offset) and not breached:
          #print(currnet_length,char)
          remaining_color_length = currnet_length + actually_processed_pixels - offset
         
          if remaining_color_length>1:
            remaining_color=f"{remaining_color_length}{char}"
            actually_processed_pixels+=currnet_length
            b_actually_processed_pixels=actually_processed_pixels
            b_remaining_color=remaining_color,
            b_pos = i+1
            fill_up=False
          else:
            b_actually_processed_pixels=actually_processed_pixels
            b_remaining_color=""
            b_pos = i+1
            fill_up=False
          breached=True

          UP_string.append(actual_string)
          actual_string = str(offset)+"X"

        actually_processed_pixels+=currnet_length



        if len(actual_color)+len(actual_string)<=MAXLENGTH:
          if remaining_color:
            actual_string+=remaining_color
            remaining_color=""
          else:
            actual_string+=actual_color
          actual_color=""
        else:
          if fill_up:
            UP_string.append(actual_string)
          else:
            DOWN_string.append(actual_string)
          actual_string=actual_color

           
    # Return the numbers and characters lists
    if fill_up:
      UP_string.append(actual_string)
    else:
      DOWN_string.append(actual_string)
      
    return b_actually_processed_pixels, b_remaining_color, b_pos, False, UP_string, DOWN_string


image_width = IMAGE_WIDTH
offset_lines=OFFSET

try:
  with open("image_data.txt", "r") as f:
    all_lines = ""
    try:
        for line in f:
          all_lines += line.rstrip()
    except EOFError:
        pass

  actually_processed_pixels = 0
  actually_processed_pixels,remaining_color, char_pos, done, UP_string, DOWN_string = process_line(all_lines,image_width,offset_lines,actually_processed_pixels)


  with open('image_data_UP.txt', 'w') as f:
      for i in range(len(UP_string)):
        if i<(len(UP_string)-1):
          newline=UP_string[i]
          f.write(f"{newline}\n")
        else:
          newline=UP_string[i]
          f.write(f"{newline}")


  with open('image_data_DOWN.txt', 'w') as f:
      for i in range(len(DOWN_string)):
        if i<(len(DOWN_string)-1):
          newline=DOWN_string[i]
          f.write(f"{newline}\n")
        else:
          newline=DOWN_string[i]
          f.write(f"{newline}")
except FileNotFoundError:
  print("ERROR: Unable to open image_data.txt")
  input("\nPress ENTER to continue")
except Exception:
  traceback.print_exc()
  input("\n\nPress ENTER to continue")
