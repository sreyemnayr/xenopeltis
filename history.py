layer_arrays = []
sizes = {}
colors = {}
bg_mask = None
background = None
eyes = None

for layer in layers:
    img = Image.open(f"LAYERS/{layer}")
    img_arr = np.array(img)
    reshaped = img_arr.reshape(-1,4)
    alpha = reshaped.flatten()[3::4]
    ralpha = alpha.reshape(5000,5000)
    mask = (ralpha > 0)
    stuff = img_arr[mask]

    if layer == "BACKGROUND.png":
        background = img_arr
        bg_mask = mask
    elif layer == "EYEWHITES.png":
        eyes = Image.fromarray(img_arr)
    else:
        layer_arrays.append({"array": img_arr, "mask": mask})
    
    #size = (np.count_nonzero(img_arr.flatten()[3::4]) / (len(img_arr)*len(img_arr[0])))*100
    size = len(stuff) / len(alpha) * 100
    sizes[layer] = size
    colors[layer] = np.mean(stuff, axis=0)
    print(layer, sizes[layer], colors[layer])
len(bg_mask)
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg)
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c = cm(i%colors/(colors+1))
        print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1.0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg)
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c = cm(i%colors/(colors+1))
        print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.save(fn)
create_series("PuOr_new")
64%1
64%2
32%2
32%3
32%4
0%1
ls
import numpy as np
import palettable
import matplotlib
from PIL import Image, ImageOps, ImageChops, ImageStat
layers = os.listdir("LAYERS")
import os
layers = os.listdir("LAYERS")
cm = palettable.colorbrewer.diverging.PuOr_11.mpl_colormap.resampled(64)
layer_arrays = []
sizes = {}
colors = {}
bg_mask = None
background = None
eyes = None

for layer in layers:
    img = Image.open(f"LAYERS/{layer}")
    img_arr = np.array(img)
    reshaped = img_arr.reshape(-1,4)
    alpha = reshaped.flatten()[3::4]
    ralpha = alpha.reshape(5000,5000)
    mask = (ralpha > 0)
    stuff = img_arr[mask]
    size = len(stuff) / len(alpha) * 100

    if layer == "BACKGROUND.png":
        background = img_arr
        bg_mask = mask
    elif layer == "EYEWHITES.png":
        eyes = Image.fromarray(img_arr)
    else:
        layer_arrays.append({"array": img_arr, "mask": mask, "size": size})
    
    #size = (np.count_nonzero(img_arr.flatten()[3::4]) / (len(img_arr)*len(img_arr[0])))*100
    #size = len(stuff) / len(alpha) * 100
    sizes[layer] = size
    colors[layer] = np.mean(stuff, axis=0)
    print(layer, sizes[layer], colors[layer])
