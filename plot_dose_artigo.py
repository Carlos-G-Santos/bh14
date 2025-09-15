import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LogNorm
from PIL import Image


'''
Input Data: Write ZOOM equals to YES/yes to select a specific region to be ploted or NO/no to plot the intere area
described in the FMESH file. Values of x_min_real, x_max_real, y_max_real and y_max_real describe the range of the
selected area for plotting.
'''
ZOOM="yes"
''' O valor do cut_value é baseado nos valores que estão na lista de valores '''
cut_value=0.5
''' Os valores para o zoom são baseados nos valores apresentados no cabeçalho '''
y_min_real=-65.0
y_max_real=-20.0
z_min_real=410.60
z_max_real=460.10


with open("loki_41_mesh", 'r') as file:
    lines = file.readlines()
    
for i in range(len(lines)):
    if "Mesh Tally Number" in lines[i]:
        tally_location = i
        break

x_value=[]

x_length = lines[tally_location+4].split()
x_length = x_length[2:]
for j in range(len(x_length)-1):
#    print(j)
    x_m=(float(x_length[j])+float(x_length[j+1]))/2
    x_value.append(x_m)
    

y_length = lines[tally_location+5].split()
y_length = y_length[2:]

z_length = lines[tally_location+6].split()
z_length = z_length[2:]

start = tally_location+10
end = start+((len(x_length)-1) * (len(y_length)-1) * (len(z_length)-1))
x_origin = len(x_length)/2
y_origin = len(y_length)/2
z_origin = len(z_length)/2
tally_data = lines[start:end]

if ZOOM=="NO" or ZOOM=="no":
     x_min=float(x_length[0])
     x_max=float(x_length[len(x_length)-1])
     y_min=float(y_length[0])
     y_max=float(y_length[len(y_length)-1])
     z_min=float(z_length[0])
     z_max=float(z_length[len(z_length)-1])
     values = []
     for line in tally_data:
         if float(line.split()[0])==cut_value:
             flux = line.split()[3]
             flux = 2.3*10**12*float(flux)

             variance = line.split()[4]
             variance = float(variance)
         
             if variance > 1. or flux == 0:
                 values.append(np.nan)
             else:
                 values.append(flux)
     values = np.array(values)
     values = np.reshape(values, (len(y_length)-1, len(z_length)-1))
 #    print(len(values))            
else:
     x_min=float(x_length[0])
     x_max=float(x_length[len(x_length)-1])
     y_min=float(y_length[0])
     y_max=float(y_length[len(y_length)-1])
     z_min=float(z_length[0])
     z_max=float(z_length[len(z_length)-1])
     values = []
     for line in tally_data:
         if float(line.split()[0])==cut_value:
             flux = line.split()[3]
             flux = 2.3*10**12*float(flux)

             variance = line.split()[4]
             variance = float(variance)
         
             if variance > 1. or flux == 0:
                 values.append(np.nan)
             else:
                 values.append(flux)
     values = np.array(values)
     values = np.reshape(values, (len(y_length)-1, len(z_length)-1))
        
     y_min_aux=y_min_real
     y_max_aux=y_max_real
     z_min_aux=z_min_real
     z_max_aux=z_max_real     
     
     w=0
     v=0
     for v in range(len(y_length)):
         if float(y_length[v])==y_min_aux:
            v_min=v  
         if float(y_length[v])==y_max_aux:
            v_max=v         
     if (v_max+v_min)//2!=0:
         v_max+=1
         y_max=float(y_length[v_max])
     for w in range(len(z_length)):         
         print(z_length[w])
         print(w)
         if float(z_length[w])==z_min_aux:
            w_min=len(z_length)-w
            print(z_length[w])
         if float(z_length[w])==z_max_aux:
            w_max=len(z_length)-w            
     if (w_max+w_min)//2!=0:
         w_max+=1
         z_max=float(z_length[w_max])
     cntr_x=int((v_max+v_min)/2)        
     cntr_z=int((w_max+w_min)/2)
     delta_x=int(x_origin-cntr_x)
     delta_z=int(z_origin-cntr_z)             
             


# values = values[::-1]
for i in range(len(values)):
    values[i] = values[i][::-1]
    
values = np.transpose(values)
if ZOOM=="YES" or ZOOM=="yes":
#   for i in range(len(values)):
#       values[i] = values[i][::-1]
   values=values[w_max:w_min,v_min:v_max]
#values=values[v_max:v_min,u_max:u_min]

def alpha_proc(img):
    '''
    Process alpha (transparency) data for outline images to overlay on 
    flux and ratio maps.
    '''
    
    alphas = np.zeros((len(img),len(img[0])))
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] > 200:
                # If the pixel is at least nearly white, make the pixel fully transparent
                alphas[i][j] = 0
            else:
                # If the part of the picture is black, make the pixel slightly transparent
                alphas[i][j] = 1
    return alphas 

def get_outlines(file):
    '''
    Pull outline data from PNG's.
    Pull one of the color values from the images (0, 1, or 2) to indicate that
        that region is black and should not be transparent.
    '''
    image = Image.open(file)
    image= np.array(image)
    Ly_img=len(image[0])
    Lz_img=len(image)
    if ZOOM=="YES" or ZOOM=="yes":
       image=image[w_max*Lz_img//len(z_length):w_min*Lz_img//len(z_length),v_min*Ly_img//len(y_length):v_max*Ly_img//len(y_length)]
    image = image[:,:,1]
    alphas = alpha_proc(image)
    
    return image, alphas

if ZOOM=="NO" or ZOOM=="no":
     x_min_real=x_min
     x_max_real=x_max
     y_min_real=y_min
     y_max_real=y_max
     z_min_real=z_min
     z_max_real=z_max
    
def show_outline(outline):
    '''
    Show the outline with the appropriate aplha(transparency) values
    '''
    
    plt.imshow(outline[0], cmap="gray", alpha=outline[1
                                                      ], extent = [y_min_real,y_max_real,z_min_real,z_max_real])

frame = get_outlines("loki41.PNG")

colormap = mpl.colormaps['jet'].copy()
colormap.set_bad(color="white")

plt.imshow(values,extent = [y_min_real,y_max_real,z_min_real,z_max_real], cmap=colormap, norm = LogNorm(vmin = np.nanmin(values), 
                                          vmax = np.nanmax(values)))

cb = plt.colorbar()
cb.ax.set_ylabel("Dose (Sv/h)")
cb.set_label('Dose (Sv/h)', fontsize=12, labelpad=15)
plt.xlabel('Y Position (cm)', fontsize=12, labelpad=10)
plt.ylabel('Z Position (cm)', fontsize=12, labelpad=10)
#plt.title('Dose Distribution', fontsize=14, pad=20)
#plt.xticks([-50,30.48],["~ 1 ft from door", "Source"])
#plt.yticks([])
show_outline(frame)
plt.show()
#print(x_length)
