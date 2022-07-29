from PIL import Image

img_orig = Image.open('Vertigo.jpg')

def edges_finder(image, factor):

    img_orig = image

    width, height = img_orig.size
    img_result = Image.new('RGBA', (width, height))

    for w in range(width):
        for h in range(height):

            borders_qty = 0
            colors = []
            srdncolor = 0

            r_orig, g_orig, b_orig = img_orig.getpixel((w, h))

            if h-1 > 0:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w, h-1))
                colors.append([r,g,b])

            if h-1 > 0 and w+1 < width:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w+1, h-1))
                colors.append([r, g, b])

            if w+1 < width:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w+1, h))
                colors.append([r, g, b])

            if h+1 < height and w+1 < width:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w+1, h+1))
                colors.append([r, g, b])

            if h+1 < height:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w, h+1))
                colors.append([r, g, b])

            if h+1 < height and w-1 > 0:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w-1, h+1))
                colors.append([r, g, b])

            if w-1 >= 0:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w-1, h))
                colors.append([r, g, b])

            if h-1 >= 0 and w-1 >=0:
                borders_qty+=1
                r, g, b = img_orig.getpixel((w, h - 1))
                colors.append([r, g, b])

            ocolor = (r_orig + g_orig + b_orig)/3
            ocolor = int(ocolor)

            for color in colors:
                color2 = (int(color[0]) + int(color[1]) + int(color[2]))/3
                srdncolor = srdncolor+color2

            srdncolor = srdncolor/borders_qty
            print(w/width*100, ' %')
            bwcolor = int(abs(ocolor-srdncolor)*factor)
            img_result.putpixel((w,h), (bwcolor, bwcolor, bwcolor, 255))

    return img_result

img_result = edges_finder(img_orig,10)
img_result.show()