len(layer_arrays)
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(1)
        else:
            c = cm(i%colors/(colors+1))
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.save(fn)
def create_series(prefix="test"):
    create(64, f"{prefix}_64.png")
    create(32, f"{prefix}_32.png")
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(4, f"{prefix}_4.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
cm = palettable.colorbrewer.diverging.PuOr_11.mpl_colormap.resampled(64)
create_series("PuOr_new")
import os
import matplotlib
import palettable
import numpy as np
from PIL import Image, ImageOps, ImageChops, ImageStat
layers = os.listdir("LAYERS")
layer_arrays = []
sizes = {}
colors = {}
bg_mask = None
background = None
eyes = None

for layer in layers:
    img = Image.open(f"LAYERS/{layer}")
    img_arr = np.array(img)
    reshaped = img_arr.reshape(-1,4)
    alpha = reshaped.flatten()[3::4]
    ralpha = alpha.reshape(5000,5000)
    mask = (ralpha > 0)
    stuff = img_arr[mask]
    size = len(stuff) / len(alpha) * 100

    if layer == "BACKGROUND.png":
        background = img_arr
        bg_mask = mask
    elif layer == "EYEWHITES.png":
        eyes = Image.fromarray(img_arr)
    else:
        layer_arrays.append({"array": img_arr, "mask": mask, "size": size})
    
    #size = (np.count_nonzero(img_arr.flatten()[3::4]) / (len(img_arr)*len(img_arr[0])))*100
    #size = len(stuff) / len(alpha) * 100
    sizes[layer] = size
    colors[layer] = np.mean(stuff, axis=0)
    print(layer, sizes[layer], colors[layer])
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(1)
        else:
            c = cm(i%colors/(colors+1))
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.save(fn)
def create_series(prefix="test"):
    create(64, f"{prefix}_64.png")
    create(32, f"{prefix}_32.png")
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(4, f"{prefix}_4.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
cm = palettable.colorbrewer.diverging.PuOr_4.mpl_colormap.resampled(64)
create_series("PuOr_new")
import os
import matplotlib
import palettable
import numpy as np
from PIL import Image, ImageOps, ImageChops, ImageStat
layers = os.listdir("LAYERS")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(1)
        else:
            c = cm(i%colors/(colors+1))
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
def create_series(prefix="test"):
    create(64, f"{prefix}_64.png")
    create(32, f"{prefix}_32.png")
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(4, f"{prefix}_4.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
cm = palettable.colorbrewer.diverging.PuOr_4.mpl_colormap.resampled(64)
layer_arrays = []
sizes = {}
colors = {}
bg_mask = None
background = None
eyes = None

for layer in layers:
    img = Image.open(f"LAYERS/{layer}")
    img_arr = np.array(img)
    reshaped = img_arr.reshape(-1,4)
    alpha = reshaped.flatten()[3::4]
    ralpha = alpha.reshape(5000,5000)
    mask = (ralpha > 0)
    stuff = img_arr[mask]
    size = len(stuff) / len(alpha) * 100

    if layer == "BACKGROUND.png":
        background = img_arr
        bg_mask = mask
    elif layer == "EYEWHITES.png":
        eyes = Image.fromarray(img_arr)
    else:
        layer_arrays.append({"array": img_arr, "mask": mask, "size": size})
    
    #size = (np.count_nonzero(img_arr.flatten()[3::4]) / (len(img_arr)*len(img_arr[0])))*100
    #size = len(stuff) / len(alpha) * 100
    sizes[layer] = size
    colors[layer] = np.mean(stuff, axis=0)
    print(layer, sizes[layer], colors[layer])
%save current_session ~0/
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(1)
        else:
            c = cm(i%colors-1/(colors+1))
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(1)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(1)
        else:
            c = cm(i%(colors-1)/(colors+1))
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        colors_to_use.append(cm((i+1)/colors))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c = colors_to_use[colors%(i+1)]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
len(colors_to_use)
32%1
32%2
32%3
round(32/3)
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        colors_to_use.append(cm((i+1)/colors))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c = colors_to_use[round(colors/(i+1))-1]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        colors_to_use.append(cm((1/colors)*(i+1)))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c = colors_to_use[round(colors/(i+1))-1]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round(colors/(i+1))-1
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round(len(layer_arrays)/colors)*(i+1)
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round(len(layer_arrays)/colors)*i
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round((i/len(layer_arrays))*colors)
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round(((i/len(layer_arrays))*colors)-1)
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
round(((32/64)*32)-1)
round(((0/64)*32)-1)
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        else:
            c_idx = round((((i+1)/len(layer_arrays))*colors)-1)
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
round((((0+1)/64)*32)-1)
round((((32+1)/64)*32)-1)
round((((31+1)/64)*32)-1)
create_series("PuOr_new")
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        if colors == 2:
            c = cm(1)
        else:
            c_idx = round(((i/len(layer_arrays))*colors))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        if colors == 2:
            c = cm(1)
        else:
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create_series("PuOr_new")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        elif colors == 2:
            c = cm(1)
        else:
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create(2,"PuOr_new_2.png")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1)
        else:
            print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create(2,"PuOr_new_2.png")
cm(0)
cm(1)
bg_color
bg_color = None
create(2,"PuOr_new_2.png")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1)
            print(bg_color, c)
        else:
            print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create(2,"PuOr_new_2.png")
cm(1)
cm(0)
cm(0.1)
cm(0.9)
cm(1.0)
cm(1)
cm(0.0)
cm(0)
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
create(2,"PuOr_new_2.png")
create(1,"PuOr_new_1.png")
cm = palettable.colorbrewer.diverging.PuOr_4_r.mpl_colormap.resampled(64)
create_series("PuOr_reverse_new")
cm = palettable.colorbrewer.diverging.Spectral_10.mpl_colormap.resampled(64)
create_series("Spectral10")
cm = palettable.wesanderson.Royal3_5.mpl_colormap.resampled(64)
create_series("Royals")
cm = palettable.scientific.sequential.Devon_20.mpl_colormap.resampled(64)
create_series("Devon")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
cm = palettable.scientific.sequential.Buda_20.mpl_colormap.resampled(64)
create_series("Buda")
cm = palettable.matplotlib.Plasma_20.mpl_colormap.resampled(64)
create_series("Plasma")
cm = palettable.lightbartlein.diverging.BlueOrangeRed_4.mpl_colormap.resampled(64)
create_series("BlueOrangeRed")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create(64, "BlueOrangeRed_64_2.png")
create(32, "BlueOrangeRed_32_2.png")
create(8, "BlueOrangeRed_8_2.png")
l = [1,2,3,4,5,6]
l[3:-3]
l[-3:3]
l
l[:-3]
l[::-3]
l[3:]+l[0:3]
l[6:]+l[:6]
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create_series("BlueOrangeRed")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    for i, layer in enumerate(layer_arrays.sorted(key=lambda x: x.get('size'))):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create_series("BlueOrangeRed_lambda")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    for i, layer in enumerate(sorted(layer_arrays, key=lambda x: x.get('size'))):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create_series("BlueOrangeRed_lambda")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    for i, layer in enumerate(sorted(layer_arrays[colors:]+layer_arrays[:colors], key=lambda x: x.get('size'))):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create_series("BlueOrangeRed_lambda_slice")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    sorted_layers = sorted(layer_arrays, key=lambda x: x.get('size'))
    layers_to_use = sorted_layers[::4]+sorted_layers[1::4]+sorted_layers[2::4]+sorted_layers[3::4]
    for i, layer in enumerate(layers_to_use[colors:]+layers_to_use[:colors]):
        
        if colors == 1:
            print("Colors is 1")
            c = cm(0)
        elif colors == 2:
            print("Colors is 2")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create_series("BlueOrangeRed_lambda_slice")
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    sorted_layers = sorted(layer_arrays, key=lambda x: x.get('size'))
    layers_to_use = sorted_layers[::4]+sorted_layers[1::4]+sorted_layers[2::4]+sorted_layers[3::4]
    for i, layer in enumerate(layers_to_use[colors:]+layers_to_use[:colors]):
        
        if colors == 0:
            #print("Colors is 1")
            c = cm(0)
        elif colors == 1:
            print("Colors is 1")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
create(0, "BlueOrangeRed_lambda_slice.png")
create(2, "BlueOrangeRed_lambda_slice_2.png")
create(1, "BlueOrangeRed_lambda_slice_1.png")
#cm = palettable. .mpl_colormap.resampled(64)
def create_series(prefix="test"):
    create(64, f"{prefix}_64.png")
    create(32, f"{prefix}_32.png")
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(4, f"{prefix}_4.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
    create(0, f"{prefix}_0.png")
cm = palettable.wesanderson.FantasticFox1_5.mpl_colormap.resampled(64)
create_series("Fox")
cm = palettable.cubehelix.cubehelix3_16.mpl_colormap.resampled(64)
create_series("CubeHelix316")
cm = palettable.colorbrewer.diverging.PiYG_11.mpl_colormap.resampled(64)
create_series("PiYG")
cm = palettable.cmocean.sequential.Thermal_20.mpl_colormap.resampled(64)
create_series("Thermal")
cm = palettable.cmocean.sequential.Thermal_20.mpl_colormap
create_series("Thermal_noremap")
def create_short_series(prefix="test"):
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(7, f"{prefix}_7.png")
    create(6, f"{prefix}_6.png")
    create(5, f"{prefix}_5.png")
    create(4, f"{prefix}_4.png")
    create(3, f"{prefix}_3.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
    create(0, f"{prefix}_0.png")
create_short_series("Thermal_short")
palettable.cmocean.sequential.Thermal_20.colors
palettable.utils.make_name_map()
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    img = Image.fromarray(bg, mode="RGBA")
    image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    for i, layer in enumerate(layer_arrays):
        
        if colors == 1:
            c = cm(0)
        if colors == 2:
            c = cm(1)
        else:
            c_idx = round(((i/len(layer_arrays))*colors))
            print("Color index", c_idx)
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    print(f"Saving {fn}")
    image.save(fn)
%save create ~126/
help %save
help save
%save?
%save create 126
def create_short_series(prefix="test"):
    create(16, f"{prefix}_16.png")
    create(8, f"{prefix}_8.png")
    create(7, f"{prefix}_7.png")
    create(6, f"{prefix}_6.png")
    create(5, f"{prefix}_5.png")
    create(4, f"{prefix}_4.png")
    create(3, f"{prefix}_3.png")
    create(2, f"{prefix}_2.png")
    create(1, f"{prefix}_1.png")
    create(0, f"{prefix}_0.png")
%save create_short 132
from math import floor
def create(colors=64, fn="Test.png"):
    
    image = Image.new("RGBA", (5000,5000), (0,0,0,255))
    bg_color = cm(0)
    print("Background color", bg_color)
    bg = background.copy()
    bg[bg_mask] = (bg_color[0]*255, bg_color[1]*255, bg_color[2]*255, 255)
    #img = Image.fromarray(bg, mode="RGBA")
    #image.alpha_composite(img)
    
    colors_to_use = []
    for i in range(0,colors):
        idx = (1/colors) * (i+1)
        print("Using index", idx)
        colors_to_use.append(cm(idx))
        
    #for i, layer in enumerate(layer_arrays[colors:]+layer_arrays[:colors]):
    sorted_layers = sorted(layer_arrays, key=lambda x: x.get('size'))
    layers_to_use = sorted_layers[::4]+sorted_layers[1::4]+sorted_layers[2::4]+sorted_layers[3::4]
    for i, layer in enumerate(layers_to_use[colors:]+layers_to_use[:colors]):
        
        if colors == 0:
            #print("Colors is 1")
            c = cm(0)
        elif colors == 1:
            print("Colors is 1")
            c = cm(1.0)
            print(bg_color, c)
        else:
            #print("Colors is not 1 or 2")
            c_idx = floor((colors)*(i/len(layer_arrays)))
            print("Color index", c_idx, colors_to_use[c_idx])
            c = colors_to_use[c_idx]
        #print("Color", c)

        layer["array"][layer["mask"]] = (c[0]*255, c[1]*255, c[2]*255, 255)
    
        img = Image.fromarray(layer["array"], mode="RGBA")
        image.alpha_composite(img)
    image.alpha_composite(eyes)
    image.alpha_composite(Image.fromarray(bg, mode="RGBA"))
    print(f"Saving {fn}")
    image.save(fn)
%save create 134
%save session ~0/
cm.colors
cm.colors()
cm.colorbar_extend
cm.with_extremes()
cm.N
cm = palettable.cmocean.sequential.Thermal_20.mpl_colormap
cm.N
cm.colors
tumblrs = os.listdir("palettes/moviesincolor/gallery-dl/tumblr/moviesincolor/")
import json
import requests
def iframely_url(url):
    sections = url.split("_")
    uid = sections[2]
    return f"https://iframely.com/api/try?url=https://moviesincolor.com/post/{uid}"
iframely_url("tumblr_moviesincolor_47879985218_01.jpg")
r = requests.get(iframely_url("tumblr_moviesincolor_47879985218_01.jpg"))
r
r.json()
r.json().title
r.json()['title']
done = []
for img in tumblrs:
    r = requests.get(iframely_url(img))
    with open(f"palettes/moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
        json.dump(r.json(), f, indent=2)
    done.append(img)
r.status_code
import time
done = []
matches = {}
for img in tumblrs:
    if img not in done:
        r = requests.get(iframely_url(img))
        if r.status_code == 200:
            j = r.json()
            matches[img] = j.get("title", j.get("url", "unknown"))
            with open(f"palettes/moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
                json.dump(j, f, indent=2)
            done.append(img)
        else:
            print("sleeping")
            time.sleep(5)
done = []
matches = {}
for img in tumblrs:
    if img not in done:
        r = requests.get(iframely_url(img))
        if r.status_code == 200:
            j = r.json()
            if not j.get("error", False):
                matches[img] = j.get("title", j.get("url", "unknown"))
                with open(f"palettes/moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
                    json.dump(j, f, indent=2)
                done.append(img)
            else:
                print("sleeping")
                time.sleep(5)
#done = []
matches = {}
for img in tumblrs:
    if img not in done:
        print(img)
        time.sleep(1)
        r = requests.get(iframely_url(img))
        if r.status_code == 200:
            j = r.json()
            if not j.get("error", False):
                matches[img] = j.get("title", j.get("url", "unknown"))
                with open(f"palettes/moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
                    json.dump(j, f, indent=2)
                done.append(img)
            else:
                print("sleeping 5")
                time.sleep(5)
len(matches)
with open("palettes/moviesincolor/matches.json", "w") as f:
    json.dump(matches, f, indent=2)
matches["tumblr_moviesincolor_145269683743_01.jpg"]
iframely_url("tumblr_moviesincolor_145269683743_01.jpg")
iframely_url("tumblr_moviesincolor_98570681908_01.jpg")
iframely_url("tumblr_moviesincolor_91215621233_01.png")
with open("palettes/moviesincolor/matches.json", "r") as f:
    new_matches = json.load(f)
new_matches("tumblr_moviesincolor_95924181593_01.jpg")
new_matches.get"tumblr_moviesincolor_95924181593_01.jpg")
new_matches.get("tumblr_moviesincolor_95924181593_01.jpg")
new_matches
def mic_url(url):
    sections = url.split("_")
    uid = sections[2]
    return f"https://moviesincolor.com/post/{uid}"
palettes = []
for fn, movie in new_matches.items():
    palettes.append({"img": fn, "source": "Movies in Color", "source_url": mic_url(fn), "inspiration": movie})
from PIL import Image, ImageOps, ImageChops, ImageStat
pwd
cd palettes/
(875,528) == (875,528)
set([(875,528), (875,528)])
hw = set()
for p in palettes:
    img = Image.open(f"img/{p['img']}")
    p['img_obj'] = img.copy()
    hw.add(img.size)
hw
len(palettes)
len(new_matches)
len(matches)
from collections import Counter
len(tumblrs)
len(done)
tumblrs[0]
done = []
done = [m for m in matches.keys()]
len(done)
#done = []
matches = {}
for img in tumblrs:
    if img not in done:
        print(img)
        time.sleep(1)
        r = requests.get(iframely_url(img))
        if r.status_code == 200:
            j = r.json()
            if not j.get("error", False):
                matches[img] = j.get("title", j.get("url", "unknown"))
                with open(f"palettes/moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
                    json.dump(j, f, indent=2)
                done.append(img)
            else:
                print("sleeping 5")
                time.sleep(5)
#done = []
matches = {}
for img in tumblrs:
    if img not in done:
        print(img)
        time.sleep(1)
        r = requests.get(iframely_url(img))
        if r.status_code == 200:
            j = r.json()
            if not j.get("error", False):
                matches[img] = j.get("title", j.get("url", "unknown"))
                with open(f"moviesincolor/json/{img}".replace(".jpg",".json"), "w") as f:
                    json.dump(j, f, indent=2)
                done.append(img)
            else:
                print("sleeping 5")
                time.sleep(5)
with open("palettes/moviesincolor/more_matches.json", "w") as f:
    json.dump(matches, f, indent=2)
with open("moviesincolor/more_matches.json", "w") as f:
    
    json.dump(matches, f, indent=2)
more_matches = {
  "tumblr_moviesincolor_59805636610_01.jpg": "Small Time Crooks (2000)",
  "tumblr_moviesincolor_79685885824_01.jpg": "Where the Wild Things Are (2009)",
  "tumblr_moviesincolor_98982294618_01.jpg": "Guts - The Walking Dead: Season 1, Episode 2 (2010)",
  "tumblr_moviesincolor_56531835074_01.jpg": "Be Kind Rewind (2008)",
  "tumblr_moviesincolor_92102417308_01.jpg": "Sin City (2005)",
  "tumblr_moviesincolor_87745814103_01.jpg": "Dirty Rotten Scoundrels (1988)",
  "tumblr_moviesincolor_49702395910_01.jpg": "Delicatessen (1991)",
  "tumblr_moviesincolor_61513276335_01.jpg": "Blazing Saddles (1974)",
  "tumblr_moviesincolor_58073313789_01.jpg": "Super 8 (2011)",
  "tumblr_moviesincolor_72806846464_01.jpg": "The New World (2005)",
  "tumblr_moviesincolor_53772008365_01.jpg": "The Skin I Live In (2011)",
  "tumblr_moviesincolor_66696589440_01.jpg": "Weird Science (1985)",
  "tumblr_moviesincolor_55100022448_01.jpg": "Hellboy (2004)",
  "tumblr_moviesincolor_56160342959_01.jpg": "Mulholland Dr. (2001)",
  "tumblr_moviesincolor_58449654032_01.jpg": "Alice in Wonderland (2010)",
  "tumblr_moviesincolor_60299094620_01.jpg": "Moulin Rouge (2001)",
  "tumblr_moviesincolor_51816064160_01.jpg": "Inception (2010)",
  "tumblr_moviesincolor_66795356883_01.jpg": "Eastern Promises (2007)",
  "tumblr_moviesincolor_59504560331_01.jpg": "Annie Hall (1977)",
  "tumblr_moviesincolor_93063666183_01.jpg": "RocknRolla (2008)",
  "tumblr_moviesincolor_93710138108_01.jpg": "Sherlock Holmes: A Game of Shadows (2011)",
  "tumblr_moviesincolor_80185061722_01.jpg": "Mean Girls (2004)"
}
for fn, movie in more_matches.items():
    palettes.append({"img": fn, "source": "Movies in Color", "source_url": mic_url(fn), "inspiration": movie})
len(palettes)
hw = set()
for p in palettes:
    if not p.get('img_obj', None):
        img = Image.open(f"img/{p['img']}")
        p['img_obj'] = img.copy()
        hw.add(img.size)
hw
for p in palettes:
    hw.add(p['img_obj'].size)
hw
hws = []
for p in palettes:
    hws.append(p['img_obj'].size)
len(hws)
Counter(hws)
lmd_y = 414
x = 37
gs_y = 488
def get_palette(img):
    upper = []
    lower = []
    for i in range(1,24):
        upper.append(img.getpixel((lmd_y, i*37)))
        lower.append(img.getpixel((gs_y, i*37)))
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
get_palette(palettes[0]['img_obj'])
def get_palette(img):
    upper = []
    lower = []
    for i in range(1,23):
        upper.append(img.getpixel((lmd_y, i*37)))
        lower.append(img.getpixel((gs_y, i*37)))
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
get_palette(palettes[0]['img_obj'])
def get_palette(img):
    upper = []
    lower = []
    for i in range(1,24):
        upper.append(img.getpixel((i*37, lmd_y)))
        lower.append(img.getpixel((i*37, gs_y)))
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
get_palette(palettes[0]['img_obj'])
p = get_palette(palettes[0]['img_obj'])
len(p[3])
palettes[0]
def get_palette(img):
    upper = []
    lower = []
    for i in range(1,24):
        upper.append(img.getpixel((i*36, lmd_y)))
        lower.append(img.getpixel((i*36, gs_y)))
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
p = get_palette(palettes[0]['img_obj'])
p
#for p in palettes:
#    if p['size'] = hw
hw
for p in palettes:
    if p['size'] == (1280, 772):
        print(p)
for p in palettes:
    if p['img_obj'].size == (1280, 772):
        print(p)
hw
palettes[0]
lmd_y
gs_y
def get_palette(img):
    upper = []
    lower = []
    if img.size == (1280, 772):
        upper_y = 608
        lower_y = 720
        x = 54
    else:
        upper_y = 414
        lower_y = 488
        x = 36
    for i in range(1,24):
        upper.append(img.getpixel((i*x, upper_y)))
        lower.append(img.getpixel((i*x, lower_y)))
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
for p in palettes:
    print(p['inspiration'])
    pal = get_palette(p['img_obj'])
    p['palettes'] = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": pal[3]}
palettes[0]
def get_palette(img):
    upper = []
    lower = []
    if img.size == (1280, 772):
        upper_y = 608
        lower_y = 720
        x = 54
    else:
        upper_y = 414
        lower_y = 488
        x = 36
    for i in range(1,24):
        upper_pixel = img.getpixel((i*x, upper_y))
        upper.append(upper_pixel)
        if(upper_pixel == (255, 255, 255)):
            print(img['img'])
        lower_pixel = img.getpixel((i*x, lower_y))
        lower.append(lower_pixel)
        if(lower_pixel == (255,255,255)):
            print(img['img'])
        
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
for p in palettes:
    #print(p['inspiration'])
    pal = get_palette(p['img_obj'])
    p['palettes'] = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": pal[3]}
def get_palette(img):
    upper = []
    lower = []
    if img.size == (1280, 772):
        upper_y = 608
        lower_y = 720
        x = 54
    else:
        upper_y = 414
        lower_y = 488
        x = 36
    for i in range(1,24):
        upper_pixel = img.getpixel((i*x, upper_y))
        upper.append(upper_pixel)
        if(upper_pixel == (255, 255, 255)):
            print("DANGER")
        lower_pixel = img.getpixel((i*x, lower_y))
        lower.append(lower_pixel)
        if(lower_pixel == (255,255,255)):
            print("DANGER")
        
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
for p in palettes:
    print(p['img'])
    pal = get_palette(p['img_obj'])
    p['palettes'] = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": pal[3]}
def get_palette(img):
    upper = []
    lower = []
    if img.size == (1280, 772):
        upper_y = 608
        lower_y = 720
        x = 54
    else:
        upper_y = 414
        lower_y = 488
        x = 36
    for i in range(1,24):
        upper_pixel = img.getpixel((i*x, upper_y))
        upper.append(upper_pixel)
        lower_pixel = img.getpixel((i*x, lower_y))
        lower.append(lower_pixel)
        
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])
for p in palettes:
    pal = get_palette(p['img_obj'])
    p['palettes'] = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": pal[3]}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
for i, p in enumerate(palettes):
    pal = get_palette(p['img_obj'])
    p['palettes'] = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": pal[3]}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
            print(i)
palettes[335]
p = palettes[335]
p['palettes']['full'] = [pp for pp in p['palettes']['full'] if pp != (255,255,255)]
palettes[335]
import pickle
with open("moviesincolor.pkl", "wb") as f:
    pickle.dump(palettes, f)
from PIL import ImageDraw
def show_key_colors(colorList):
    '''
    Make a long rectangle, composed of the colors
    detailed in colorList, a list of (R, G, B) tuples
    '''
    n = len(colorList)

    im = Image.new('RGBA', (50*n, 50))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw.rectangle([(50*idx, 0), (50*(idx+1), 50*(idx+1))],
                       fill=tuple(color))

    return im
titles = []
titles.count("Ryan")
titles = ["Ryan"]
titles.count("Ryan")
titles = []
for p in palettes:
    
    ct = titles.count(p['inspiration'])
    titles.append(p['inspiration'])
    p['title'] = p['inspiration']
    if ct > 0:
        p['title'] = f"{p['title']} #{ct}"
for p in palettes:
    for name, colors in p['palettes']:
        pal_img = show_key_colors(colors)
        pal_img.save(f"previews/{p['source']}_{p['title']}_{name}.jpg")
for p in palettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save(f"previews/{p['source']}_{p['title']}_{name}.jpg")
colors
def show_key_colors(colorList):
    '''
    Make a long rectangle, composed of the colors
    detailed in colorList, a list of (R, G, B) tuples
    '''
    n = len(colorList)

    im = Image.new('RGB', (50*n, 50))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw.rectangle([(50*idx, 0), (50*(idx+1), 50*(idx+1))],
                       fill=tuple(color))

    return im
for p in palettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save(f"previews/{p['source']}_{p['title']}_{name}.jpg")
palettes[0]
for p in palettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save(f"previews/{p['source']}_{p['title']}_{name}.png".replace(' ',''))
os.walk()
os.walk("./")
done = []
not done
done = [1]
not done
readme = []
for p in sorted(palettes, key=lambda x: x['title']):
    readme.append(f"## {x['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = f"previews/{p['source']}_{p['title']}_{name}.png".replace(' ','')
        readme.append(f"### {name}")
        readme.append(f"![{x['title']}]({fn})")
    readme.append("---")
readme = []
for p in sorted(palettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = f"previews/{p['source']}_{p['title']}_{name}.png".replace(' ','')
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")
len(readme)
with open("moviesincolor.md", "w") as f:
    f.write("\n".join(readme))
import lzma
test = lzma.open("/Users/ryan/Projects/stoics/stoa/palettes/cinema.palettes/2016-10-08_01-07-30_UTC.json.xz").read().decode("utf-8")
test
json.loads(test)
def make_filename(filename):
    keepcharacters = ('(',')','_')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()
for p in palettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save(make_filename(f"previews/{p['source']}_{p['title']}_{name}")+".png")
readme = []
for p in sorted(palettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = make_filename(f"previews/{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")
with open("moviesincolor.md", "w") as f:
    f.write("\n".join(readme))
with open("README.md", "w") as f:
    f.write("\n".join(readme))
for p in palettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save("previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png")
readme = []
for p in sorted(palettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = "previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")
with open("README.md", "w") as f:
    f.write("\n".join(readme))
with open("moviesincolor.md", "w") as f:
    f.write("\n".join(readme))
def get_palette_cp(img):
    upper = []
    #lower = []
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    y = 677
    #    lower_y = 488
    x = 100
    for i in range(1,11):
        pixel = img.getpixel((i*x, y))
        upper.append(upper_pixel)
        #lower_pixel = img.getpixel((i*x, lower_y))
        #lower.append(lower_pixel)
        
    return upper
cps = [fn for fn in os.listdir("palettes/moviesincolor/gallery-dl/tumblr/moviesincolor/") if ".jpg" in fn]
cps = [fn for fn in os.listdir("cinema.palettes") if ".jpg" in fn]
len(cps)
#done = []
matches = {}
for img in cps:
    if img not in done:
        print(img)
        
        #time.sleep(1)
        #r = requests.get(iframely_url(img))
        #if r.status_code == 200:
        #    j = r.json()
        #    if not j.get("error", False):
        #        matches[img] = j.get("title", j.get("url", "unknown"))
        with open(f"cinema.palettes/{img}".replace(".jpg",".txt"), "r") as f:
            txt = f.read()
            matches[img] = txt.split('.')[0]
            #        json.dump(j, f, indent=2)
            done.append(img)
            #else:
            #    print("sleeping 5")
            #    time.sleep(5)
len(done)
len(matches)
#done = []
matches = {}
for img in cps:
    if img not in done:
        #print(img)
        
        #time.sleep(1)
        #r = requests.get(iframely_url(img))
        #if r.status_code == 200:
        #    j = r.json()
        #    if not j.get("error", False):
        #        matches[img] = j.get("title", j.get("url", "unknown"))
        try:
            with open(f"cinema.palettes/{img}".replace(".jpg",".txt"), "r") as f:
                txt = f.read()
                matches[img] = txt.split('.')[0]
                #        json.dump(j, f, indent=2)
                done.append(img)
        except:
            print(f"Problem with {img}")
            #else:
            #    print("sleeping 5")
            #    time.sleep(5)
len(matches)
done = []
matches = {}
for img in cps:
    if img not in done:
        #print(img)
        
        #time.sleep(1)
        #r = requests.get(iframely_url(img))
        #if r.status_code == 200:
        #    j = r.json()
        #    if not j.get("error", False):
        #        matches[img] = j.get("title", j.get("url", "unknown"))
        try:
            with open(f"cinema.palettes/{img}".replace(".jpg",".txt"), "r") as f:
                txt = f.read()
                matches[img] = txt.split('.')[0]
                #        json.dump(j, f, indent=2)
                done.append(img)
        except:
            print(f"Problem with {img}")
            #else:
            #    print("sleeping 5")
            #    time.sleep(5)
len(matches)
len(done)
matches
#cinemapalettes = []
#for fn, movie in new_matches.items():
#    cinemapalettes.append({"img": fn, "source": "cinema.palettes", "source_url": mic_url(fn), "inspiration": movie})
test = lzma.open("/Users/ryan/Projects/stoics/stoa/palettes/cinema.palettes/2016-10-08_01-07-30_UTC.json.xz").read().decode("utf-8")
test
test.keys()
json.loads(test)
j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
#j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
    j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
def get_instagram_url(fn): j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
def get_instagram_url(fn):
    j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
    return f"https://instagram.com/p/{j.get('shortcode')}/"
list(matches.keys())[0]
get_instagram_url(f"cinema.palettes/2017-03-09_03-36-37_UTC.jpg")
j
fn = "cinema.palettes/2017-03-09_03-36-37_UTC.jpg"
#def get_instagram_url(fn):
j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8"))
#    return f"https://instagram.com/p/{j.get('shortcode')}/"
j
j.keys()
j.get('node').keys()
def get_instagram_url(fn):
    j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8")).get('node', {})
    return f"https://instagram.com/p/{j.get('shortcode')}/"
get_instagram_url(f"cinema.palettes/2017-03-09_03-36-37_UTC.jpg")
cinemapalettes = []
for fn, movie in matches.items():
    if movie[-1] != ")":
        print(fn, movie)
    #cinemapalettes.append({"img": fn, "source": "cinema.palettes", "source_url": get_instagram_url(f"cinema.palettes/{fn}"), "inspiration": movie})
cinemapalettes = []
for fn, movie in matches.items():
    if movie[-1] != ")":
        if ")" in movie:
            matches[fn] = movie.split(")")[0] + ")"
        else:
            print(fn, movie)
    #cinemapalettes.append({"img": fn, "source": "cinema.palettes", "source_url": get_instagram_url(f"cinema.palettes/{fn}"), "inspiration": movie})
matches["2016-11-14_09-40-52_UTC.jpg"]
matches["2017-05-29_09-10-45_UTC.jpg"] = "The Man from U.N.C.L.E. (2015)"
matches["2017-01-14_19-35-38_UTC.jpg"] = "Supernatural (TV Series)"
matches["2017-01-14_19-58-28_UTC.jpg"] = "True Blood (TV Series)"
matches["2017-01-14_20-01-52_UTC.jpg"] = "Vampire Diaries (TV Show)"
matches["2021-01-23_02-59-01_UTC.jpg"] = "Bernie Game of Thrones (Meme)"
matches["2021-01-23_03-00-07_UTC.jpg"] = "Sad Keanu and Bernie (Meme)"
matches["2021-01-23_02-57-13_UTC.jpg"] = "Bernie Breakfast Club (Meme)"
cinemapalettes = []
for fn, movie in matches.items():
    if movie[-1] != ")":
        if ")" in movie:
            matches[fn] = movie.split(")")[0] + ")"
        else:
            print(fn, movie)
    #cinemapalettes.append({"img": fn, "source": "cinema.palettes", "source_url": get_instagram_url(f"cinema.palettes/{fn}"), "inspiration": movie})
cinemapalettes = []
for fn, movie in matches.items():
    if movie[-1] != ")":
        if ")" in movie:
            matches[fn] = movie.split(")")[0] + ")"
        else:
            print(fn, movie)
    cinemapalettes.append({"img": fn, "source": "cinema.palettes", "source_url": get_instagram_url(f"cinema.palettes/{fn}"), "inspiration": movie})
hw = set()
for p in cinemapalettes:
    if not p.get('img_obj', None):
        img = Image.open(f"cinema.palettes/{p['img']}")
        p['img_obj'] = img.copy()
        hw.add(img.size)
hw
for p in cinemapalettes:
    hws.append(p['img_obj'].size)
Counter(hws)
hows = []
hws = []
for p in cinemapalettes:
    hws.append(p['img_obj'].size)
Counter(hws)
def get_palette_cp(img):
    upper = []
    #lower = []
    w, h = img.size
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    
    y = 677
    #    lower_y = 488
    x = 100
    for i in range(1,11):
        pixel = img.getpixel((i*x, y))
        upper.append(upper_pixel)
        #lower_pixel = img.getpixel((i*x, lower_y))
        #lower.append(lower_pixel)
        
    return upper
for p in cinemapalettes:
    w, h = p['img_obj'].size
    if h > 776:
        print(p['img'], w)
for p in cinemapalettes:
    w, h = p['img_obj'].size
    if h > 776:
        print(p['img'], h)
def get_palette_cp(img):
    upper = []
    offset = 0
    ncolors = 10
    #lower = []
    w, h = img.size
    y = h - 120
    if h < 900:
        x = 100
    elif h < 1000:
        offset = 0
        x = 115
        ncolors = 9
    else:
        offset = 50
        x = 120
        ncolors = 9
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    #    lower_y = 488
    for i in range(1,ncolors+1):
        pixel = img.getpixel((offset+i*x, y))
        upper.append(upper_pixel)
        #lower_pixel = img.getpixel((i*x, lower_y))
        #lower.append(lower_pixel)
        
    return upper
for i, p in enumerate(cinemapalettes):
    pal = get_palette_cp(p['img_obj'])
    p['palettes'] = {"full": pal}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
            print(i)
def get_palette_cp(img):
    upper = []
    offset = 0
    ncolors = 10
    #lower = []
    w, h = img.size
    y = h - 120
    if h < 900:
        x = 100
    elif h < 1000:
        offset = 0
        x = 115
        ncolors = 9
    else:
        offset = 50
        x = 120
        ncolors = 9
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    #    lower_y = 488
    for i in range(1,ncolors+1):
        pixel = img.getpixel((offset+i*x, y))
        upper.append(pixel)
        #lower_pixel = img.getpixel((i*x, lower_y))
        #lower.append(lower_pixel)
        
    return upper
for i, p in enumerate(cinemapalettes):
    pal = get_palette_cp(p['img_obj'])
    p['palettes'] = {"full": pal}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
            print(i)
def get_palette_cp(img):
    try:
        upper = []
        offset = 0
        ncolors = 10
        #lower = []
        w, h = img.size
        y = h - 120
        if h < 900:
            x = 100
        elif h < 1000:
            offset = 0
            x = 115
            ncolors = 9
        else:
            offset = 50
            x = 120
            ncolors = 9
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    #    lower_y = 488
        for i in range(1,ncolors+1):
            pixel = img.getpixel((offset+i*x, y))
            upper.append(pixel)
            #lower_pixel = img.getpixel((i*x, lower_y))
            #lower.append(lower_pixel)
    except:
        print(f"Problem with {img}")
        
    return upper
for i, p in enumerate(cinemapalettes):
    pal = get_palette_cp(p['img_obj'])
    p['palettes'] = {"full": pal}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
            print(i)
def get_palette_cp(img):
    try:
        upper = []
        offset = 0
        ncolors = 10
        #lower = []
        w, h = img.size
        y = h - 120
        if h < 900:
            x = 100
        elif h < 1000:
            offset = 0
            x = 115
            ncolors = 9
        else:
            offset = -50
            x = 120
            ncolors = 9
    #if img.size == (1280, 772):
    #    upper_y = 608
    #    lower_y = 720
    #    x = 54
    #else:
    #    lower_y = 488
        for i in range(1,ncolors+1):
            pixel = img.getpixel((offset+i*x, y))
            upper.append(pixel)
            #lower_pixel = img.getpixel((i*x, lower_y))
            #lower.append(lower_pixel)
    except:
        print(f"Problem with {img}")
        
    return upper
for i, p in enumerate(cinemapalettes):
    pal = get_palette_cp(p['img_obj'])
    p['palettes'] = {"full": pal}
    for pp in pal:
        if (255, 255, 255) in pp:
            print(p['img'])
            print(i)
for p in cinemapalettes:
    
    ct = titles.count(p['inspiration'])
    titles.append(p['inspiration'])
    p['title'] = p['inspiration']
    if ct > 0:
        p['title'] = f"{p['title']} #{ct}"
palettes[0]
for p in cinemapalettes:
    for name, colors in p['palettes'].items():
        pal_img = show_key_colors(colors)
        pal_img.save("previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png")
readme = []
for p in sorted(cinemapalettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = "previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")
with open("cinemapalettes.md", "w") as f:
    f.write("\n".join(readme))
hws = []
#with open("cinemapalettes.md", "w") as f:
#    f.write("\n".join(readme))
get_instagram_url(f"filmandcolor/2018-09-12_22-41-40_UTC.jpg")
process_folder()
%save last_session ~1/
%save last_session ~2/
%save last_session ~3/
%save last_session ~2/
%save history -l 400
