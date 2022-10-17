import matplotlib.pyplot as plt
import numpy as np
from matplotlib_scalebar.scalebar import ScaleBar


def fix_image_clims(mpl_images):
    for im in mpl_images[1:]:
        im.set_clim(mpl_images[0].get_clim())

def plot_mip(images, output_file=None, labels=None, axis=2):
    # A function to plot the maximum intensity projection.
    # make a maximum intensity projection
    if labels is None:
        labels = [""] * len(images)
    fig, axes = plt.subplots(1, len(images), figsize=(6.4*len(images), 4.8))
    if len(images) == 1:
        axes = [axes]
    mpl_images = []
    
    # Plot each image on a seperate subplot
    for ax, image, label in zip(axes, images, labels):
        im = ax.imshow(np.max(image, axis=axis), 
                   extent=(-0.06, 0.06, -0.06, 0.06))
        mpl_images.append(im)
        # Turn axes off
        ax.axis("off")
        ax.set_title(label)
        
        # Add a scale bar.
        s = ScaleBar(0.1, "m", location="lower right")
        ax.add_artist(s)
    
    fix_image_clims(mpl_images)
    
    # Fix the colour limits to the same thing.
    fig.suptitle(f"Maximum Intensity Projections")
    plt.colorbar(mpl_images[0], ax=axes, label="PA Signal")
    
    # Either save or show
    if output_file is not None:
        plt.savefig(f"{output_file}.png")
        plt.close()
    else:
        plt.show()