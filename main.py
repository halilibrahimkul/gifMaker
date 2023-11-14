from PIL import Image

image_path_list = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg','photo4.jpg','photo5.jpg']
image_list = [Image.open(file) for file in image_path_list]
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=1000, # in milliseconds
            loop=0)