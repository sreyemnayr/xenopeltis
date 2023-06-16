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



done = []

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

with open("moviesincolor/matches.json", "r") as f:
    matches = json.load(f)

palettes = []
hws = []
titles = []

for fn, movie in matches.items():

    ct = titles.count(movie)
    titles.append(movie)
    title = movie
    if ct > 0:
        title = f"{title} #{ct}"

    img = Image.open(f"img/{fn}")
    pal = get_palette(img)
    img_palettes = {"light": pal[0], "medium": pal[1], "dark": pal[2], "full": [pp for pp in pal[3] if pp != (255,255,255)]}
    for name, colors in img_palettes.items():
        pal_img = show_key_colors(colors)
        pal_img.save("previews/"+make_filename(f"Movies in Color_{title}_{name}")+".png")
    
    hws.append(img.size)

    palettes.append(
        {"img": fn,
         "title": title,
         "source": "Movies in Color",
         "source_url": mic_url(fn),
         "inspiration": movie,
         "img_obj": img.copy(),
         "palettes": img_palettes,

         })

readme = []
for p in sorted(palettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = "previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")

with open("moviesincolor.md", "w") as f:
    f.write("\n".join(readme))


# cinema.palettes

cps = [fn for fn in os.listdir("cinema.palettes") if ".jpg" in fn]
done = []
matches = {}
for img in cps:
    if img not in done:
        try:
            with open(f"cinema.palettes/{img}".replace(".jpg",".txt"), "r") as f:
                txt = f.read()
                matches[img] = txt.split('.')[0]
                done.append(img)
        except:
            print(f"Problem with {img}")

matches["2017-05-29_09-10-45_UTC.jpg"] = "The Man from U.N.C.L.E. (2015)"
matches["2017-01-14_19-35-38_UTC.jpg"] = "Supernatural (TV Series)"
matches["2017-01-14_19-58-28_UTC.jpg"] = "True Blood (TV Series)"
matches["2017-01-14_20-01-52_UTC.jpg"] = "Vampire Diaries (TV Show)"
matches["2021-01-23_02-59-01_UTC.jpg"] = "Bernie Game of Thrones (Meme)"
matches["2021-01-23_03-00-07_UTC.jpg"] = "Sad Keanu and Bernie (Meme)"
matches["2021-01-23_02-57-13_UTC.jpg"] = "Bernie Breakfast Club (Meme)"

cinemapalettes = []
hws = []

for fn, movie in matches.items():
    ct = titles.count(movie)
    titles.append(movie)
    title = movie
    pal = get_palette_cp(img)
    pal_img = show_key_colors(pal)
    pal_img.save("previews/"+make_filename(f"cinema.palettes_{title}_full")+".png")

    if ct > 0:
        title = f"{title} #{ct}"

    img = Image.open(f"cinema.palettes/{fn}")
    hws.append(img.size)
    if movie[-1] != ")":
        if ")" in movie:
            movie = movie.split(")")[0] + ")"
        else:
            print(fn, movie)
    cinemapalettes.append({
        "img": fn,
        "source": "cinema.palettes",
        "source_url": get_instagram_url(f"cinema.palettes/{fn}"),
        "inspiration": movie,
        "img_obj": img.copy(),
        "title": title,
        "palettes": {"full": pal}
        })
    


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


# filmandcolor

cps = [fn for fn in os.listdir("filmandcolor") if ".jpg" in fn]
done = []
matches = {}
for img in cps:
    if img not in done:
        try:
            with open(f"filmandcolor/{img}".replace(".jpg",".txt"), "r") as f:
                txt = f.read()
                matches[img] = txt.split('.')[0]
                done.append(img)
        except:
            print(f"Problem with {img}")


fcpalettes = []
hws = []

for fn, movie in matches.items():
    ct = titles.count(movie)
    titles.append(movie)
    title = movie
    pal = get_palette_fc(img)
    pal_img = show_key_colors(pal)
    pal_img.save("previews/"+make_filename(f"filmandcolor_{title}_full")+".png")

    if ct > 0:
        title = f"{title} #{ct}"

    img = Image.open(f"filmandcolor/{fn}")
    hws.append(img.size)
    if movie[-1] != ")":
        if ")" in movie:
            movie = movie.split(")")[0] + ")"
        else:
            print(fn, movie)
    fcpalettes.append({
        "img": fn,
        "source": "filmandcolor",
        "source_url": get_instagram_url(f"filmandcolor/{fn}"),
        "inspiration": movie,
        "img_obj": img.copy(),
        "title": title,
        "palettes": {"full": pal}
        })
    


readme = []
for p in sorted(fcpalettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = "previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")

with open("filmandcolor.md", "w") as f:
    f.write("\n".join(readme))

# palettemaniac

done = []

with open("palettemaniac/matches.json", "r") as f:
    matches = json.load(f)


pmpalettes = []
hws = []

pmfiles = [f.get('img') for f in pmpalettes]

for fn, movie in matches.items():
    if fn not in pmfiles:
        ct = titles.count(movie)
        titles.append(movie)
        title = movie
        pal = get_palette_pm(img)
        pal_img = show_key_colors(pal)
        pal_img.save("previews/"+make_filename(f"palettemaniac_{title}_full")+".png")

        if ct > 0:
            title = f"{title} #{ct}"

        img = Image.open(f"palettemaniac/{fn}")
        hws.append(img.size)

        pmpalettes.append({
            "img": fn,
            "source": "palettemaniac",
            "source_url": get_instagram_url(f"palettemaniac/{fn}"),
            "inspiration": movie,
            "img_obj": img.copy(),
            "title": title,
            "palettes": {"full": pal}
            })
    


readme = []
for p in sorted(pmpalettes, key=lambda x: x['title']):
    readme.append(f"## {p['title']}")
    for name, colors in p['palettes'].items():
        #pal_img = show_key_colors(colors)
        fn = "previews/"+make_filename(f"{p['source']}_{p['title']}_{name}")+".png"
        readme.append(f"### {name}")
        readme.append(f"![{p['title']}]({fn})")
    readme.append("---")

with open("palettemaniac.md", "w") as f:
    f.write("\n".join(readme))