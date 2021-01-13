import cv2

def divider(a):
    if (a % 10 != 0):
        return 10 - (a % 10)
    return 0

# Input image
input = cv2.imread('yoshi2.jpg',0)
dimensions = input.shape
yvalue = input.shape[0]
xvalue = input.shape[1]
ypadding = divider(yvalue)
xpadding = divider(xvalue)
# Get input size
height, width = input.shape[:2]

pixelsize = 5

# Desired "pixelated" size
w, h = (((yvalue + ypadding) // pixelsize), ((xvalue + xpadding) // pixelsize))

print(type(w))
print(type(h))
# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)


for i in range(yvalue):
  for j in range(xvalue):  
    if(output[i,j] >= 0 and output[i,j] < 21):
       output[i,j] = 10
    if(output[i,j] >= 21 and output[i,j] < 42):
       output[i,j] = 31
    if(output[i,j] >= 42 and output[i,j] < 63):
       output[i,j] = 52
    if(output[i,j] >= 63 and output[i,j] < 84):
       output[i,j] = 73
    if(output[i,j] >= 84 and output[i,j] < 105):
       output[i,j] = 94
    if(output[i,j] >= 105 and output[i,j] < 126):
       output[i,j] = 115
    if(output[i,j] >= 126 and output[i,j] < 147):
       output[i,j] = 136
    if(output[i,j] >= 147 and output[i,j] < 168):
       output[i,j] = 157
    if(output[i,j] >= 168 and output[i,j] < 189):
       output[i,j] = 178
    if(output[i,j] >= 189 and output[i,j] < 210):
       output[i,j] = 199
    if(output[i,j] >= 210 and output[i,j] < 231):
       output[i,j] = 220
    if(output[i,j] >= 231 and output[i,j] < 255):
       output[i,j] = 243
    if(output[i, j] == 255):
        output[i, j] = 255


strs = ["" for x in range((yvalue + ypadding) // pixelsize)]

for i in range(0, yvalue, pixelsize):
    for j in range(0, xvalue, pixelsize):
        if(output[i, j] == pixelsize):
            strs[i// pixelsize] +="@@"
        if(output[i, j] == 31):
            strs[i// pixelsize] +="$$"
        if(output[i, j] == 52):
            strs[i// pixelsize] +="##"
        if(output[i, j] == 73):
            strs[i// pixelsize] +="**"
        if(output[i, j] == 94):
            strs[i// pixelsize] +="!!"
        if(output[i, j] == 115):
            strs[i// pixelsize] +="=="
        if(output[i, j] == 136):
            strs[i// pixelsize] +=";;"
        if(output[i, j] == 157):
            strs[i// pixelsize] +="::"
        if(output[i, j] == 178):
            strs[i// pixelsize] +="~~"
        if(output[i, j] == 199):
            strs[i// pixelsize] +="--"
        if(output[i, j] == 220):
            strs[i// pixelsize] +=",,"
        if(output[i, j] == 243):
            strs[i// pixelsize] +=".."
        if(output[i, j] == 255):
            strs[i// pixelsize] +="  "

for line in strs:
    print (line)
# cv2.imshow("cropped", input)

cv2.imshow('Output', output)
image = cv2.copyMakeBorder(input, 0, ypadding, 0, xpadding, cv2.BORDER_CONSTANT, None, 255)
cv2.imshow('border', image)

print (strs)
print (yvalue + divider(yvalue))
print (xvalue + divider(xvalue))

cv2.waitKey(0)