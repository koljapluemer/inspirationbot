import csv

# loop forza.txt    
with open('../global/data/forzaOld.txt', 'r') as f:
    with open('../global/data/forza.txt', 'w') as w:
        for line in f:
            # split the line into image url and car profile url
            image_url, car_url = line.split()
            # get the car name from the car profile url
            fixed_image_url = image_url.split('revision/')[0]
            print(fixed_image_url)
            w.write(fixed_image_url + ' ' + car_url + '\n')