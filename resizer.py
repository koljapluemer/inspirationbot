import sys
import os 
# get image path from arguments

file = sys.argv[1]

srcset = [
		"256x445",
		"660x1147",
		"900x1564",
		"1100x1912",
		"1270x2208",
		"1420x2468",
		"1550x2694",
		"1680x2920",
		"1790x3112"
       ]

# 285×120, 1183×500, 1690×714, 2071×875

srcset = [
        "285x120",
        "1183x500",
        "1690x714",
        "2071x875"
         ]

# 256×829, 495×1604, 650×2106, 778×2520, 868×2812, 980×3175, 1080×3499, 1170×3790, 1260×4082, 1340×4341, 1420×4600, 1490×4827, 1556×5041

srcset = [
        "256x829",
        "495x1604",
        "650x2106",
        "778x2520",
        "868x2812",
        "980x3175",
        "1080x3499",
        "1170x3790",
        "1260x4082",
        "1340x4341",
        "1420x4600",
        "1490x4827",
        "1556x5041"
        ]

# use convert to generate an image for each srcset
# actually execute the command
for size in srcset:
    command = f'convert {file} -resize {size} {file.split(".")[0]}-{size.split("x")[0]}.{file.split(".")[1]}'
    os.system(command)
