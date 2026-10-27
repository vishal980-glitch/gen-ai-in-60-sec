"""Gen AI in 60 Sec - Day 40: Image = Numbers (Pixels)
Challenge: Pixels ke numbers badlo, image dekho
Run free in Google Colab - no setup needed.
"""
row1 = [0, 255, 0]
row2 = [255, 255, 255]
img = [row1, row2]
print("height:", len(img))
print("width :", len(img[0]))
print("pixel :", img[0][1])
bright = [[p // 2 for p in r] for r in img]
print(bright)
